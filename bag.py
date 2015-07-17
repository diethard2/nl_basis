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
from basis import *

class Woonplaats(B_Object):
    """ Woonplaats is het object waarin gegevens tijdens verwerking worden
    opgeslagen en bevat functies om deze als csv of als sql weer terug
    te geven. 
    """

    def __init__(self):
        """Woonplaats is een vlakobject die kan bestaan uit meerdere polygonen.
        """
        B_Object.__init__(self, "woonplaats")
        self.add_field(B_Field("id", "INTEGER", "identificatie",
                               is_key_field=True))
        self.add_field(B_Field("naam", "TEXT", "woonplaatsNaam"))
        self.add_field(B_Field("geometry", "MULTIPOLYGON",
                               "woonplaatsGeometrie",
                               to_object=gml.MultiPolygon))

class OpenbareRuimte(B_Object):

    # kopregel van een in  een csv-bestand
    header = 'id;naam;geometry'

    def __init__(self):
        """OpenbareRuimte(elem), xml_element = xml-tree die alle informatie bevat
        om een object OpenbareRuimte aan te maken en te vullen.
        """
        B_Object.__init__(self, "openbare_ruimte")
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))

class Pand:

    def __init__(self):
        """Pand(elem), xml_element = xml-tree die alle informatie bevat
        om een object Pand aan te maken en te vullen.
        """
        B_Object.__init__(self, "pand")
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))
        self.add_field(B_Field("bouwjaar", "TEXT", "bouwjaar"))
        self.add_field(B_Field("status", "TEXT", "pandstatus"))
        self.add_field(B_Field("geometry", "POLYGON",
                               "pandGeometrie",
                               to_object=gml.Polygon))

class Verblijfsobject:

    def __init__(self):
        """Verblijfsobject(elem), xml_element = xml-tree die alle informatie bevat
        om een object Verblijfsobject aan te maken en te vullen.
        """
        B_Object.__init__(self, "verblijfsobject")
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))


class Standplaats:

    def __init__(self):
        """Standplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object Standplaats aan te maken en te vullen.
        """
        B_Object.__init__(self, "standplaats")

    def add_fields(self):
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))

class Ligplaats:

    def __init__(self):
        """Ligplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object Ligplaats aan te maken en te vullen.
        """
        B_Object.__init__(self, "ligplaats")
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))

class Nummer:

    def __init__(self):
        """Nummer(elem), xml_element = xml-tree die alle informatie bevat
        om een object Nummer aan te maken en te vullen.
        """
        B_Object.__init__(self, "nummer")
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))

class GemeenteWoonplaats:

    def __init__(self):
        """GemeenteWoonplaats(elem), xml_element = xml-tree die alle informatie bevat
        om een object GemeenteWoonplaats aan te maken en te vullen.
        """
        B_Object.__init__(self, "gemeente_woonplaats")
        self.add_field(B_Field("id", "TEXT", "identificatie",
                               is_key_field=True))


