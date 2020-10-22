from app import jsonify
from zk import ZK, const
from app.config import Config
from datetime import datetime
import json
import time

conf = Config()

def fetch_macaddr_device():
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:
            return conn.get_mac()
        else:
            return None

    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None


def fetch_time_device():
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:
            return conn.get_time()
        else:
            return None

    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None


def send_time_device():
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:
            newtime = datetime.today()
            conn.set_time(newtime)
            time.sleep(1)
            return conn.get_time()
        else:
            return None

    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None


def set_ipaddr_config(ipAddr):
    conf.IP_ADDR_DEVICE = ipAddr
    return conf.IP_ADDR_DEVICE

def get_ipaddr_config():
    return conf.IP_ADDR_DEVICE
