from flask import Flask

from app.views import index_views

BLUEPRINTS = [index_views]


def create_app():
    app = Flask(__name__)

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
