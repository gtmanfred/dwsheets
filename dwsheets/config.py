import figenv


class Configuration(metaclass=figenv.MetaConfig):
    PROJECT_NAME = 'Dungeon World Sheets'
    ALLOW_ORIGIN = ['dwsheets.app']
    DEBUG = False
    DATABASE_URI = 'sqlite:///database.db'

    # OAUTH2
    SECRET = '511ed3627bdfce473d785669af34fbc8ffc427c29c4bfc0b85e2b811593b67e0'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
