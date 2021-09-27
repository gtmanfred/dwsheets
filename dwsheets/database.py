import databases

from .config import Configuration as config


db = databases.Database(config.DATABASE_URI)
