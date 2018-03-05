<<<<<<< HEAD
from mongoengine import Document, StringField, IntField, BooleanField

# Create collection - Tạo tủ
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = IntField()
=======
from mongoengine import Document, StringField, IntField, BooleanField

# Create collection - Tạo tủ
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = IntField()
>>>>>>> c66cbb960d8d7951e6cc6f66a65ddca735944685
