from . import device
from app import jsonify, request
from . import service
from datetime import datetime
import json



@device.route('/api/v1/zk/device/status', methods=['GET'])
def get_device_status():
    return jsonify({'message': 'api zk: estado dispositivo -> ok ..'})


@device.route('/api/v1/zk/device/macaddr', methods=['GET'])
def get_device_macaddr():
    mac = service.fetch_macaddr_device()
    if mac:
        return jsonify({'macaddr-device': str(mac).upper()})
    else:
        return jsonify({'macaddr-device': 'api zk: not found ..'})


@device.route('/api/v1/zk/device/datetime', methods=['GET'])
def get_device_time():
    timezk = service.fetch_time_device()
    if timezk:
        return jsonify({'datetime-device': str(timezk)})
    else:
        return jsonify({'datetime-device': 'api zk: not found ..'})


@device.route('/api/v1/zk/device/datetime', methods=['POST'])
def set_device_time():
    if(request.data):
        payload = request.get_json()
        print("item ->", payload)
    timezk = service.send_time_device()
    if timezk:
        return jsonify({'datetime-device': str(timezk)})
    else:
        return jsonify({'datetime-device': 'api zk: not found ..'})


@device.route('/api/v1/zk/config/ipaddr', methods=['GET'])
def get_config_ipaddr():
    ipAddr = service.get_ipaddr_config()
    return jsonify({'ipAddress': str(ipAddr)})


@device.route('/api/v1/zk/config/ipaddr', methods=['POST'])
def set_config_ipaddr():
    ipAddr = service.get_ipaddr_config()
    if (request.data):
        payload = request.get_json()
        print("payload ->", payload)
        ipAddr = payload['ipAddress']
        ipAddr = service.set_ipaddr_config(ipAddr)
    
    return jsonify({'ipAddress': str(ipAddr)})





