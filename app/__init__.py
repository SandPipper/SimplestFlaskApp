from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

query_cache = {}
mysql_engine = create_engine("mysql+pymysql://{}:{}@localhost/?charset=utf8mb4"\
                             .format(os.environ['USER'],
                                     os.environ['PASSWORD']),
                             execution_options={'compiled_cache': query_cache})
if __name__ != '__main__':
    mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {} \
                                  CHARACTER SET utf8 COLLATE utf8_unicode_ci" \
                                  .format(os.environ['DB_NAME']))

mysql_engine.execute("USE {}".format(os.environ['DB_NAME']))

from app import views, models
