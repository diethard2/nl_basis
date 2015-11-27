DROP INDEX IF EXISTS idx_bag_verblijfsobject_id_pand
--
CREATE INDEX idx_bag_verblijfsobject_id_pand
ON bag_verblijfsobject (id_pand)
--
DROP VIEW if exists view_woonplaats
--
CREATE VIEW view_woonplaats AS
SELECT wg.id_woonplaats AS id,
    w.naam AS naam,
    g.naam AS gemeentenaam,
    w.rowid as rowid,
    w.geometry AS geometry
FROM woonplaats_gemeente AS wg
LEFT JOIN bag_woonplaats AS w ON wg.id_woonplaats = w.id
LEFT JOIN gemeente AS g ON wg.id_gemeente = g.gemeentecode
--
INSERT OR IGNORE INTO views_geometry_columns
    (view_name, view_geometry, view_rowid, f_table_name, f_geometry_column, read_only)
  VALUES ('view_woonplaats', 'geometry', 'rowid', 'bag_woonplaats', 'geometry', 1)
---
DELETE
FROM gemeente 
WHERE naam NOT IN 
(select distinct(gemeentenaam) from view_woonplaats);
--
DROP VIEW if exists view_adres
--
CREATE VIEW view_adres AS
SELECT n.id AS id,
    o.naam AS naam_openbare_ruimte,
    n.huisnummer AS huisnummer,
    n.huisletter AS huisletter,
    n.huisnummertoevoeging AS huisnummertoevoeging,
    n.postcode AS postcode,
    o.id_woonplaats AS id_woonplaats      
FROM nummeraanduiding AS n
LEFT JOIN openbare_ruimte AS o ON n.id_openbare_ruimte = o.id
--
DROP VIEW if exists view_verblijfsobject
--
CREATE VIEW view_verblijfsobject AS
SELECT v.id AS id,
       a.naam_openbare_ruimte as straat,
       a.huisnummer as huisnummer,
       a.huisletter as huisletter,
       a.huisnummertoevoeging as huisnummertoevoeging,
       a.postcode as postcode,
       w.naam as woonplaats,
       w.gemeentenaam as gemeente,
       v.gebruiksdoel as gebruiksdoel,
       v.oppervlakte as oppervlakte,
       v.id_pand as id_pand,
       v.rowid as rowid,
       v.geometry as geometry
FROM bag_verblijfsobject AS v
LEFT JOIN view_adres AS a ON v.id_hoofdadres = a.id
LEFT JOIN view_woonplaats AS w on a.id_woonplaats = w.id
--
INSERT OR IGNORE INTO views_geometry_columns
    (view_name, view_geometry, view_rowid, f_table_name, f_geometry_column, read_only)
 VALUES ('view_verblijfsobject', 'geometry', 'rowid', 'bag_verblijfsobject', 'geometry', 1)
--
DROP VIEW if exists view_ligplaats
--
CREATE VIEW view_ligplaats AS
SELECT l.id AS id,
       a.naam_openbare_ruimte as straat,
       a.huisnummer as huisnummer,
       a.huisletter as huisletter,
       a.huisnummertoevoeging as huisnummertoevoeging,
       a.postcode as postcode,
       w.naam as woonplaats,
       w.gemeentenaam as gemeente,
       l.rowid as rowid,
       l.geometry as geometry
FROM bag_ligplaats as l
LEFT JOIN view_adres AS a ON l.id_hoofdadres = a.id
LEFT JOIN view_woonplaats AS w on a.id_woonplaats = w.id
--
INSERT OR IGNORE INTO views_geometry_columns
    (view_name, view_geometry, view_rowid, f_table_name, f_geometry_column, read_only)
VALUES ('view_ligplaats', 'geometry', 'rowid', 'bag_ligplaats', 'geometry', 1)
--
DROP VIEW if exists view_standplaats
--
CREATE VIEW view_standplaats AS
SELECT s.id AS id,
       a.naam_openbare_ruimte as straat,
       a.huisnummer as huisnummer,
       a.huisletter as huisletter,
       a.huisnummertoevoeging as huisnummertoevoeging,
       a.postcode as postcode,
       w.naam as woonplaats,
       w.gemeentenaam as gemeente,
       s.rowid as rowid,
       s.geometry as geometry
FROM bag_standplaats as s
LEFT JOIN view_adres AS a ON s.id_hoofdadres = a.id
LEFT JOIN view_woonplaats AS w on a.id_woonplaats = w.id
--
INSERT OR IGNORE INTO views_geometry_columns
    (view_name, view_geometry, view_rowid, f_table_name, f_geometry_column, read_only)
VALUES ('view_standplaats', 'geometry', 'rowid', 'bag_standplaats', 'geometry', 1)

