from . import eventdata
from . import service
from app import jsonify, request
import json


@eventdata.route('/api/v1/zk/eventlogs', methods=['GET'])
def fetch_eventlogs():
    return jsonify({'response': 'eventlogs device ..'})


@eventdata.route('/api/v1/zk/canteen/printer/test', methods=['GET'])
def test_printer_ticket():
    service.print_test_data()
    return jsonify({'printer': 'ticket ok'}), 200


@eventdata.route('/api/v1/zk/canteen/printer', methods=['POST'])
def printer_ticket():
    if(request.data):
        payload = request.get_json()
        print("payload ->", payload)
        service.print_ticket_canteen(payload)
    
    return jsonify({'printer': 'ticket ok'}), 200
