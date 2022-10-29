from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.create_tables import create_tables
from app.load_data import load_data

from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_tables(app, db)
    load_data(db)


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    register_extensions(app)
    return app


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
