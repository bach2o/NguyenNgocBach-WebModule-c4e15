from mongoengine import*

# Create collection - Tạo tủ
class Service(Document):
    image = StringField()
    name = StringField()
    yob = IntField()  # Year of birth
    gender = IntField() #0: female, 1: male
    height = IntField()
    measurements = ListField() # List
    phone = StringField()
    address= StringField()
    description = StringField()
    status = BooleanField()
