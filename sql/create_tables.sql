DROP TABLE if exists gemeente
--
CREATE TABLE gemeente 
    (gemeentecode TEXT NOT NULL,
     naam TEXT NOT NULL)
--
DROP TABLE if exists woonplaats
--
CREATE TABLE woonplaats
    (id INTEGER NOT NULL PRIMARY KEY,
     naam TEXT NOT NULL)
--
SELECT AddGeometryColumn('woonplaats', 'geometry', 28992, 'MULTIPOLYGON', 'XY')
--
SELECT CreateSpatialIndex('woonplaats', 'geometry')
--
DROP TABLE if exists pand
--
CREATE TABLE pand
    (id TEXT NOT NULL PRIMARY KEY,
     bouwjaar TEXT NOT NULL,
     status TEXT NOT NULL)
--
SELECT AddGeometryColumn('pand', 'geometry', 28992, 'POLYGON', 'XY')
--
SELECT CreateSpatialIndex('pand', 'geometry')
--
DROP TABLE if exists gem_wpl_rel
--
CREATE TABLE gem_wpl_rel
    (gemeentecode, TEXT NOT NULL,
     woonplaats_id, INTEGER NOT NULL)
--
CREATE INDEX i_gem_wpl_rel ON gem_wpl_rel (gemeentecode, woonplaats_id)

    


