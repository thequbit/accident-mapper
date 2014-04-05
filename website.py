from flask import Flask
from flask import render_template
from flask import request

import json
import datetime

app = Flask(__name__, static_folder='web/static', static_url_path='')
app.template_folder = "web"
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    print "Traffic Incident Visualization Web App Starting ..."

    host = '0.0.0.0'
    port = 8005

    app.run(host=host, port=port)
