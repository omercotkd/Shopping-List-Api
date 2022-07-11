import mongoengine as me
from Modules.DB_Collections.users import Users
from UsefulFunctions.ids_genertors import random_string_id

class ShoppingItem(me.EmbeddedDocument):
    id = me.StringField(default=random_string_id)
    name = me.StringField()
    amount = me.IntField()
    unit = me.StringField()
    link = me.StringField()
    priority = me.IntField()


class Shoppinglists(me.Document):
    owners = me.ListField(me.ReferenceField(Users))
    items = me.EmbeddedDocumentListField(ShoppingItem)
    name = me.StringField()