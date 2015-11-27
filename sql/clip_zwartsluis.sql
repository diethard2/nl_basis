DELETE from verblijfsobject
WHERE MbrDisjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from pand
WHERE MbrDisjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from ligplaats
WHERE MbrDisjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from standplaats
WHERE MbrDisjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from verblijfsobject
WHERE Disjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from pand
WHERE Disjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from ligplaats
WHERE Disjoint(geometry, (select geometry from woonplaats where id='2201'))
--
DELETE from standplaats
WHERE Disjoint(geometry, (select geometry from woonplaats where id='2201'))
--
select InvalidateLayerStatistics('ligplaats')
--
select InvalidateLayerStatistics('standplaats')
--
select InvalidateLayerStatistics('pand')
--
select InvalidateLayerStatistics('verblijfsobject')
--
select InvalidateLayerStatistics('verblijfsobject', 'geometry')
--
select InvalidateLayerStatistics('ligplaats', 'geometry')
--
select InvalidateLayerStatistics('standplaats', 'geometry')
--
select InvalidateLayerStatistics('pand', 'geometry')
--
select UpdateLayerStatistics('ligplaats')
--
select UpdateLayerStatistics('standplaats')
--
select UpdateLayerStatistics('pand')
--
select UpdateLayerStatistics('verblijfsobject')
--
vacuum
