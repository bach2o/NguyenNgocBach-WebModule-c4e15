<<<<<<< HEAD
import mlab
from models.customer import Customer

mlab.connect()

Customer.objects(id = input('Bro, give me the id you want to delete!')).delete()
=======
import mlab
from models.customer import Customer

mlab.connect()

Customer.objects(id = input('Bro, give me the id you want to delete!')).delete()
>>>>>>> c66cbb960d8d7951e6cc6f66a65ddca735944685
