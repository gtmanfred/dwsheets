import figenv


class Configuration(metaclass=figenv.MetaConfig):
    PROJECT_NAME = 'Dungeon World Sheets'

    ALLOW_ORIGIN = ['dwsheets.app']

    DEBUG = False
