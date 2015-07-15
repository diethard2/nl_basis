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
import basis
import unittest

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


unit_test_suites = [_suite_b_field_regular, _suite_b_field_special]

def main():
    basis_test_suite = unittest.TestSuite(unit_test_suites)
    unittest.TextTestRunner(verbosity=2).run(basis_test_suite)
        
if __name__ == "__main__":
    main()
    

        
