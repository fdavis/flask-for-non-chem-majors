import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = ''
	APP_NAME = 'Flask Test'
	SECRET_KEY = 'thisisaveryhardsecret!1337!1337!|-|4%0|2'
	LISTINGS_PER_PAGE = 10

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@server/db'
	DEBUG = False

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
	DEBUG = True

class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
	TESTING = True
