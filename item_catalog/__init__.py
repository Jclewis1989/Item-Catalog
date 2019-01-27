from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db.init_app(app)
    
    from item_catalog.main.routes import main
    from item_catalog.posts.routes import posts
    from item_catalog.json.routes import json

    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(json)

    return app