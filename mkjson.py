
import csv
import utm
import json

QUERYID = 0
CASE_NUM = 1
CASE_YEAR = 2
REGN_CNTY_CDE = 3
COMP_MUNI = 4
MUNITYPE = 5
REF_MRKR = 6
ATINTERSECTION_IND = 7
COMPX = 8
COMPY = 9
ACC_DATE = 10
ACC_TIME = 11
DMV_ACCD_CLSF = 12
NUM_OF_INJURIES = 13
NUM_OF_FATALITIES = 14
NUM_OF_VEH = 15
ACCD_TYP = 16
COLLISION_TYP = 17
TRAF_CNTL = 18
LIGHT_COND = 19
WEATHER = 20
ROAD_SURF_COND = 21

def readdata(csvfile):

    f = open(csvfile,'r')
    reader = csv.reader(f)

    events = []
    count = 0
    places = []
    for row in reader:
        #print row
        #raise Exception('debug')
        if count == 0:
            count += 1  
            continue
        
        #print "{0}: {1}".format(count,row)

        #cells = line.split(',')
        cells = row
        event = {}
        #event['queryid'] = cells[QUERYID]
        #event['casenum'] = cells[CASE_NUM]
        #event['year'] = cells[CASE_YEAR]
        #event['region'] = cells[REGN_CNTY_CDE]
        #event['municipality'] = cells[REGN_CNTY_CDE]
        #event['municipalitytype'] = cells[MUNITYPE]
        #event['markerreference'] = cells[REF_MRKR]
        #event['atintersection'] = cells[ATINTERSECTION_IND]
        #event['compx'] = cells[COMPX]
        #event['compy'] = cells[COMPY]
        event['date'] = cells[ACC_DATE]
        event['time'] = cells[ACC_TIME]
        event['class'] = cells[DMV_ACCD_CLSF]
        event['injuries'] = cells[NUM_OF_INJURIES]
        event['fatalities'] = cells[NUM_OF_FATALITIES]
        event['vehiclecount'] = cells[NUM_OF_VEH]
        event['accidenttype'] = cells[ACCD_TYP]
        event['collisiontype'] = cells[COLLISION_TYP]
        event['trafficcontrol'] = cells[TRAF_CNTL]
        #event['lightcondition'] = cells[LIGHT_COND]
        #event['weather'] = cells[WEATHER]
        #event['roadconditions'] = cells[ROAD_SURF_COND]
        event['municipality'] = cells[COMP_MUNI]

        if cells[COMP_MUNI] not in places:
            places.append(cells[COMP_MUNI])

        #easting = int(event['compx'])
        #northing = int(event['compy'])
        easting = int(cells[COMPX])
        northing = int(cells[COMPY])
        (lat,lng) = utm.to_latlon(easting,northing,18,'T')

        event['lat'] = lat
        event['lng'] = lng

        events.append(event)

        count += 1
        if ( count % 100 == 0 ):
            print "{0} ...".format(count)

        #print "{0}: {1}".format(count,row)

    f.close()

    with open('events.json','w') as outfile:
        outfile.write(json.dumps(events))

    with open('places.json','w') as outfile:
        outfile.write(json.dumps(places))

    print 'done.'

if __name__ == '__main__':

    readdata('traffic.csv')
