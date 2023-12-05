class ConfigDev:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/sisprev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ConfigProd:
    DEBUG = False

config = {
    'development': ConfigDev
}