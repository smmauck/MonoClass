from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

	# Initialize core
	app = Flask(__name__)
	app.config.from_object('config.Config')

	# Initialize plugins
	db.init_app(app)

	with app.app_context():
		from api.views import auth

		app.register_blueprint(auth.bp)

	return app