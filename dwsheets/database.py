from sqlalchemy.ext.asyncio import create_async_engine

from .config import Configuration as config


def create_engine():
    connect_args = {"check_same_thread": False}
    engine = create_async_engine(
        config.SQLALCHEMY_DATABASE_URI,
        future=True,
        echo=True,
        connect_args=connect_args,
    )
    return engine
