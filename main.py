import sys
sys.path.insert(0, 'libs')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

from google.appengine.ext.webapp.util import run_wsgi_app
run_wsgi_app(app)