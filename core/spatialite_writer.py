'''
/***************************************************************************
Class Spatialite_writer requests to Spatialite database.
It can create a new Spatialite Database, read and execute an SQL file but also
handles a direct a given SQL statement.

begin                : 2016-01-17 
copyright            : (C) 2016 by Diethard Jansen
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

class Spatialite_writer:

    def __init__(self, a_spatialite_db):
        ''' Create a new instance to communicate with a spatialite db.
        '''
        self._db = a_spatialite_db
        self._sql_statements = []
        
    def execute(self):
        '''Creates a connection to database and executes sql_statements
        '''
        conn = dbapi2.connect(self._db)
        cur = conn.cursor()
        for sql_statement in self._sql_statements:
            cur.execute(sql_statement)
        conn.commit()
        conn.close()
        self._sql_statements = []

    def create(self):
        '''creates a new SpatiaLite database'''
        self._sql_statements = ['SELECT InitSpatialMetadata()']
        self.execute()

    def replace(self, search_string, replace_string):
        '''replace in sql_statements search_string with replace_string'''        
        sqls = self._sql_statements
        s_search = search_string
        s_replace = replace_string
        sqls = [sql.replace(s_search, s_replace) for sql in sqls]
        self._sql_statements = sqls

    def add_sql_statements(self, sql_statements):
        '''add a list of sql_statements to current list of sql statements'''
        self._sql_statements.extend(sql_statements)

    def read_sql_file(self, sql_file):
        '''Reads sql statements from a file and add to list of sql statements

        The file should contain valid sql-statements and and with ";"
        SQL-statements can be written over several lines for good
        readability.
        Lines with comment should start with "--".
        Unneccesary whitespace is removed before adding these to sql file.
        '''
        # next insert the sql_statements to create joins and special indexes
        sql_statements = []
        sql_statement = ""
        for line in open(sql_file):
            line = line.strip()
            if line.startswith("--"): #comment
                continue
            elif line.endswith(";"): #end of SQL statement
                line = line.rstrip(";")
                sql_statement += line
                sql_statement = ' '.join(sql_statement.split())
                sql_statements.append(sql_statement)
                sql_statement = ""
            else: #part of SQL statement
                # put back in space for proper splitting
                line += ' '  
                sql_statement += line
            
        self._sql_statements.extend(sql_statements)
