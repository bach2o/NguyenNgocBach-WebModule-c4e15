from pymongo import *
import mlab
from models.river import River
mlab.connect()

all_rivers_in_africa = River.objects()

for river in all_rivers_in_africa:
    if river['continent'] == 'S. America' and river['length'] < 1000:
        print(river['name'])
