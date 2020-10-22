from flask import Flask, jsonify, request
from .userdata import userdata
from .eventdata import eventdata
from .device import device
from .config import Config
from .shared.scheduler import scheduler


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    scheduler.init_app(app)
    scheduler.start()


    app.register_blueprint(userdata)
    app.register_blueprint(eventdata)
    app.register_blueprint(device)

    return app
    