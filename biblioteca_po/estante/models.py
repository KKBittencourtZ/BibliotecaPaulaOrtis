from django.contrib.auth.models import User
from django.db import models

class Books(models.Model):
    numero_id = models.ForeignKey(on_delete=models.CASCADE,max_length=4, unique=True, blank=False, null=False)
    nome_livro = models.TextField(blank=False, null=False)
    slug = models.SlugField(nome_livro)
    autores = models.TextField(blank=False, null=False)
    situacao = models.CharField(max_length=10)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    responsavel_alteracao = models.CharField(User)
