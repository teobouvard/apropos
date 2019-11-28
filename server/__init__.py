import json

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_database'

mongo = PyMongo(app)

from server import routes