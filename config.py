__author__ = 'Girish'


import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY ='Top SECRET'


config = {
    'development':DevelopmentConfig
}

