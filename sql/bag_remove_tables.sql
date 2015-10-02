DELETE FROM views_geometry_columns
--
DROP VIEW if exists view_adres
--
DROP VIEW if exists view_woonplaats
--
DROP VIEW if exists view_verblijfsobject
--
DROP VIEW if exists view_ligplaats
--
DROP VIEW if exists view_standplaats
--
SELECT DisableSpatialIndex('bag_woonplaats', 'geometry');
--
SELECT DisableSpatialIndex('bag_standplaats', 'geometry');
--
SELECT DisableSpatialIndex('bag_ligplaats', 'geometry');
--
SELECT DisableSpatialIndex('bag_verblijfsobject', 'geometry');
--
DELETE FROM geometry_columns WHERE f_table_name='bag_ligplaats'
--
DELETE FROM geometry_columns WHERE f_table_name='bag_standplaats'
--
DELETE FROM geometry_columns WHERE f_table_name='bag_woonplaats'
--
DELETE FROM geometry_columns WHERE f_table_name='bag_verblijfsobject'
--
DROP TABLE if exists bag_woonplaats
--
DROP TABLE if exists openbare_ruimte
--
DROP TABLE if exists bag_verblijfsobject
--
DROP TABLE if exists bag_ligplaats
--
DROP TABLE if exists bag_standplaats
--
DROP TABLE if exists nummeraanduiding
--
DROP TABLE if exists woonplaats_gemeente
--
DROP TABLE if exists gemeente
--
DROP TABLE if exists idx_bag_ligplaats_geometry
--
DROP TABLE if exists idx_bag_ligplaats_geometry_node
--
DROP TABLE if exists idx_bag_ligplaats_geometry_parent
--
DROP TABLE if exists idx_bag_ligplaats_geometry_rowid
--
DROP TABLE if exists idx_bag_woonplaats_geometry
--
DROP TABLE if exists idx_bag_woonplaats_geometry_node
--
DROP TABLE if exists idx_bag_woonplaats_geometry_parent
--
DROP TABLE if exists idx_bag_woonplaats_geometry_rowid
--
DROP TABLE if exists idx_bag_standplaats_geometry
--
DROP TABLE if exists idx_bag_standplaats_geometry_node
--
DROP TABLE if exists idx_bag_standplaats_geometry_parent
--
DROP TABLE if exists idx_bag_standplaats_geometry_rowid
--
DROP TABLE if exists idx_bag_verblijfsobject_geometry
--
DROP TABLE if exists idx_bag_verblijfsobject_geometry_node
--
DROP TABLE if exists idx_bag_verblijfsobject_geometry_parent
--
DROP TABLE if exists idx_bag_verblijfsobject_geometry_rowid
--
DROP TABLE if exists idx_bag_pand_geometry
--
DROP TABLE if exists idx_bag_pand_geometry_node
--
DROP TABLE if exists idx_bag_pand_geometry_parent
--
DROP TABLE if exists idx_bag_pand_geometry_rowid
--
SELECT UpdateLayerStatistics('woonplaats')
--
SELECT UpdateLayerStatistics('verblijfsobject')
--
SELECT UpdateLayerStatistics('pand')
--
SELECT UpdateLayerStatistics('ligplaats')
--
SELECT UpdateLayerStatistics('standplaats')
--
VACUUM
