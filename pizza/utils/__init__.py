from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
