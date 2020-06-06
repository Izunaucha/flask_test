import os
class Config(object):
    SECRET_KEY = "Fabrizio_j_Catalano"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False