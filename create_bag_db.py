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
from pyspatialite import dbapi2
import bag
##import my_resources

def get_sql_statements(sql_file):
    '''get_sql_statements(sql_file) --> list of sql statements

    Reads sql statements from a file where these can be written over several
    lines for good readability. A line is added between two statements using
    "--". Unneccesary whitespace is removed.

    >>> import my_resources
    >>> sql_test_file = my_resources.sql_test_file
    >>> sql_test_file
    'test/test.sql'
    >>> a_file = my_resources.my_resource_file(sql_test_file)
    >>> statements = get_sql_statements(a_file)
    >>> statements
    ['CREATE TABLE person (name TEXT)', "INSERT INTO person VALUES ('Peter')"]
    '''

    # next insert the sql_statements to create joins and special indexes
    sql_statements = []
    sql_statement = ""
    for line in open(sql_file):
        if line.startswith("--"):
            sql_statement = ' '.join(sql_statement.split())
            sql_statements.append(sql_statement)
            sql_statement = ""
            continue
        sql_statement += line
    sql_statement = ' '.join(sql_statement.split())
    sql_statements.append(sql_statement)
    return sql_statements

def create_db(new_file):
    '''create_db(new_file) --> new empty spatialite db

    Creates a new spatialite database with provided filename.

    >>> import my_resources
    >>> my_test_db = my_resources.test_db
    >>> my_test_db
    'test/test.sqlite'
    >>> test_db = my_resources.my_resource_file(my_test_db)
    >>> create_db(test_db)
    '''
    conn = dbapi2.connect(new_file)
    cur = conn.cursor()
    sql_statements = {'SELECT InitSpatialMetadata()'}
    for sql_statement in sql_statements:
        rs = cur.execute(sql_statement)
    rs = cur.execute(sql_statement)
    conn.commit()
    rs.close()
    conn.close()

def execute_sql(spatialite_db, sql_statements):
    '''Opens a connection to spatialite database and
    runs given sql_statements'''
    conn = dbapi2.connect(spatialite_db)
    cur = conn.cursor()
    for sql_statement in sql_statements:
        rs = cur.execute(sql_statement)
    conn.commit()
    rs.close()
    conn.close()
 
def create_datamodel(spatialite_db):
    '''creates a new BAG datamodel in given spatialite_db
    >>> import my_resources
    >>> my_test_db = my_resources.test_db
    >>> my_test_db
    'test/test.sqlite'
    >>> test_db = my_resources.my_resource_file(my_test_db)
    >>> create_datamodel(test_db)
    '''
    sql_file = 'sql/gemeente.sql'
    sql_statements = bag.sql_creation_statements()
    sql_statements.extend(get_sql_statements(sql_file))
    execute_sql(spatialite_db, sql_statements)

def create_views(spatialite_db):
    '''create views to provide better access to information'''
    sql_file = 'sql/bag_views.sql'
    sql_statements = get_sql_statements(sql_file)
    execute_sql(spatialite_db, sql_statements)
    
def create_styles(spatialite_db):
    '''create styles used in qgis for tables'''
    sql_file = 'sql/bag_stijlen.sql'
    sql_statements = get_sql_statements(sql_file)
    execute_sql(spatialite_db, sql_statements)

def flatten_tables(spatialite_db):
    '''create flat tables from view for faster performance'''
    sql_file = 'sql/bag_flat_tables.sql'
    sql_statements = get_sql_statements(sql_file)
    execute_sql(spatialite_db, sql_statements)

def drop_tables(spatialite_db):
    '''remove tables that are not neccesary anymore'''
    sql_file = 'sql/bag_remove_tables.sql'
    sql_statements = get_sql_statements(sql_file)
    execute_sql(spatialite_db, sql_statements)

def clip_zwartsluis(spatialite_db):
    '''clip geodata from zwartsluis only'''
    sql_file = 'sql/clip_zwartsluis.sql'
    sql_statements = get_sql_statements(sql_file)
    execute_sql(spatialite_db, sql_statements)

if __name__ == "__main__":
    pass
##    import doctest
##    doctest.testmod()
