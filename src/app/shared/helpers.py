import json
from datetime import datetime

def obj_to_dict(obj):
    return obj.__dict__


def obj_to_json(obj):
    s = json.dumps(obj.__dict__, default = obj_to_dict)
    return json.loads(s)


def get_weekday(date):
    days=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    dayNumber=date.weekday()
    return days[dayNumber]