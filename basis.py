'''from xml_utils import clean_tag
import gml
'''

class Basis(object):
    """Parent class for all Basis Classes i.e. defined in bag.py."""

    csv_header = ''

    def __init__(self):
        # attributes
        self.id = 0

##        self.naam = ""
##        self.geometry = "" # in WKT notation
##        # for caching variable
##        self.tag = None
##        self.tag2process = {}
##        self.tag2field = {}
##        self.tag2object = {}
##
##    def set_id(self, value):
##        self.id = value
##        
##    def set_naam(self, value):
##        self.naam = value
##
##    def set_geometry(self, value):
##        self.geometry = value



    def as_sql_string(self, value):
        return value.replace("'", "''")
        

##    def _process(self, xml_element):
##        """Process an xml_element.
##        """
##        for i_elem in xml_element:
##            self.tag = clean_tag(i_elem.tag)
##            if self.tag2process.has_key(self.tag):
##                a_process = self.tag2process[self.tag]
##                a_process(i_elem)
##            
##    def _process_field(self, xml_element):
##        """Convert contents of xml_element into field_value."""
##        a_field = self.tag2field[self.tag]
##        
##        if self.tag2object.has_key(self.tag):
##            an_object = self.tag2object[self.tag]
##            value = an_object(xml_element).as_wkt()
##        else:
##            value = xml_element.text
##            
##        a_field(value)
            
        
