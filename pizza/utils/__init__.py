from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

jwt = JWTManager()
app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
