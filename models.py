from datetime import datetime
from mongoengine import Document, StringField, IntField, DateTimeField, connect

connect('Alunos')

class Aluno(Document):
    
    nome = StringField(required=True)
    idade = IntField(required=True)
    curso = StringField(required=True)
    data_criacao = DateTimeField(required=True, default=datetime.utcnow())