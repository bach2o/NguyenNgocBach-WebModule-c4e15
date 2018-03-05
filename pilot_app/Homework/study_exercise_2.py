<<<<<<< HEAD
import mlab
from models.customer import Customer

mlab.connect()


bro_get_the_id = Customer.objects.get(id= input('Bro, give me the id you want to get!'))

print(bro_get_the_id.to_mongo())
=======
import mlab
from models.customer import Customer

mlab.connect()


bro_get_the_id = Customer.objects.get(id= input('Bro, give me the id you want to get!'))

print(bro_get_the_id.to_mongo())
>>>>>>> c66cbb960d8d7951e6cc6f66a65ddca735944685
