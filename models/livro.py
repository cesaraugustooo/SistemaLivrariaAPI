from peewee import AutoField, CharField, FloatField, IntegerField, Model
from config.database import database


class Livro(Model):
    id = AutoField()
    nome = CharField()
    descricao = CharField()
    preco = FloatField()
    genero = CharField()
    editora = CharField()
    edicao = CharField()
    publicacao = CharField()

    class Meta:
        database = database
