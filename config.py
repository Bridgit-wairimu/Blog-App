import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/blog'
    SECRET_KEY='23456789'

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/blog'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/blog'
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }