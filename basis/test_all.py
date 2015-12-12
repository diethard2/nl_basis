"""
/***************************************************************************
 basic test functions that resembles all the steps to include as configurable
 algoritmes in processing.
 -------------------
 begin                : 2015-07-20
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
import create_bag_db, fill_bag_db
import time

new_db = "C:/data/bag/bag.sqlite"

def create_db():
    time_start = time.clock()
    global new_db
    create_bag_db.create_db(new_db)
    time_end = time.clock()
    print "create_db seconds used: " + str(time_end - time_start)

def create_datamodel():
    time_start = time.clock()
    global new_db
    create_bag_db.create_datamodel(new_db)
    time_end = time.clock()
    print "create_datamodel seconds used: " + str(time_end - time_start)

def fill_db():
    time_start = time.clock()
    global new_db
    input_dir = "C:/data/bag/input"
    print "new_db ", new_db
    filler = fill_bag_db.FillDB(new_db, input_dir)
    filler.run()
    time_end = time.clock()
    print "fill_db seconds used: " + str(time_end - time_start)

def create_views():
    time_start = time.clock()
    global new_db
    create_bag_db.create_views(new_db)
    time_end = time.clock()
    print "create_views seconds used: " + str(time_end - time_start)

def flatten_tables():
    time_start = time.clock()
    global new_db
    create_bag_db.flatten_tables(new_db)
    time_end = time.clock()
    print "flatten_tables seconds used: " + str(time_end - time_start)

def drop_tables():
    time_start = time.clock()
    global new_db
    create_bag_db.drop_tables(new_db)
    time_end = time.clock()
    print "drop_tables seconds used: " + str(time_end - time_start)

def clip_zwartsluis():
    time_start = time.clock()
    global new_db
    create_bag_db.clip_zwartsluis(new_db)
    time_end = time.clock()
    print "clip zwartsluis seconds used: " + str(time_end - time_start)

def create_styles():
    time_start = time.clock()
    global new_db
    create_bag_db.create_styles(new_db)
    time_end = time.clock()
    print "create_styles seconds used: " + str(time_end - time_start)

def full_run():
    create_db()
    time.sleep(5) # give spatialite time to finish properly
    create_datamodel()
    fill_db()
    create_views()
    flatten_tables()
    drop_tables()
    create_styles()
