import os

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@localhost/{}?charset=utf8mb4"\
                          .format(os.environ['USER'],
                                  os.environ['PASSWORD'],
                                  os.environ['DB_NAME'])
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ['SECRET_KEY']
