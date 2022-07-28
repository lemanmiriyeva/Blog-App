from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from app import app


db = SQLAlchemy(app)
migrate = Migrate(app,db, compare_type=True)
admin = Admin(app, name='Blog App', template_mode='bootstrap3' )