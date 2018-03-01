import mlab
from models.customer import Customer

mlab.connect()

Customer.objects(id = input('Bro, give me the id you want to delete!')).delete()
