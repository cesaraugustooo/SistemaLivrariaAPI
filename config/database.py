from peewee import SqliteDatabase

database = SqliteDatabase('database.db')

def conect():
    database.connect()
    from models.livro import Livro
    database.create_tables([Livro])

class end():
    database.close()

