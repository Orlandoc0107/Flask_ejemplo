#importamos flask
from flask import Flask,Blueprint
from .models.models import db
from .routers.routes_auth import auth
import pymysql
import os
from dotenv import load_dotenv

load_dotenv() 

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '..', 'producionDB.db')


def create_app():
    app = Flask(__name__)

    # Configura la base de datos 

    #SQlite --> Para desarrollo Descomenta esta linea y comenta la configuracion para MySQl
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    #MySQL ---> Cuando ya esta Desplegado

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.register_blueprint(auth)

    return app
