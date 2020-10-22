from flask import Blueprint

device = Blueprint('device', __name__)

from . import routes
