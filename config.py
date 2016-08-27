import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'yiwj\xfa\xe0\x18\xe7\xde\xa1\x8b#\x9e\xdbyXqC\x9e\xcdK\xcaz8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mtotooh@localhost/auto_exam"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mtotooh@localhost/flask_blog_testdb'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
    "production": ProductionConfig
}