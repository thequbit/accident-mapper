import json

from mkjson import readdata

accidenttypes= [
    "COLLISION WITH PEDESTRIAN",
    "RAN OFF ROAD ONLY",
    "COLLISION WITH GUIDE RAIL",
    "COLLISION WITH OTHER FIXED OBJECT",
    "COLLISION WITH MOTOR VEHICLE",
    "COLL. W/EARTH ELE./ROCK CUT/DITCH",
    "COLLISION WITH GUIDERAIL - END",
    "COLLISION WITH SNOW EMBANKMENT",
    "COLL. W/LIGHT SUPPORT/UTILITY POLE",
    "OVERTURNED",
    "COLLISION WITH TREE",
    "COLLISION WITH OTHER",
    "COLLISION WITH OTHER BARRIER",
    "COLLISION WITH CURBING",
    "COLLISION WITH MEDIAN/BARRIER",
    "COLLISION WITH BICYCLIST",
    "COLLISION WITH BUILDING/WALL",
    "COLLISION WITH SIGN POST",
    "COLLISION WITH FENCE",
    "COLLISION WITH DEER",
    "OTHER NON-COLLISION",
    "COLLISION WITH OTHER PEDESTRIAN",
    "COLLISION WITH FIRE HYDRANT",
    "COLLISION WITH BRIDGE STRUCTURE",
    "COLLISION WITH CRASH CUSHION",
    "COLLISION WITH CULVERT/HEADWALL",
    "FIRE/EXPLOSION",
    "COLLISION WITH ANIMAL",
    "COLLISION WITH IN-LINE SKATER",
    "SUBMERSION",
    "COLLISION WITH MEDIAN/BARRIER - END"
]

years = ['2010','2011','2012','2013']

towns = [
    "Ontario",
    "Rochester",
    "Riga",
    "Irondequoit",
    "Hamlin", 
    "Spencerport", 
    "Mendon", 
    "Macedon", 
    "Penfield",
    "Churchville", 
    "Walworth", 
    "Brockport", 
    "Perinton", 
    "Honeoye Falls", 
    "Chili", 
    "East Rochester", 
    "Brighton", 
    "Henrietta", 
    "Rush",
    "Clarkson",
    "Ogden", 
    "Sweden", 
    "Webster", 
    "Gates", 
    "Fairport",
    "Pittsford",
    "Parma", 
    "Scottsville",
    "Wheatland", 
    "Hilton", 
    "Greece", 
]

if __name__ == '__main__':

    # read in data as csv->json
    data = readdata('traffic.csv')

    # build framework for dicts
    counts = {}
    townstats = {}
    for year in years:
        counts[year] = {}
        townstats[year] = {}
        for town in towns:
            #counts[year][town] = {}
            townstats[year][town] = {}
            for accidenttype in accidenttypes:
                counts[year][accidenttype] = 0
                townstats[year][town][accidenttype] = 0

    # populate dicts
    for d in data:
       
        townstats[d['year']][d['municipality']][d['accidenttype']] += 1
        counts[d['year']][d['accidenttype']] += 1

    # write out data
    with open('townstats.json','w') as f:
        f.write(json.dumps(townstats))
    with open('counts.json','w') as f:
        f.write(json.dumps(counts))

