import json

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# add mongo url to flask config, so that flask_pymongo can use it to make connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_database'
mongo = PyMongo(app)

from server import routes