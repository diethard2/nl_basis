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
import gml
from basis import *


def woonplaats():
    obj = B_Object("woonplaats")
    obj.add_field(B_Field("id", "INTEGER", "identificatie", is_key_field=True))
    obj.add_field(B_Field("naam", "TEXT", "woonplaatsNaam"))
    obj.add_field(B_Field("geometry", "MULTIPOLYGON", "woonplaatsGeometrie",
                          to_object=gml.MultiPolygon))
    obj.add_tags_to_process()
    return obj

def pand():
    obj = B_Object("pand")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("bouwjaar", "TEXT", "bouwjaar"))
    obj.add_field(B_Field("status", "TEXT", "pandstatus"))
    obj.add_field(B_Field("geometry", "POLYGON", "pandGeometrie",
                          to_object=gml.Polygon))
    obj.add_tags_to_process()
    return obj

def openbare_ruimte():
    obj = B_Object("openbare_ruimte")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_tags_to_process()
    return obj

def verblijfsobject():
    obj = B_Object("verblijfsobject")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_tags_to_process()
    return obj

def standplaats():
    obj = B_Object("standplaats")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_tags_to_process()
    return obj

def ligplaats():
    obj = B_Object("ligplaats")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_tags_to_process()
    return obj

def nummer():
    obj = B_Object("nummer")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_tags_to_process()
    return obj

def gemeente_woonplaats():
    obj = B_Object("gemeente_woonplaats")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_tags_to_process()
    return obj

##tag2object = {"woonplaats",
##              "pand",
##              "openbare_ruimte",
##              "verblijfsobject",
##              "standplaats",
##              "ligplaats",
##              "nummer",
##              "gemeente_woonplaats"}

basis_objects = {"Woonplaats": woonplaats(),
                 "Pand": pand(),
                 "openbareRuimte": openbare_ruimte(),
                 "verblijfsobject": verblijfsobject(),
                 "Standplaats": standplaats(),
                 "Ligplaats": ligplaats(),
                 "Nummer": nummer(),
                 "Gemeente_woonplaats": gemeente_woonplaats()
                 }

