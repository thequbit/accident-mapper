import json

from pymongo import MongoClient

from mkjson import readdata

def popdb(filename):

    # read in accident data from disk
    data = readdata(filename)

    # setup mongodb connection
    uri = 'mongodb://localhost:27017/'
    dbclient = MongoClient(uri)
    db = dbclient['monroecountyaccidentdata']
    accidents = db['accidents']

    accidents.remove()

    print "Loading {0} accidents into database ...".format(len(data))

    # load accident data into the collection
    for d in data:
        accidents.insert(d)

    count = accidents.count()

    print "Successfully loaded {0} accidents into the database.".format(count)

if __name__ == '__main__':

    popdb('traffic.csv')
