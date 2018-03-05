
import mlab
from models.service import Service
from random import randint, choice
from faker import Faker

mlab.connect()

# for i in range(50):
#     print('Saving service', i + 1, '....')
fake = Faker()
service = Service(
    image = "https://vignette.wikia.nocookie.net/naruto/images/b/b3/Tsunade_infobox2.png/revision/latest/scale-to-width-down/300?cb=20150108211132",
    name = "Tsunade",
    yob = 0,  # Year of birth
    gender = 0, #0: female, 1: male
    height = 163,
    measurements = [106,62,90], # List
    phone=fake.phone_number(),
    address = "Hidden Leaf Village",
    description = "Tsunade was very willing to believe in the attainability of dreams while Nawaki and Dan were alive, and that by supporting and encouraging those dreams she might be able to help achieve them. When both died gruesomely shortly after receiving her support, Tsunade lost faith in the idea of dreaming for anything, believing that the mere pursuit would be doomed from the outset. She becomes especially critical of wanting to be Hokage, as both Dan and Nawaki died trying to attain the title and the past Hokage have all died prematurely and, Tsunade argues, pointlessly because they held the position; she concludes that to be Hokage is a fool's job. ",
    status = choice([True, False])
                )
service.save()
