from os import environ, path
from dotenv import load_dotenv


class Config():
    TESTING = False
    DEBUG = False


class ConfigDev(Config):
    TESTING = True
    DEBUG = True


class ConfigProd(Config):
    pass