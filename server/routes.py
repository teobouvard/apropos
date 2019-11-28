from server import app
from server import mongo
from flask import jsonify

@app.route('/random', methods=['GET'])
def get_random_command():
    res = mongo.db.manpages.aggregate([{ '$sample': { 'size': 1 } }])
    document = list(res)[0]
    del document['_id']
    return jsonify(document)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response