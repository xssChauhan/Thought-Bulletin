import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
	
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
	app.config['SECRET_KEY'] = '$%&??!'
	bootstrap.init_app(app)
	db.init_app(app)
	
	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app