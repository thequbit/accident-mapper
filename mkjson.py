
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

    count = 0
    accidents = []
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
        event['queryid'] = cells[QUERYID].strip()
        event['casenum'] = cells[CASE_NUM].strip()
        event['year'] = cells[CASE_YEAR].strip()
        event['region'] = cells[REGN_CNTY_CDE].strip()
        event['municipality'] = cells[REGN_CNTY_CDE].strip()
        event['municipalitytype'] = cells[MUNITYPE].strip()
        event['markerreference'] = cells[REF_MRKR].strip()
        event['atintersection'] = cells[ATINTERSECTION_IND].strip()
        event['compx'] = cells[COMPX].strip()
        event['compy'] = cells[COMPY].strip()
        event['date'] = cells[ACC_DATE].strip()
        event['time'] = cells[ACC_TIME].strip()
        event['class'] = cells[DMV_ACCD_CLSF].strip()
        event['injuries'] = cells[NUM_OF_INJURIES].strip()
        event['fatalities'] = cells[NUM_OF_FATALITIES].strip()
        event['vehiclecount'] = cells[NUM_OF_VEH].strip()
        event['accidenttype'] = cells[ACCD_TYP].strip()
        event['collisiontype'] = cells[COLLISION_TYP].strip()
        event['trafficcontrol'] = cells[TRAF_CNTL].strip()
        event['lightcondition'] = cells[LIGHT_COND].strip()
        event['weather'] = cells[WEATHER].strip()
        event['roadconditions'] = cells[ROAD_SURF_COND].strip()
        event['municipality'] = cells[COMP_MUNI].strip()

        #easting = int(event['compx'])
        #northing = int(event['compy'])
        easting = int(cells[COMPX])
        northing = int(cells[COMPY])
        (lat,lng) = utm.to_latlon(easting,northing,18,'T')

        event['lat'] = lat
        event['lng'] = lng

        accidents.append(event)

        count += 1
        if ( count % 100 == 0 ):
            print "{0} ...".format(count)

        #print "{0}: {1}".format(count,row)

    f.close()
    
    #for key in accidents.keys():
    #    with open('./web/static/accidents-{0}.json'.format(key.replace(' ','')),'w') as outfile:
    #        outfile.write(json.dumps(accidents[key]))
    #
    #with open('./web/static/places.json','w') as outfile:
    #    outfile.write(json.dumps(places))
    #
    #with open('./web/static/years.json','w') as outfile:
    #    outfile.write(json.dumps(years))

    print 'done.'

    return accidents;

if __name__ == '__main__':

    readdata('traffic.csv')
