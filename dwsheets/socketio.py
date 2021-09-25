import socketio

from .config import Configuration as config


sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=','.join(config.ALLOW_ORIGIN)
)
