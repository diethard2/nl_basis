import unittest
import test.test_gml
import test.test_basis
import test.test_bag

def main():
    unit_test_suites =test.test_gml.unit_test_suites
    unit_test_suites.extend(test.test_basis.unit_test_suites)
    unit_test_suites.extend(test.test_bag.unit_test_suites)
    full_test_suite = unittest.TestSuite(unit_test_suites)
    unittest.TextTestRunner(verbosity=2).run(full_test_suite)
        
if __name__ == "__main__":
    main()
