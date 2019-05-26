import os

from flask import Flask, session
from config import Config

# from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # login.init_app(app)

    # Session(app)

    # Set up database
    # engine = create_engine(db_url)
    # db = scoped_session(sessionmaker(bind=engine))

    from book_reviews import repo
    repo.init_app(app)

    from book_reviews import books
    app.register_blueprint(books.bp, url_prefix='/books')

    return app
