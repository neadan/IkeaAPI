from flask import Flask

from app.bathroom.routes import bathroom_bp
from app.lighting.routes import lighting_bp
from app.models import db


def create_app():
    app = Flask("IkeaAPI")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ikea.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(bathroom_bp)
    app.register_blueprint(lighting_bp)
    return app
