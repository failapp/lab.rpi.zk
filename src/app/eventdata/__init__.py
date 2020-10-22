from flask import Blueprint

eventdata = Blueprint('eventdata', __name__)

from . import routes
