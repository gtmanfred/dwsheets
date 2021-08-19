import os.path
import pathlib

import yaml

srdfile = pathlib.Path(__file__).parent / 'srd.yaml'

class Loader(yaml.SafeLoader):

    def __init__(self, stream):

        self._root = os.path.split(stream.name)[0]

        super(Loader, self).__init__(stream)

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))

        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)

with srdfile.open('r') as fh_:
    srd = yaml.load(fh_, Loader)
