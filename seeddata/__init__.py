import pathlib

import yaml

srdfile = pathlib.Path(__file__).parent / 'srd.yaml'

class Loader(yaml.SafeLoader):

    def __init__(self, stream):
        self._root = pathlib.Path(stream.name).parent
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = self._root / self.construct_scalar(node)
        with filename.open('r') as fh_:
            return yaml.load(fh_, Loader)

Loader.add_constructor('!include', Loader.include)

with srdfile.open('r') as fh_:
    srd = yaml.load(fh_, Loader)
