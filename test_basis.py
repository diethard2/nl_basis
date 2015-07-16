"""
/***************************************************************************
 Unit test suite to test basis objects, B_Field and B_Object
 -------------------
 begin                : 14-07-2015
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
import basis, gml
import unittest
from xml_utils import *
import xml.etree.ElementTree as ET

class B_FieldRegularTestCase(unittest.TestCase):
    """
    unittests to test Regular text basis Field B_Field
    """

    def setUp(self):
        """
        Setup a test create a regular B_Field.
        """
        self.field = basis.B_Field("naam", "TEXT")

    def test_field_name(self):
        self.assertEqual(self.field.name, "naam")

    def test_field_type(self):
        self.assertEqual(self.field.type, "TEXT")

    def test_is_mandatory(self):
        self.assertEqual(self.field.is_mandatory, True)

    def test_is_key_field(self):
        self.assertEqual(self.field.is_key_field, False)
        
    def test_is_tag2object(self):
        self.assertEqual(self.field.tag2object, ())

    def test_set_value(self):
        self.field.value = "Nico"
        self.assertEqual(self.field.value, "Nico")
        
    def test_sql_value(self):
        self.field.value = "'s Hertogenbosch"
        self.assertEqual(self.field.sql_value(), "'''s Hertogenbosch'")

    def test_is_geometry(self):
        self.assertEqual(self.field.is_geometry(), False)
        
    def test_sql_definition(self):
        self.assertEqual(self.field.sql_definition(), "naam TEXT NOT NULL")
        
_suite_b_field_regular = unittest.TestLoader().loadTestsFromTestCase(B_FieldRegularTestCase)

class B_FieldSpecialTestCase(unittest.TestCase):
    """
    unittests to test special cases of B_Field
    """

    def test_is_key_field(self):
        field = basis.B_Field("id", "INTEGER", is_key_field=True)
        self.assertEqual(field.is_key_field, True)
        
    def test_integer_value_as_sql(self):
        field = basis.B_Field("nr", "INTEGER")
        field.value = "20"
        self.assertEqual(field.sql_value(), '20')        

    def test_key_field_definition(self):
        """
        Test a created key field.
        """
        field = basis.B_Field("id", "INTEGER", is_key_field=True)
        self.assertEqual(field.sql_definition(),
                         'id INTEGER NOT NULL PRIMARY KEY')

    def test_is_geometry(self):
        field = basis.B_Field("geometry", "MULTIPOLYGON")
        self.assertEqual(field.is_geometry(), True)


_suite_b_field_special = unittest.TestLoader().loadTestsFromTestCase(B_FieldSpecialTestCase)

class B_ObjectTestCase(unittest.TestCase):
    """
    unittests to test basic object, in this case a woonplaats..
    """
    def setUp(self):
        """
        For each test create a woonplaats read from xml file woonplaats.xml
        
        This unit_test is actually not an example how to create new objects.
        Objects should be subclassed! But in this case it is tested if it
        can be used to actually processes an xml element representing
        a BAG object.
        """
        woonplaats = basis.B_Object("woonplaats")
        # to be included in init of derived classes, adding fields..
        field_id = basis.B_Field("id", "INTEGER", is_key_field=True)
        woonplaats.add_field("identificatie", field_id)
        field_name = basis.B_Field("naam", "TEXT")
        woonplaats.add_field("woonplaatsNaam", field_name)
        field_geometry = basis.B_Field("geometry", "MULTIPOLYGON",
                                       tag2object=("woonplaatsGeometrie",
                                                   gml.MultiPolygon))
        woonplaats.add_field("woonplaatsGeometrie", field_geometry)
        # include also how to process each tag found for object..
        # after creation.. (i.e. using method add_tags_to_process())
        woonplaats.add_tags_to_process()
        # to call from reader class (for each xml tag for this object
        # encountered.
        xml_file = open("test/woonplaats.xml")
        root = ET.fromstring(xml_file.read())
        xml_woonplaats = find_xml_with_tag(root, "Woonplaats", None)
        woonplaats.process(xml_woonplaats)
        self.woonplaats = woonplaats
        xml_file.close()

    def test_field_names(self):
        self.assertEqual(self.woonplaats.field_names(),
                         ['id', 'naam', 'geometry'])

    def test_field_values(self):
        self.assertEqual(self.woonplaats.field_values(),
                         ['1000', 'Hoogerheide',
                          'MultiPolygon(((80089.798 383288.255, \
81816.255 383744.931, 82005.608 381650.906, 80769.242 381394.722, \
80089.798 383288.255),(80758.104 383310.532, 81704.871 383455.332, \
81348.441 382809.303, 80802.658 382820.441, 80758.104 383310.532)))'])

    def test_field_types(self):
        self.assertEqual(self.woonplaats.field_types(),
                         ["INTEGER", "TEXT", "MULTIPOLYGON"])

    def test_field_names_and_sql_values(self):
        self.assertEqual(self.woonplaats.field_names_and_sql_values(),
                         (['id', 'naam', 'geometry'],
                          ['1000', "'Hoogerheide'",
                           "GeomFromText('MultiPolygon(((80089.798 \
383288.255, 81816.255 383744.931, 82005.608 381650.906, \
80769.242 381394.722, 80089.798 383288.255),(80758.104 383310.532, \
81704.871 383455.332, 81348.441 382809.303, 80802.658 382820.441, \
80758.104 383310.532)))', 28992)"]))

    def test_csv_header(self):
        self.assertEqual(self.woonplaats.csv_header(),
                         'id;naam;geometry')

    def test_as_csv(self):
        self.assertEqual(self.woonplaats.as_csv(),
                         '1000;Hoogerheide;MultiPolygon(((80089.798 \
383288.255, 81816.255 383744.931, 82005.608 381650.906, \
80769.242 381394.722, 80089.798 383288.255),(80758.104 383310.532, \
81704.871 383455.332, 81348.441 382809.303, 80802.658 382820.441, \
80758.104 383310.532)))')

    def test_as_sql(self):
        self.assertEqual(self.woonplaats.as_sql(),
                         "INSERT INTO woonplaats (id, naam, geometry) \
VALUES (1000, 'Hoogerheide', GeomFromText('MultiPolygon(((80089.798 \
383288.255, 81816.255 383744.931, 82005.608 381650.906, \
80769.242 381394.722, 80089.798 383288.255),(80758.104 383310.532, \
81704.871 383455.332, 81348.441 382809.303, 80802.658 382820.441, \
80758.104 383310.532)))', 28992))")

    def test_sql_drop_table_statement(self):
        self.assertEqual(self.woonplaats.sql_drop_table_statement(),
                         "DROP TABLE if exists woonplaats")

    def test_sql_create_table_statement(self):
        self.assertEqual(self.woonplaats.sql_create_table_statement(),
                         "CREATE TABLE woonplaats (id INTEGER NOT NULL \
PRIMARY KEY,naam TEXT NOT NULL)")

    def test_sql_add_geometry_statement(self):
        self.assertEqual(self.woonplaats.sql_add_geometry_statement(),
                         "SELECT AddGeometryColumn('woonplaats', 'geometry', \
28992, 'MULTIPOLYGON', 'XY')")

    def test_sql_create_index_statement(self):
        self.assertEqual(self.woonplaats.sql_create_index_statement(),
                         "SELECT CreateSpatialIndex('woonplaats', 'geometry')")
                             
_suite_b_object = unittest.TestLoader().loadTestsFromTestCase(B_ObjectTestCase)

unit_test_suites = [_suite_b_field_regular, _suite_b_field_special,
                    _suite_b_object]

def main():
    basis_test_suite = unittest.TestSuite(unit_test_suites)
    unittest.TextTestRunner(verbosity=2).run(basis_test_suite)
        
if __name__ == "__main__":
    main()
    

        
