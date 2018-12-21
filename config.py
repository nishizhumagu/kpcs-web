class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = None
    #
    # @staticmethod
    # def init_app(app):
    #     pass


class Productingconfig(Config):
    SECRET_KEY = 'mimahenfuzanibuyaocaile'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fy@127.0.0.1/data-kpcs'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1


class Developmentconfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////root/pycharm-projects/kpcs-web/data-dev.sqlite'


class Testingconfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fy@127.0.0.1:3306/data-test'


