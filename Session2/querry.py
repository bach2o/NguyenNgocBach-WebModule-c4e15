import mlab
from models.service import Service

mlab.connect()



get_id = Service.objects.get(id= '5a95632b4506281ed0759bea')

print(get_id.to_mongo())
