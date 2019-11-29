import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

from server import routes