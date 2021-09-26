import importlib.abc
import importlib.machinery
import importlib.util
import os
import pathlib
import sys

import fastapi


class HandlerLoader(importlib.abc.SourceLoader):

    def __init__(self, fullname, path):
        """Cache the module name and the path to the file found by the
        finder."""
        self.name = fullname
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, path):
        with open(path, 'rb') as codefile:
            return codefile.read()

    def exec_module(self, module, app: fastapi.FastAPI, version: str):
        super().exec_module(module)

        if (router := getattr(module, 'router', None)) is None:
            return

        app.include_router(
            router,
            prefix=f'/api/{version}',
        )

        return module


def load_handlers(app: fastapi.FastAPI):

    loader_details = [
        (HandlerLoader, importlib.machinery.SOURCE_SUFFIXES),
    ]

    handler_dir = pathlib.Path(os.path.dirname(__file__)).parent / 'handlers'

    for version_dir in handler_dir.iterdir():
        if not version_dir.is_dir():
            continue
        version = version_dir.name
        finder = importlib.machinery.FileFinder(
            str(version_dir),
            *loader_details,
        )

        for entry in version_dir.iterdir():
            if entry.name in ('__init__.py', ):
                continue

            # use the FileFinder to find the spec for `entry` module in `path`
            modname, _ = os.path.splitext(entry.name)
            spec = finder.find_spec(modname)
            if not spec.loader:
                continue
            module = importlib.util.module_from_spec(spec)
            sys.modules[modname] = module
            spec.loader.exec_module(module, app=app, version=version)
