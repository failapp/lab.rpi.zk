from app.shared.scheduler import scheduler
from app.config import Config
from . import service
from datetime import datetime
import time

conf = Config()

@scheduler.task('date', id='task_polling_device')
def task_eventdata():

    while True:
        try:
            print("task polling device .. " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
            service.polling_data_device()
            time.sleep(10)
        except:
            time.sleep(10)
            continue

    
# @scheduler.task('date', id='task_polling')
# def task_eventdata():
#     while True:
#         try:
#             print("polling eventdata process .. " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
#             time.sleep(10)
#         except:
#             print("error concurrent polling process ..")
#             continue

