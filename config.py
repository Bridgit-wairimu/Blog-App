import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/blog'
    SECRET_KEY='23456789'


#  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "kirikabridgit@gmail.com"
    MAIL_PASSWORD = "9089%300"
    
class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/blog'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/blog'
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }