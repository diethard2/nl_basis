CREATE TABLE woonplaats 
(id TEXT NOT NULL PRIMARY KEY,
 naam TEXT,
 gemeente TEXT)
--
SELECT AddGeometryColumn('woonplaats', 'geometry', 28992, 'MULTIPOLYGON', 'XY')
--
SELECT CreateSpatialIndex('woonplaats', 'geometry')
--
INSERT INTO woonplaats
(id, naam, gemeente, geometry) 
SELECT id, naam, gemeentenaam, geometry FROM view_woonplaats
--
CREATE TABLE verblijfsobject 
(id TEXT NOT NULL PRIMARY KEY,
 straat TEXT,
 huisnummer TEXT,
 postcode TEXT,
 woonplaats TEXT,
 gemeente TEXT,
 oppervlakte TEXT,
 gebruiksdoel TEXT,
 openbare_ruimte TEXT,
 id_pand TEXT)
--
SELECT AddGeometryColumn('verblijfsobject', 'geometry', 28992, 'POINT', 'XY')
--
SELECT CreateSpatialIndex('verblijfsobject', 'geometry')
--
CREATE INDEX idx_adres_id_pand
ON verblijfsobject (id_pand)
--
INSERT INTO verblijfsobject 
(id, straat, huisnummer, postcode, woonplaats, gemeente, oppervlakte, gebruiksdoel, openbare_ruimte, id_pand, geometry)
SELECT id, naam_openbare_ruimte, huisnummer, postcode, woonplaats, gemeente, oppervlakte, gebruiksdoel, type_openbare_ruimte, id_pand, geometry FROM view_verblijfsobject
--
CREATE TABLE ligplaats
(id TEXT NOT NULL PRIMARY KEY,
 naam_openbare_ruimte TEXT,
 huisnummer TEXT,
 postcode TEXT,
 woonplaats TEXT,
 gemeente TEXT,
 type_openbare_ruimte TEXT)
--
SELECT AddGeometryColumn('ligplaats', 'geometry', 28992, 'POLYGON', 'XY')
--
SELECT CreateSpatialIndex('ligplaats', 'geometry')
--
INSERT INTO ligplaats
(id, naam_openbare_ruimte, huisnummer, postcode, woonplaats, gemeente, type_openbare_ruimte, geometry)
SELECT id, naam_openbare_ruimte, huisnummer, postcode, woonplaats, gemeente, type_openbare_ruimte, geometry 
FROM view_ligplaats
--
CREATE TABLE standplaats
(id TEXT NOT NULL PRIMARY KEY,
 naam_openbare_ruimte TEXT,
 huisnummer TEXT,
 postcode TEXT,
 woonplaats TEXT,
 gemeente TEXT,
 openbare_ruimte TEXT)
--
SELECT AddGeometryColumn('standplaats', 'geometry', 28992, 'POLYGON', 'XY')
--
SELECT CreateSpatialIndex('standplaats', 'geometry')
--
INSERT INTO standplaats
(id, naam_openbare_ruimte, huisnummer, postcode, woonplaats, gemeente, openbare_ruimte, geometry)
SELECT id, naam_openbare_ruimte, huisnummer, postcode, woonplaats, gemeente, type_openbare_ruimte, geometry
FROM view_standplaats
