import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '77Fo*MJy1h0k'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False