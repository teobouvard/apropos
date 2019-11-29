from flask import jsonify
from pymongo import MongoClient
import os

from server import app

client = MongoClient('mongodb', 27017)
db = client.test_database

@app.route('/', methods=['GET'])
def base():
    res = 'API endpoint'
    return jsonify(res)

@app.route('/random', methods=['GET'])
def get_random_command():
    res = db.manpages.aggregate([{ '$sample': { 'size': 1 } }])
    document = list(res)[0]
    del document['_id']
    return jsonify(document)
