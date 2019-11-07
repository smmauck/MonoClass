from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    # Initialize core
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        # Register blueprints
        from .views import auth
        app.register_blueprint(auth.bp)

        # Create database tables
        from .models import User
        db.create_all()

    return app
