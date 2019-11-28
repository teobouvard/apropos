from server import app
from server import mongo
from flask import jsonify

@app.route('/', methods=['GET'])
def base():
    res = 'API endpoint'
    return jsonify(res)

@app.route('/random', methods=['GET'])
def get_random_command():
    res = mongo.db.manpages.aggregate([{ '$sample': { 'size': 1 } }])
    document = list(res)[0]
    del document['_id']
    return jsonify(document)