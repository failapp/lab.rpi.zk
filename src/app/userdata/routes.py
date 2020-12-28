from . import userdata
from . import service
from app import jsonify, request
from datetime import datetime
import json


@userdata.route('/api/v1/zk/users', methods=['GET'])
def fetch_users():
    userList = service.fetch_device_users()
    if not userList is None:
            return jsonify(userList), 200
    else:
        return jsonify({}), 204
    

@userdata.route('/api/v1/zk/users/<userId>', methods=['GET'])
def fetch_user(userId):
    user = service.fetch_device_user(userId)
    if not user is None:
            return user, 200
    else:
        return jsonify({}), 204
    

@userdata.route('/api/v1/zk/users', methods=['POST'])
def store_user():

    if (request.data):
        payload = request.get_json()
        user = service.store_device_user(payload)
        if not user is None:
            return jsonify(user), 200
        else:
            return jsonify({}), 204

    else:
        return jsonify({}), 204




@userdata.route('/api/v1/zk/users', methods=['DELETE'])
def delete_user():

    if (request.data):
        payload = request.get_json()
        delete = service.delete_device_user(payload)
        if delete == True:
            return jsonify({}), 200
        else:
            return jsonify({}), 204

    else:
        return jsonify({}), 204


@userdata.route('/api/v1/zk/users/fingerprint/<userId>', methods=['POST'])
def save_fingerprint_template():
    #service.save_fingerprint_template(payload)
    return jsonify({}), 204
