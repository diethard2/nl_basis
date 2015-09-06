"""
/***************************************************************************
 bag bevat alle bag objecten gedefinieerd in de xml-bestanden in
 hierarchische volgorde.
 - Woonplaats
 - OpenbareRuimte
 - Pand
 - Verblijfsobject, Standplaats, Ligplaats
 - Nummeraanduiding
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
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("naam", "TEXT", "woonplaatsNaam"))
    obj.add_field(B_Field("geometry", "MULTIPOLYGON", "woonplaatsGeometrie",
                          to_object=gml.MultiPolygon))
    obj.add_tags_to_process()
    return obj

def pand():
    obj = B_Object("pand")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("bouwjaar", "TEXT", "bouwjaar"))
##    obj.add_field(B_Field("status", "TEXT", "pandstatus"))
    obj.add_field(B_Field("geometry", "POLYGON", "pandGeometrie",
                          to_object=gml.Polygon))
    obj.add_tags_to_process()
    return obj

def openbare_ruimte():
    obj = B_Object("openbare_ruimte")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("naam", "TEXT", "openbareRuimteNaam"))
    obj.add_field(B_Field("type", "TEXT", "openbareRuimteType"))
    obj.add_field(B_Field("id_woonplaats", "TEXT", "gerelateerdeWoonplaats",
                          to_object=BAG_Id))
    obj.add_tags_to_process()
    return obj

def verblijfsobject():
    obj = B_Object("verblijfsobject")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("gebruiksdoel", "TEXT",
                          "gebruiksdoelVerblijfsobject"))
    obj.add_field(B_Field("oppervlakte", "TEXT", "oppervlakteVerblijfsobject"))
    obj.add_field(B_Field("id_hoofdadres", "TEXT", "gerelateerdeAdressen",
                          to_object=BAG_Adressen))
    obj.add_field(B_Field("id_pand", "TEXT", "gerelateerdPand",
                          to_object=BAG_Id))
    obj.add_field(B_Field("geometry", "POINT", "verblijfsobjectGeometrie",
                          to_object=gml.Point))
    
    obj.add_tags_to_process()
    return obj

def standplaats():
    obj = B_Object("standplaats")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("id_hoofdadres", "TEXT", "gerelateerdeAdressen",
                          to_object=BAG_Adressen))
    obj.add_field(B_Field("geometry", "POLYGON", "standplaatsGeometrie",
                          to_object=gml.Polygon))
    obj.add_tags_to_process()
    return obj

def ligplaats():
    obj = B_Object("ligplaats")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("id_hoofdadres", "TEXT", "gerelateerdeAdressen",
                          to_object=BAG_Adressen))
    obj.add_field(B_Field("geometry", "POLYGON", "ligplaatsGeometrie",
                          to_object=gml.Polygon))
    obj.add_tags_to_process()
    return obj

def nummeraanduiding():
    obj = B_Object("nummeraanduiding")
    obj.add_field(B_Field("id", "TEXT", "identificatie", is_key_field=True))
    obj.add_field(B_Field("postcode", "TEXT", "postcode"))
    obj.add_field(B_Field("huisnummer", "TEXT", "huisnummer"))
    obj.add_field(B_Field("type", "TEXT", "typeAdresseerbaarObject",
                          is_mandatory=False))
    obj.add_field(B_Field("id_openbare_ruimte", "TEXT",
                          "gerelateerdeOpenbareRuimte", to_object=BAG_Id))
    obj.add_tags_to_process()
    return obj

def woonplaats_gemeente():
    obj = B_Object("woonplaats_gemeente")
    obj.add_field(B_Field("id_woonplaats", "TEXT", "gerelateerdeWoonplaats",
                          to_object=BAG_Id, is_key_field=True))
    obj.add_field(B_Field("id_gemeente", "TEXT", "gerelateerdeGemeente",
                          to_object=BAG_Id))
    obj.add_tags_to_process()
    return obj

def sql_creation_statements():
    sql_statements = []
    for i_basis_object in basis_objects.values():
        sql_statements.extend(i_basis_object.sql_create_table_statements())
    return sql_statements


class BAG_Id(B_XmlProcessor):
    """ To process xml_element gerelateerdeWoonplaats or gerelateerdePand
    which is part of xml object openbare ruimte
    """

    def __init__(self):
        B_XmlProcessor.__init__(self)
        self.id = ""
        self.add_tag_method_to_process("identificatie",self._process_id)

    def _process_id(self, elem):
        self.id = elem.text

    def as_text(self):
        return self.id

class BAG_Adressen(B_XmlProcessor):
    """ To process xml_element gerelateerdeAdressen which is part of
        several xml object elements
    """

    def __init__(self):
        B_XmlProcessor.__init__(self)
        self.id_hoofdadres = ""
        self.ids_nevenadressen = []
        self._add_tags_to_process()

    def _add_tags_to_process(self):
        self.add_tag_method_to_process("hoofdadres",self._process_hoofdadres)
        self.add_tag_method_to_process("nevenadres",self._process_nevenadres)

    def _process_hoofdadres(self, elem):
        self.id_hoofdadres = self._get_id(elem)
    
    def _process_nevenadres(self, elem):
        self.ids_nevenadressen.append(self._get_id(elem))

    def _get_id(self, elem):
        for i_elem in elem:
            tag = clean_tag(i_elem.tag)
            if tag == "identificatie":
                return i_elem.text

    def as_text(self):
        return self.id_hoofdadres
                

basis_objects = {"Woonplaats": woonplaats(),
                 "Pand": pand(),
                 "OpenbareRuimte": openbare_ruimte(),
                 "Verblijfsobject": verblijfsobject(),
                 "Standplaats": standplaats(),
                 "Ligplaats": ligplaats(),
                 "Nummeraanduiding": nummeraanduiding(),
                 "GemeenteWoonplaatsRelatie": woonplaats_gemeente()
                 }

