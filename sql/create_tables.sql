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
DROP TABLE if exists gem_wpl_rel
--
CREATE TABLE gem_wpl_rel
    (gemeentecode, TEXT NOT NULL,
     woonplaats_id, INTEGER NOT NULL)
--
CREATE INDEX i_gem_wpl_rel ON gem_wpl_rel (gemeentecode, woonplaats_id)

    


