DEBUG = True
SECRET_KEY = "\xa4C\x04\xaee,\x16\xdc\x9f\x1c'rl)\xa3h\xf8R\x02~\xb6\xbe\xc4\x10"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/flask-practice-db'

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
