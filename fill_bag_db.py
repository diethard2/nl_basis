'''
/***************************************************************************
Fill BAG db with data

begin                : 2015-06-19 
copyright            : (C) 2015 by Diethard Jansen
email                : diethard.jansen at gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
'''
import os, zipfile, re
from xml_utils import clean_tag
from cStringIO import StringIO
import xml.etree.cElementTree as ET
from pyspatialite import dbapi2
import codecs
import bag

class FillDB:
    
    def __init__(self, spatialite_db, p_dir):
        self.db = spatialite_db
        self._dir = p_dir
        self._file = None
        self._conn = None
        self._cur = None
        self._root = None
        self._xml_object_count = 0
        self._tag2process = {"producten": self._process_xml_element,
                             "LVC-product": self._process_LVC_product}
        self._tag = None
        self.TAG_BAG_OBJECTS = {"Woonplaats": bag.Woonplaats}

    def run(self):
        self._conn = dbapi2.connect(self.db)
        self._cur = self._conn.cursor()
        for root, dirs, files in os.walk(self._dir):
            for name in files:
                if 'Tabel33' in name:
                    self.process_gemeententabel(root, name)
                elif name == 'inspireadressen.zip':
                    self.process_bag_zipfile(root, name)
                else:
                    self.process_xml_file(root, name)
        self._conn.close()

    def _file_from(self, root, name):
        a_file = os.path.join(root, name)
        return os.path.realpath(a_file)

    def _clean_line(self, line):
        line = line.replace('\x00', '')
        line = line.replace('"', '')
        line = line.replace('\xff\xfe', '')
        line = line.replace("'", "''")
        line = line.strip()
        return line

    def process_gemeententabel(self, root, name):
        csv_file = self._file_from(root, name)
        print csv_file
        line_count = 0
        values = []
        for line in open(csv_file):
            line_count += 1
            if line_count == 1:
                continue
            line = self._clean_line(line)
            fields = line.split(',')
            if fields[2] == '':
                gemeentecode = fields[0]
                name = fields[1]
                sql = "INSERT INTO gemeente VALUES ('%s', '%s')" % \
                      (gemeentecode, name)
                self._cur.execute(sql)
        self._conn.commit()

    def process_bag_zipfile(self, root, name):
        zip_file = self._file_from(root, name)
        self._process_zip_in_zip(zip_file)
                        
    def _process_zip_in_zip(self, zip_file):
        with zipfile.ZipFile(zip_file, "r") as zfile:
            for name in zfile.namelist():
                if re.search(r'\.zip$', name) != None:
                    # We have a zip within a zip
                    print "Found zipped zipfile: " + name
                    zfiledata = StringIO(zfile.read(name))
                    self._process_xmls_in_zip(zfiledata)

    def _process_xmls_in_zip(self, zfiledata):
        with zipfile.ZipFile(zfiledata) as zfile:
            for file_name in zfile.namelist():
                if re.search(r'\.xml$', file_name) != None:
                    # We have an xml in a zip within a zip
                    xml_file = zfile.open(file_name)
                    self._process_zipped_xml_file(xml_file)
                 
    def _process_zipped_xml_file(self, xml_file):
        # read the xml file and process Bag Compact addresses
##        print "Verwerk bestand: " + xml_file
        self._root = ET.fromstring(xml_file.read())
        for i_elem in self._root:
            self._process_xml_element(i_elem)
        
    def process_xml_file(self, root, name):
        # read the xml file and process Bag Compact addresses
        xml_file = self._file_from(root, name)
        print "Verwerk bestand: " + xml_file
        an_iterator = ET.iterparse(xml_file, events=("start", "end"))
        # get the root element..
        event, self._root = an_iterator.next()
        
        for event, elem in an_iterator:
            if event == "end":
                tag = clean_tag(elem.tag)
                if tag == "antwoord":
                    self._process_xml_element(elem)
        self._conn.commit()

    def _process_xml_element(self, xml_element):
        """Process an xml_element.
        """
        for i_elem in xml_element:
            self._tag = clean_tag(i_elem.tag)
            if self._tag2process.has_key(self._tag):
                a_process = self._tag2process[self._tag]
                a_process(i_elem)

    def _process_LVC_product(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            tag_bag_objects = self.TAG_BAG_OBJECTS
            if tag_bag_objects.has_key(tag):
                bag_object_class = tag_bag_objects[tag]
                bag_object = bag_object_class(i_elem)
                sql = bag_object.as_sql()
                try:
                    self._cur.execute(sql)
                except dbapi2.IntegrityError:
                    # objects with unique ids are encountered more often in
                    # xml files delivered. Just ignore..
                    pass
                self._xml_object_count += 1
                i_elem.clear()
                if self._xml_object_count % 100 is 0:
                    self._root.clear()            
        
        
