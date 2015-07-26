"""
/***************************************************************************
 Unit test suite to test bag objects.
 -------------------
 begin                : 26-06-2015
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
import bag
from xml_utils import *
import xml.etree.ElementTree as ET
import unittest

class WoonplaatsTestCase(unittest.TestCase):
    """
    First unittest to test Woonplaats

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the Woonplaats read from xml file woonplaats.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/woonplaats.xml")
        root = ET.fromstring(xml_file.read())
        xml_woonplaats = find_xml_with_tag(root, "Woonplaats", None)
        self.woonplaats = bag.woonplaats()
        self.woonplaats.process(xml_woonplaats)
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

    def test_csv_header(self):
        self.assertEqual(self.woonplaats.csv_header(), 'id;naam;geometry')

    def test_as_csv(self):
        self.assertEqual(self.woonplaats.as_csv(),
                         '1000;Hoogerheide;MultiPolygon(((80089.798 383288.255, \
81816.255 383744.931, 82005.608 381650.906, 80769.242 381394.722, \
80089.798 383288.255),(80758.104 383310.532, 81704.871 383455.332, \
81348.441 382809.303, 80802.658 382820.441, 80758.104 383310.532)))')

    def test_as_sql(self):
        self.assertEqual(self.woonplaats.as_sql(),
                         "INSERT INTO woonplaats (id, naam, geometry) \
VALUES (1000, 'Hoogerheide', \
GeomFromText('MultiPolygon(((80089.798 383288.255, 81816.255 383744.931, \
82005.608 381650.906, 80769.242 381394.722, 80089.798 383288.255),\
(80758.104 383310.532, 81704.871 383455.332, 81348.441 382809.303, \
80802.658 382820.441, 80758.104 383310.532)))', 28992))")

_suite_woonplaats1 = unittest.TestLoader().loadTestsFromTestCase(WoonplaatsTestCase)
                         
class WoonplaatsMultipolygonTestCase(unittest.TestCase):
    """
    Second unittest to test Woonplaats with MultiPolygon 

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the Woonplaats read from xml file
        woonplaats_multipolygon.xml

        The geometry actually consists of two seperate gml polygon elements
        which the first polygon includes two inner rings.
        """
        xml_file = open("test/woonplaats_multipolygon.xml")
        root = ET.fromstring(xml_file.read())
        xml_woonplaats = find_xml_with_tag(root, "Woonplaats", None)
        self.woonplaats = bag.woonplaats()
        self.woonplaats.process(xml_woonplaats)
        xml_file.close()        

    def test_as_csv(self):
        self.assertEqual(self.woonplaats.as_csv(),
                         '1197;Leeuwarden;MultiPolygon(((180001.576 580918.246, \
186053.377 581436.193, 186462.283 578137.688, 180328.700 577510.700, \
180001.576 580918.246),(181733.025 579596.742, 181911.214 579873.924, \
182049.805 579576.943, 181733.025 579596.742),(185257.193 579586.843, \
185366.086 579784.830, 185534.375 579636.339, 185257.193 579586.843)),\
((184247.460 577379.288, 185435.382 577735.665, 185544.274 577112.006, \
184445.447 576914.019, 184247.460 577379.288)))')

    def test_as_sql(self):
        self.assertEqual(self.woonplaats.as_sql(),
                         "INSERT INTO woonplaats (id, naam, geometry) \
VALUES (1197, 'Leeuwarden', \
GeomFromText('MultiPolygon(((180001.576 580918.246, \
186053.377 581436.193, 186462.283 578137.688, 180328.700 577510.700, \
180001.576 580918.246),(181733.025 579596.742, 181911.214 579873.924, \
182049.805 579576.943, 181733.025 579596.742),(185257.193 579586.843, \
185366.086 579784.830, 185534.375 579636.339, 185257.193 579586.843)),\
((184247.460 577379.288, 185435.382 577735.665, 185544.274 577112.006, \
184445.447 576914.019, 184247.460 577379.288)))', 28992))")

_suite_woonplaats2 = unittest.TestLoader().loadTestsFromTestCase(WoonplaatsMultipolygonTestCase)

class PandTestCase(unittest.TestCase):
    """
    Unittest to test Pand

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the Pand read from xml file pand.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/pand.xml")
        root = ET.fromstring(xml_file.read())
        xml_pand = find_xml_with_tag(root, "Pand", None)
        self.pand = bag.pand()
        self.pand.process(xml_pand)
        xml_file.close()        

    def test_field_names(self):
        self.assertEqual(self.pand.field_names(),
                         ['id', 'bouwjaar', 'status', 'geometry'])

    def test_field_values(self):
        self.assertEqual(self.pand.field_values(),
                         ['1987100000011601', '2012', 'Pand in gebruik',
                          'Polygon((253680.97 576716.1, 253679.11 576736.32, \
253667.39 576735.3, 253669.21 576715.11, 253680.97 576716.1),\
(253679.875 576724.723, 253671.753 576723.992, 253671.406 576727.849, \
253679.528 576728.58, 253679.875 576724.723))'])

    def test_csv_header(self):
        self.assertEqual(self.pand.csv_header(), 'id;bouwjaar;status;geometry')

    def test_as_csv(self):
        self.assertEqual(self.pand.as_csv(),
                         '1987100000011601;2012;Pand in gebruik;\
Polygon((253680.97 576716.1, 253679.11 576736.32, 253667.39 576735.3, \
253669.21 576715.11, 253680.97 576716.1),(253679.875 576724.723, \
253671.753 576723.992, 253671.406 576727.849, 253679.528 576728.58, \
253679.875 576724.723))')

    def test_as_sql(self):
        self.assertEqual(self.pand.as_sql(),
                         "INSERT INTO pand \
(id, bouwjaar, status, geometry) VALUES ('1987100000011601', \
'2012', 'Pand in gebruik', GeomFromText('Polygon((253680.97 576716.1, \
253679.11 576736.32, 253667.39 576735.3, 253669.21 576715.11, \
253680.97 576716.1),(253679.875 576724.723, 253671.753 576723.992, \
253671.406 576727.849, 253679.528 576728.58, 253679.875 576724.723))', 28992))")

_suite_pand = unittest.TestLoader().loadTestsFromTestCase(PandTestCase)

class LigplaatsTestCase(unittest.TestCase):
    """
    Unittest to test ligplaats

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the ligplaats read from xml file ligplaats.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/ligplaats.xml")
        root = ET.fromstring(xml_file.read())
        xml_ligplaats = find_xml_with_tag(root, "Ligplaats", None)
        self.ligplaats = bag.ligplaats()
        self.ligplaats.process(xml_ligplaats)
        xml_file.close()        

    def test_field_names(self):
        self.assertEqual(self.ligplaats.field_names(),
                         ['id', 'id_hoofdadres', 'geometry'])

    def test_field_values(self):
        self.assertEqual(self.ligplaats.field_values(),
                         ['0479020000000242', '0479200000077867',
                          'Polygon((111768.489 494373.227, \
111777.876 494372.193, 111792.324 494370.6, 111792.359 494370.824, \
111793.299 494376.881, 111795.039 494382.906, 111796.098 494386.936, \
111796.657 494391.202, 111796.698 494394.091, 111796.701 494394.332, \
111782.216 494395.467, 111770.828 494396.359, 111769.647 494382.898, \
111768.489 494373.227))'])

    def test_csv_header(self):
        self.assertEqual(self.ligplaats.csv_header(), 'id;id_hoofdadres;geometry')

    def test_as_csv(self):
        self.assertEqual(self.ligplaats.as_csv(),
                         '0479020000000242;0479200000077867;\
Polygon((111768.489 494373.227, 111777.876 494372.193, 111792.324 494370.6, \
111792.359 494370.824, 111793.299 494376.881, 111795.039 494382.906, \
111796.098 494386.936, 111796.657 494391.202, 111796.698 494394.091, \
111796.701 494394.332, 111782.216 494395.467, 111770.828 494396.359, \
111769.647 494382.898, 111768.489 494373.227))')

    def test_as_sql(self):
        self.assertEqual(self.ligplaats.as_sql(),
                         "INSERT INTO ligplaats \
(id, id_hoofdadres, geometry) VALUES ('0479020000000242', \
'0479200000077867', GeomFromText('Polygon((111768.489 494373.227, \
111777.876 494372.193, 111792.324 494370.6, 111792.359 494370.824, \
111793.299 494376.881, 111795.039 494382.906, 111796.098 494386.936, \
111796.657 494391.202, 111796.698 494394.091, 111796.701 494394.332, \
111782.216 494395.467, 111770.828 494396.359, 111769.647 494382.898, \
111768.489 494373.227))', 28992))")

##    def test_ids_nevenadressen(self):
##        self.assertEqual(self.ligplaats.ids_nevenadressen,
##                         {'0513200000029680', '0513200000041049'})

_suite_ligplaats = unittest.TestLoader().loadTestsFromTestCase(LigplaatsTestCase)

unit_test_suites = [_suite_woonplaats1, _suite_woonplaats2, _suite_pand,
                    _suite_ligplaats]

def main():
    bag_test_suite = unittest.TestSuite(unit_test_suites)
    unittest.TextTestRunner(verbosity=2).run(bag_test_suite)
        
if __name__ == "__main__":
    main()
    

        
