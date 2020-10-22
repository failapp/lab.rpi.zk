from os import environ

class Config:
    SCHEDULER_API_ENABLED = True
    APIREST_ENDPOINT = environ.get('APIREST_ENDPOINT', 'http://localhost:9000')
    BROKER_ENDPOINT = 'amq.architeq.cl:5672'
    BROKER_USER = 'zkservice'
    BROKER_PWD = '12345'
    IP_ADDR_DEVICE = environ.get('IP_ADDR_DEVICE_ZK', '192.168.20.75')
    TCP_PORT_DEVICE = 4370
    COMPANY_NAME = 'Sandvik Chile S.A'
    COMPANY_RUT = '94.879.000-9'
    COMPANY_ADDRESS = 'Av. Eduardo Frei Montalva #9990'
    COMPANY_LOCALITY = 'Quilicura, Santiago'
    PRINTER_USB_VENDOR_ID = 0x0525
    PRINTER_USB_PRODUCT_ID = 0xa700
    