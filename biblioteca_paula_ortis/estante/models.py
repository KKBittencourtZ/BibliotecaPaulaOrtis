from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    numero_id = models.ForeignKey(int, unique=True, on_delete=models.CASCADE)
    nome_livro = models.TextField()
    autores = models.TextField()
    situacao = models.CharField()
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    responsavel_alteracao = models.CharField(User)
