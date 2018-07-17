"""Application configuration settings"""

import os


class Config(object):
    """Main configuration class"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    """Production environment configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL', None)


class Development(Config):
    """Development environment configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', None)


class Testing(Config):
    """Testing environment configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', None)


SET_ENVIRONMENT = os.environ.get('FLASK_ENV')


CONFIGURATION = {
    'production': Production,
    'development': Development,
    'testing': Testing,
    'default': Development
}

ENVIRONMENT_OBJECT = None

try:
    ENVIRONMENT_OBJECT = CONFIGURATION[SET_ENVIRONMENT]

except KeyError:
    ENVIRONMENT_OBJECT = CONFIGURATION['default']
