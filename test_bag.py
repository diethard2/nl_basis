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
                         "INSERT INTO bag_woonplaats (id, naam, geometry) \
VALUES ('1000', 'Hoogerheide', \
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
                         "INSERT INTO bag_woonplaats (id, naam, geometry) \
VALUES ('1197', 'Leeuwarden', \
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
                         ['id', 'bouwjaar', 'geometry'])

    def test_field_values(self):
        self.assertEqual(self.pand.field_values(),
                         ['1987100000011601', '2012', 
                          'Polygon((253680.97 576716.1, 253679.11 576736.32, \
253667.39 576735.3, 253669.21 576715.11, 253680.97 576716.1),\
(253679.875 576724.723, 253671.753 576723.992, 253671.406 576727.849, \
253679.528 576728.58, 253679.875 576724.723))'])

    def test_csv_header(self):
        self.assertEqual(self.pand.csv_header(), 'id;bouwjaar;geometry')

    def test_as_csv(self):
        self.assertEqual(self.pand.as_csv(),
                         '1987100000011601;2012;\
Polygon((253680.97 576716.1, 253679.11 576736.32, 253667.39 576735.3, \
253669.21 576715.11, 253680.97 576716.1),(253679.875 576724.723, \
253671.753 576723.992, 253671.406 576727.849, 253679.528 576728.58, \
253679.875 576724.723))')

    def test_as_sql(self):
        self.assertEqual(self.pand.as_sql(),
                         "INSERT INTO pand \
(id, bouwjaar, geometry) VALUES ('1987100000011601', \
'2012', GeomFromText('Polygon((253680.97 576716.1, \
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
                         "INSERT INTO bag_ligplaats \
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

class StandplaatsTestCase(unittest.TestCase):
    """
    Unittest to test standplaats

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the standplaats read from xml file standplaats.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/standplaats.xml")
        root = ET.fromstring(xml_file.read())
        xml_standplaats = find_xml_with_tag(root, "Standplaats", None)
        self.standplaats = bag.standplaats()
        self.standplaats.process(xml_standplaats)
        xml_file.close()        

    def test_field_names(self):
        self.assertEqual(self.standplaats.field_names(),
                         ['id', 'id_hoofdadres', 'geometry'])

    def test_field_values(self):
        self.assertEqual(self.standplaats.field_values(),
                         ['1730030000000161', '1730200000020033',
                          'Polygon((240292.542 568557.492, \
240297.926 568548.571, 240309.307 568554.416, 240304.385 568563.491, \
240292.542 568557.492))'])

    def test_csv_header(self):
        self.assertEqual(self.standplaats.csv_header(), 'id;id_hoofdadres;geometry')

    def test_as_csv(self):
        self.assertEqual(self.standplaats.as_csv(),
                         '1730030000000161;1730200000020033;\
Polygon((240292.542 568557.492, 240297.926 568548.571, 240309.307 568554.416, \
240304.385 568563.491, 240292.542 568557.492))')

    def test_as_sql(self):
        self.assertEqual(self.standplaats.as_sql(),
                         "INSERT INTO bag_standplaats \
(id, id_hoofdadres, geometry) VALUES ('1730030000000161', \
'1730200000020033', GeomFromText('Polygon((240292.542 568557.492, \
240297.926 568548.571, 240309.307 568554.416, 240304.385 568563.491, \
240292.542 568557.492))', 28992))")

_suite_standplaats = unittest.TestLoader().loadTestsFromTestCase(StandplaatsTestCase)


class OpenbareRuimteTestCase(unittest.TestCase):
    """
    Unittest to test openbare_ruimte

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the openbare_ruimte read from xml file openbare_ruimte.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/openbare_ruimte.xml")
        root = ET.fromstring(xml_file.read())
        xml_openbare_ruimte = find_xml_with_tag(root, "OpenbareRuimte", None)
        self.openbare_ruimte = bag.openbare_ruimte()
        self.openbare_ruimte.process(xml_openbare_ruimte)
        xml_file.close()

    def test_field_names(self):
        self.assertEqual(self.openbare_ruimte.field_names(),
                         ['id', 'naam', 'id_woonplaats'])

    def test_field_values(self):
        self.assertEqual(self.openbare_ruimte.field_values(),
                         ['1895300000000478', 'Oosthofflaan', '1893'])

    def test_csv_header(self):
        self.assertEqual(self.openbare_ruimte.csv_header(),
                         'id;naam;id_woonplaats')

    def test_as_csv(self):
        self.assertEqual(self.openbare_ruimte.as_csv(),
                         '1895300000000478;Oosthofflaan;1893')

    def test_as_sql(self):
        self.assertEqual(self.openbare_ruimte.as_sql(),
                         "INSERT INTO openbare_ruimte \
(id, naam, id_woonplaats) VALUES ('1895300000000478', 'Oosthofflaan', \
'1893')")

_suite_openbare_ruimte = unittest.TestLoader().loadTestsFromTestCase(OpenbareRuimteTestCase)

class NummeraanduidingTestCase(unittest.TestCase):
    """
    Unittest to test nummeraanduiding

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the nummeraanduiding read from xml file nummeraanduiding.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/nummeraanduiding.xml")
        root = ET.fromstring(xml_file.read())
        xml_nummeraanduiding = find_xml_with_tag(root, "Nummeraanduiding", None)
        self.nummeraanduiding = bag.nummeraanduiding()
        self.nummeraanduiding.process(xml_nummeraanduiding)
        xml_file.close()

    def test_field_names(self):
        self.assertEqual(self.nummeraanduiding.field_names(),
                         ['id', 'postcode', 'huisnummer', 'huisletter',
                          'huisnummertoevoeging', 'type', 'id_openbare_ruimte'])

    def test_field_values(self):
        self.assertEqual(self.nummeraanduiding.field_values(),
                         ['1987200000006076', '9651BG', '13', 'A', '1',
                          'Verblijfsobject', '1987300000000095'])

    def test_csv_header(self):
        self.assertEqual(self.nummeraanduiding.csv_header(),
                         'id;postcode;huisnummer;huisletter;huisnummertoevoeging;type;\
id_openbare_ruimte')

    def test_as_csv(self):
        self.assertEqual(self.nummeraanduiding.as_csv(),
                         '1987200000006076;9651BG;13;A;1;Verblijfsobject;\
1987300000000095')

    def test_as_sql(self):
        self.assertEqual(self.nummeraanduiding.as_sql(),
                         "INSERT INTO nummeraanduiding \
(id, postcode, huisnummer, huisletter, huisnummertoevoeging, type, id_openbare_ruimte) \
VALUES ('1987200000006076', '9651BG', 13, 'A', '1', 'Verblijfsobject', '1987300000000095')")

_suite_nummeraanduiding = unittest.TestLoader().loadTestsFromTestCase(NummeraanduidingTestCase)

class WoonplaatsGemeenteTestCase(unittest.TestCase):
    """
    Unittest to test woonplaats_gemeente

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the woonplaats_gemeente read from xml file woonplaats_gemeente.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/gemeentewoonplaatsrelatie.xml")
        root = ET.fromstring(xml_file.read())
        xml_woonplaats_gemeente = find_xml_with_tag(root,
                                                    "GemeenteWoonplaatsRelatie",
                                                    None)
        self.woonplaats_gemeente = bag.woonplaats_gemeente()
        self.woonplaats_gemeente.process(xml_woonplaats_gemeente)
        xml_file.close()

    def test_field_names(self):
        self.assertEqual(self.woonplaats_gemeente.field_names(),
                         ['id_woonplaats', 'id_gemeente'])

    def test_field_values(self):
        self.assertEqual(self.woonplaats_gemeente.field_values(),
                         ['3386', '0003'])

    def test_csv_header(self):
        self.assertEqual(self.woonplaats_gemeente.csv_header(),
                         'id_woonplaats;id_gemeente')

    def test_as_csv(self):
        self.assertEqual(self.woonplaats_gemeente.as_csv(),
                         '3386;0003')

    def test_as_sql(self):
        self.assertEqual(self.woonplaats_gemeente.as_sql(),
                         "INSERT INTO woonplaats_gemeente \
(id_woonplaats, id_gemeente) VALUES ('3386', '0003')")

_suite_woonplaats_gemeente = unittest.TestLoader().loadTestsFromTestCase(WoonplaatsGemeenteTestCase)

class VerblijfsobjectTestCase(unittest.TestCase):
    """
    Unittest to test verblijfsobject

    Run test from commandline in folder with code with following statement:
    python test_bag.py
    """
    def setUp(self):
        """
        For each test create the verblijfsobject read from xml file verblijfsobject.xml

        The geometry actually consists of an gml polygon element which includes
        an outer and inner ring.
        """
        xml_file = open("test/verblijfsobject.xml")
        root = ET.fromstring(xml_file.read())
        xml_verblijfsobject = find_xml_with_tag(root, "Verblijfsobject", None)
        self.verblijfsobject = bag.verblijfsobject()
        self.verblijfsobject.process(xml_verblijfsobject)
        xml_file.close()

    def test_field_names(self):
        self.assertEqual(self.verblijfsobject.field_names(),
                         ['id', 'gebruiksdoel', 'oppervlakte',
                          'id_hoofdadres', 'id_pand', 'geometry'])

    def test_field_values(self):
        self.assertEqual(self.verblijfsobject.field_values(),
                         ['0003010000125985', 'woonfunctie', '69',
                          '0003200000134057', '0003100000122770',
                          'Point(252767.348 593745.504)'])

    def test_csv_header(self):
        self.assertEqual(self.verblijfsobject.csv_header(),
                         'id;gebruiksdoel;oppervlakte;id_hoofdadres;\
id_pand;geometry')

    def test_as_csv(self):
        self.assertEqual(self.verblijfsobject.as_csv(),
                         '0003010000125985;woonfunctie;69;0003200000134057;\
0003100000122770;Point(252767.348 593745.504)')

    def test_as_sql(self):
        self.assertEqual(self.verblijfsobject.as_sql(),
                         "INSERT INTO bag_verblijfsobject \
(id, gebruiksdoel, oppervlakte, id_hoofdadres, id_pand, geometry) \
VALUES ('0003010000125985', 'woonfunctie', 69, '0003200000134057', \
'0003100000122770', GeomFromText('Point(252767.348 593745.504)', 28992))")

_suite_verblijfsobject = unittest.TestLoader().loadTestsFromTestCase(VerblijfsobjectTestCase)

unit_test_suites = [_suite_woonplaats1, _suite_woonplaats2, _suite_pand,
                    _suite_ligplaats, _suite_standplaats,
                    _suite_openbare_ruimte, _suite_nummeraanduiding,
                    _suite_woonplaats_gemeente, _suite_verblijfsobject]

def main():
    bag_test_suite = unittest.TestSuite(unit_test_suites)
    unittest.TextTestRunner(verbosity=2).run(bag_test_suite)
        
if __name__ == "__main__":
    main()
    

        
