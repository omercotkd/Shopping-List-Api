import mongoengine as me
from Modules.DB_Collections.users import Users
import uuid

class ShoppingItem(me.EmbeddedDocument):
    id = me.StringField(default=str(uuid.uuid4))
    name = me.StringField()
    amount = me.IntField()
    unit = me.StringField()
    link = me.StringField()
    priority = me.IntField()


class Shoppinglists(me.Document):
    owners = me.ListField(me.ReferenceField(Users))
    items = me.EmbeddedDocumentListField(ShoppingItem)
    name = me.StringField()