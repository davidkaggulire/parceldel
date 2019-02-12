"""__init__.py"""

from flask import Flask
from config import app_config
from api.v1.views.parcel_views import order


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(order)
    return app
