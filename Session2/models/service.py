from mongoengine import Document, StringField, IntField, BooleanField

# Create collection - Tạo tủ
class Service(Document):
    name = StringField()
    yob = IntField()  # Year of birth
    gender = IntField() #0: female, 1: male
    height = IntField()
    phone = StringField()
    address= StringField()
    status = BooleanField()
