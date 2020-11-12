from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)



# use Config class
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# from app import routes, j'importe toutes routes definis dans routes.py
from app import routes, models



#https://ondras.zarovi.cz/sql/demo/
