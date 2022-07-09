import mongoengine as me


class Users(me.Document):
    email = me.EmailField()