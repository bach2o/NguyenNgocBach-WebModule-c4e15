<<<<<<< HEAD
import mlab
from models.customer import Customer
from random import randint, choice
from faker import Faker

mlab.connect()

for i in range(100):
    print('Saving customer', i + 1, '....')
    fake = Faker()
    customer = Customer(name = fake.name(),
        gender = randint(0, 1), # 0: female , 1: male
        email = fake.email(),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = randint(0, 1)) # 0: Not contacted, 1: Contacted
    customer.save()
=======
import mlab
from models.customer import Customer
from random import randint, choice
from faker import Faker

mlab.connect()

for i in range(100):
    print('Saving customer', i + 1, '....')
    fake = Faker()
    customer = Customer(name = fake.name(),
        gender = randint(0, 1), # 0: female , 1: male
        email = fake.email(),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = randint(0, 1)) # 0: Not contacted, 1: Contacted
    customer.save()
>>>>>>> c66cbb960d8d7951e6cc6f66a65ddca735944685
