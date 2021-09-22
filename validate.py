from pbtasheets.schemas.classes import Class
from seeddata import srd

for cls in srd['classes']:
  Class(**cls)
