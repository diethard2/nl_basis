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
from basis import Basis
from xml_utils import clean_tag
import gml


class Woonplaats(Basis):
    """ Woonplaats is het object waarin gegevens tijdens verwerking worden
    opgeslagen en bevat functies om deze als csv of als sql weer terug te geven. 
    """

    # kopregel van een woonplaats in een csv
    csv_header = 'id;naam;geometry'

    def __init__(self, xml_element):
        """Woonplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object Woonplaats aan te maken en te vullen.
        """
        super(Basis, self).__init__()
        
        self.tag2process = {"identificatie": self._process_field,
                            "woonplaatsNaam": self._process_field,
                            "woonplaatsGeometrie": self._process_field}
        self.tag2field = {"identificatie": self.set_id,
                          "woonplaatsNaam": self.set_naam,
                          "woonplaatsGeometrie": self.set_geometry}
        self.tag2object = {"woonplaatsGeometrie": gml.MultiPolygon}

        self._process(xml_element)
    
    def as_csv(self):
        attributes = [self.id, self.naam, self.geometry]
        return ";".join(attributes)

    def as_sql(self):
        sql = "INSERT INTO woonplaats (id, naam, geometry) \
VALUES (%s, '%s', GeomFromText('%s', 28992))" % (self.id,
                                                 self.as_sql_string(self.naam),
                                                 self.geometry)
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

