import unittest
import test_bag, test_gml

def main():
    unit_test_suites =test_gml.unit_test_suites
    unit_test_suites.extend(test_bag.unit_test_suites)
    full_test_suite = unittest.TestSuite(unit_test_suites)
    unittest.TextTestRunner(verbosity=2).run(full_test_suite)
        
if __name__ == "__main__":
    main()
