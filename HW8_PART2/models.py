from mongoengine import Document
from mongoengine.fields import StringField, BooleanField



class Contacts(Document):
    fullname = StringField()
    email = StringField()
    sign_message = BooleanField(default=False)