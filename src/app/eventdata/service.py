from zk import ZK, const
from zk.user import User
from app.config import Config
from app.shared.helpers import obj_to_json, obj_to_dict
from escpos import *
from datetime import datetime
import requests
import json
import time

conf = Config()

def polling_data_device():

    conn = None
    try:
        
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()

        if conn:
            newtime = datetime.today()
            conn.set_time(newtime)
            time.sleep(1)
            
            macAddr = str(conn.get_mac()).upper()

            print("polling eventdata process .. " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

            for data in conn.live_capture():
                try:
                    if data is None:
                        # implement here timeout logic ..
                        pass
                    else:
                        print("data -> ", data)
                        send_data_apirest(data, macAddr)
                except:
                    print('error en captura [conn.live_capture] ..')
                    continue

    except Exception as e:
        print ("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()



def print_test_data():
    try:
        print('test printer canteen ..')

        dni = "15.200.300-4"
        firstName = "Esteban"
        lastName = "Dido Matta"
            
        p = printer.Usb(conf.PRINTER_USB_VENDOR_ID, conf.PRINTER_USB_PRODUCT_ID)
        p.set(font='a', text_type='normal', density=1)
        p.text( conf.COMPANY_NAME + "\n")
        p.text( conf.COMPANY_RUT + "\n")
        p.text( conf.COMPANY_ADDRESS + "\n")
        p.text( conf.COMPANY_LOCALITY + "\n")
        p.text(" \n")

        p.set(font='a', text_type='normal', width=1, height=1, density=4)
        p.text("Servicio Casino\n")
        #p.text( get_weekday(att.timestamp) + " " + att.timestamp.strftime("%d/%m/%Y %H:%M:%S")+ "\n")
        p.text( datetime.today().strftime("%d/%m/%Y %H:%M:%S") + "\n" )
        p.text(" \n")

        p.set(font='b', text_type='normal', width=2, height=2, density=1)
        p.text(dni + "\n")
        p.text(firstName  + "\n")
        p.text(lastName + "\n")
        p.text(" \n")

        p.set(font='a', text_type='normal', width=1, height=1, density=1)
        p.text("Cheksum: #20f7889914s \n")
        p.set(font='b', text_type='normal', width=1, height=1, density=1)
        p.text("https://www.architeq.cl\n")
        p.text(" \n")
    
        p.cut()

    except:
        print('error in test printer ticket canteen ..')



def print_ticket_canteen(payload):
    try:
        print('printer ticket canteen ..')

        dni = payload['dni']
        firstName = payload['firstName']
        lastName = payload['lastName']
        eventDateTime = payload['eventDateTime']
        serviceName = payload['serviceName']
        checkumTicket = payload['checksumTicket']
            
        p = printer.Usb(conf.PRINTER_USB_VENDOR_ID, conf.PRINTER_USB_PRODUCT_ID)
        p.set(font='a', text_type='normal', density=1)
        p.text( conf.COMPANY_NAME + "\n")
        p.text( conf.COMPANY_RUT + "\n")
        p.text( conf.COMPANY_ADDRESS + "\n")
        p.text( conf.COMPANY_LOCALITY + "\n")
        p.text(" \n")

        p.set(font='a', text_type='normal', width=1, height=1, density=4)
        p.text("Servicio Casino\n")
        p.text(serviceName + "\n")
        #p.text( get_weekday(att.timestamp) + " " + att.timestamp.strftime("%d/%m/%Y %H:%M:%S")+ "\n")
        #p.text( datetime.today().strftime("%d/%m/%Y %H:%M:%S") + "\n" )
        p.text(eventDateTime + "\n")
        p.text(" \n")

        p.set(font='b', text_type='normal', width=2, height=2, density=1)
        p.text(dni + "\n")
        p.text(firstName  + "\n")
        p.text(lastName + "\n")
        p.text(" \n")

        p.set(font='a', text_type='normal', width=1, height=1, density=1)
        #p.text("Cheksum: #20f7889914s \n")
        p.text("Cheksum: " + checkumTicket + "\n")
        p.set(font='b', text_type='normal', width=1, height=1, density=1)
        p.text("https://www.architeq.cl\n")
        p.text(" \n")

        p.cut()

    except:
        print('error in test printer ticket canteen ..')




def send_data_apirest(att, macAddr):
    try:
        #print("[x] -> user_id: " + str(att.user_id) + ", timestamp: " + str(att.timestamp) + ", verification type: " + str(att.status) + ", verification state: " + str(att.punch))
        event_datetime = datetime.strftime(att.timestamp,'%Y-%m-%d %H:%M:%S')
        checksum = ''

        payload = {'dateTime': event_datetime, 'userId': att.user_id, 'verType': att.status, 'verStatus': att.punch, 'macDevice': macAddr, 'checksum': checksum }
        endpoint = conf.APIREST_ENDPOINT + '/api/v1/rpi/eventdata'
        print('endpoint apirest eventdata:', endpoint)
        headers = {'content-type': 'application/json'}
        response = requests.post(endpoint, data=json.dumps(payload).encode('utf8'), headers=headers)
        print('send eventdata to apirest.. response status code: ', response.status_code)
        if response.status_code == 200:
            return True

    except:
        print("error in send eventdata to apirest.. ")
    return False