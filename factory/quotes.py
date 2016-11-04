#encoding: utf-8
from peewee import *

db = SqliteDatabase('quotes.db')

class Quote(Model):
    author = CharField()
    text = TextField()

    class Meta:
        database = db

db.connect()

Quote.create_table(True)