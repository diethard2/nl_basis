'''
/***************************************************************************
Create BAG DB
Creates a spatialite database and fills it from xml file holding all places to
stay (buildings) of the Netherlands. Use this temporary until we make a more
general class to import basis national geodata delivered in XML.

begin                : 2015-06-19 
copyright            : (C) 2015 by Diethard Jansen
email                : diethard.jansen at gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
'''
import spatialite_writer, bag
from os import path

def create_db(new_file):
    '''create_db(new_file) --> new empty spatialite db

    Creates a new spatialite database with provided filename.'''
    spatialite = spatialite_writer.Spatialite_writer(new_file)
    spatialite.create()

def create_datamodel(spatialite_db):
    '''creates a new BAG datamodel in given spatialite_db
    '''
    spatialite = spatialite_writer.Spatialite_writer(spatialite_db)
    sql_statements = bag.sql_creation_statements()
    spatialite.add_sql_statements(sql_statements)
    sql_file = path.join(path.dirname(__file__), '../sql/gemeente.sql')
    spatialite.read_sql_file(sql_file)
    spatialite.execute()

def create_views(spatialite_db):
    '''create views to provide better access to information'''
    sql_file = path.join(path.dirname(__file__), '../sql/bag_views.sql')
    spatialite = spatialite_writer.Spatialite_writer(spatialite_db)
    spatialite.read_sql_file(sql_file)
    spatialite.execute()
    
def create_styles(spatialite_db):
    '''create styles used in qgis for tables'''
    sql_file = path.join(path.dirname(__file__), '../sql/bag_stijlen.sql')
    spatialite = spatialite_writer.Spatialite_writer(spatialite_db)
    spatialite.read_sql_file(sql_file)
    # replace in sql statement the path to choosen input folder, otherwise styles wil not work!
    new_dir = path.dirname(spatialite_db)
    cur_dir = 'C:/data/bag'
    spatialite.replace(cur_dir, new_dir)
    spatialite.execute()

def flatten_tables(spatialite_db):
    '''create flat tables from view for faster performance'''
    sql_file = path.join(path.dirname(__file__), '../sql/bag_flat_tables.sql')
    spatialite = spatialite_writer.Spatialite_writer(spatialite_db)
    spatialite.read_sql_file(sql_file)
    spatialite.execute()

def drop_tables(spatialite_db):
    '''remove tables that are not neccesary anymore'''
    sql_file = path.join(path.dirname(__file__), '../sql/bag_remove_tables.sql')
    spatialite = spatialite_writer.Spatialite_writer(spatialite_db)
    spatialite.read_sql_file(sql_file)
    spatialite.execute()

def clip_zwartsluis(spatialite_db):
    '''clip geodata from zwartsluis only'''
    sql_file = path.join(path.dirname(__file__), '../sql/clip_zwartsluis.sql')
    spatialite = spatialite_writer.Spatialite_writer(spatialite_db)
    spatialite.read_sql_file(sql_file)
    spatialite.execute()
