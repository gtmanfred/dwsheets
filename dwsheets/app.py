import fastapi.staticfiles
import socketio
from fastapi.responses import RedirectResponse

from . import __version__
from .config import Configuration as config
from .socketio import sio
from .utils.loader import load_handlers


def redirect_to_ui():
    return RedirectResponse('/ui')


def healthcheck():
    return {'message': "I'm doing OK. Thanks for asking."}


def create_app(debug=False):
    app = fastapi.FastAPI(
        title=config.PROJECT_NAME,
        description=config.PROJECT_NAME,
        version=__version__,
        debug=debug,
    )

    sio_asgi_app = socketio.ASGIApp(
        socketio_server=sio,
        other_asgi_app=app
    )

    app.add_route("/socket.io/", route=sio_asgi_app, methods=['GET', 'POST'])
    app.add_websocket_route("/socket.io/", sio_asgi_app)

    app.mount(
        '/ui',
        fastapi.staticfiles.StaticFiles(
            directory='dwsheets/static/',
            html=True,
            check_dir=False,
        )
    )
    app.get('/')(redirect_to_ui)
    app.get('/health')(healthcheck)

    load_handlers(app)

    return app
