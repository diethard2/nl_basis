import create_bag_db, fill_bag_db
import time

new_db = "C:/data/bag/test.sqlite"

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

def full_run():
    create_db()
    time.sleep(5) # give spatialite time to finish properly
    create_datamodel()
    fill_db()
