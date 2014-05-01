from flask import Flask
from flask import render_template
from flask import request

import json
import datetime

from pymongo import MongoClient

# flask application
app = Flask(__name__, static_folder='web/static', static_url_path='')
app.template_folder = "web"
app.debug = True

# mongodb connection
uri = 'mongodb://localhost:27017/'
dbclient = MongoClient(uri)
db = dbclient['monroecountyaccidentdata']
accidents = db['accidents']

allowed = [
    #'queryid',
    #'casenum',
    'year',
    #'region',
    #'municipalitytype',
    #'markerreference',
    #'atintersection',
    #'compx',
    #'compy',
    #'date',
    #'time',
    #'class',
    'injuries',
    'fatalities',
    'vehiclecount',
    'accidenttype',
    'collisiontype',
    'trafficcontrol',
    'lightcondition',
    'weather',
    'roadconditions',
    'municipality',
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/count.json')
def count():
    return json.dumps({'accidentcount': accidents.count()})

@app.route('/getall.json')
def getall():
    docs = accidents.find()
    results = []
    for d in docs:
        d['_id'] = str(d['_id'])
        results.append(d)
    return json.dumps({'accidents': results})

@app.route('/getone.json')
def getone():
    doc = accidents.find_one()
    doc['_id'] = str(doc['_id'])
    return json.dumps(doc)

@app.route('/getfields.json')
def getfields():
    results = {}
    for a in allowed:
        results[a] = accidents.distinct(a)
    return json.dumps(results)

@app.route('/query.json')
def query():

    #print request.args

    try:
        q = {}
        for key,val in request.args.iteritems():
           if key in allowed: 
               q[key] = val

        if len(q) != 0: 
            docs = accidents.find(q)
            results = []
            for doc in docs:
                doc['_id'] = str(doc['_id'])
                results.append(doc)
            success = True
            error = ''
        else:
            results = []
            success = False
            error = 'At least one field must be specified.'
    except Exception, e:
        results = []
        success = False
        error = str(e)

    return json.dumps({'query': q, 'success': success, 'error': error, 'results': results})

if __name__ == '__main__':

    print "Traffic Incident Visualization Web App Starting ..."

    host = '0.0.0.0'
    port = 8005

    app.run(host=host, port=port)
