from server import app
from flask import jsonify

@app.route('/random', methods=['GET'])
def get_random_command():
    res = {'name':'ls', 'description':'list files'}
    return jsonify(res)