"""
/***************************************************************************
 bag bevat alle bag objecten gedefinieerd in de xml-bestanden in
 hierarchische volgorde.
 - Woonplaats
 - OpenbareRuimte
 - Pand
 - Verblijfsobject, Standplaats, Ligplaats
 - Nummer
 - GemeenteWoonplaats (koppeling tussen gemeente en woonplaatsen)
 -------------------
 begin                : 2015-06-01
 copyright            : (C) 2015 by Diethard Jansen
 email                : Diethard.Jansen at Gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from xml_utils import clean_tag
import gml

class Woonplaats:
    """ Woonplaats is het object waarin gegevens tijdens verwerking worden
    opgeslagen en bevat functies om deze als csv of als sql weer terug te geven. 
    """

    # kopregel van een woonplaats in een csv
    csv_header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Woonplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object Woonplaats aan te maken en te vullen.
        """
        # attributes
        self.id = 0
        self.naam = ""
        self.geometry = "" # in WKT notation
        # method to fill attributes
        self._process(xml_element)

    def _process(self, xml_element):
        """Vult de eigenschappen vanuit het xml_element.
        """
        for i_elem in xml_element:
            tag = clean_tag(i_elem.tag)
            if tag == "identificatie":
                self.id = i_elem.text
                continue
            if tag == "woonplaatsNaam":
                self.naam = i_elem.text
                continue 
            if tag == "woonplaatsGeometrie":
                self.geometry = gml.MultiPolygon(i_elem).as_wkt()                

    def as_csv(self):
        attributes = [self.id, self.naam, self.geometry]
        return ";".join(attributes)

    def as_sql(self):
        sql = "INSERT INTO woonplaats (id, naam, geometry) \
VALUES (%s, '%s', GeomFromText('%s', 28992))" % (self.id, self.naam, self.geometry)
        return sql


class OpenbareRuimte:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """OpenbareRuimte(elem), xml_element = xml-tree die alle informatie bevat
        om een object OpenbareRuimte aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)


class Pand:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Pand(elem), xml_element = xml-tree die alle informatie bevat
        om een object Pand aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)


class Verblijfsobject:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Verblijfsobject(elem), xml_element = xml-tree die alle informatie bevat
        om een object Verblijfsobject aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)

class Standplaats:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Standplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object Standplaats aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)

class Ligplaats:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Ligplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object Ligplaats aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)

class Nummer:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Nummer(elem), xml_element = xml-tree die alle informatie bevat
        om een object Nummer aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)

class GemeenteWoonplaats:

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """GemeenteWoonplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object GemeenteWoonplaats aan te maken en te vullen.
        """
        self.id = 0

    def as_csv(self):
        a_list = ['%04d' % self.id,
                  self.naam, self.geom_wkt]
        return ";".join(a_list)

    def as_sql(self):
        sql = "INSERT INTO  (id, naam, geom) \
VALUES ('%04d', '%s', GeomFromText('%s', \
28992))" % (self.id, self.naam, self.geom_wkt)

