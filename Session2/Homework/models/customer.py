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
