from django.contrib import admin
from django.db import models

class Books(models.Model):
    numero_id = models.DecimalField(primary_key=True , max_digits=4, unique=True, blank=False, null=False)
    nome_livro = models.TextField(blank=False, null=False)
    slug = models.SlugField(nome_livro)
    autores = models.TextField( default='Desconhecido', null=False)
    # situacao = models.CharField(max_length=10)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    responsavel_alteracao = models.ForeignKey(admin, on_delete=models.CASCADE)
