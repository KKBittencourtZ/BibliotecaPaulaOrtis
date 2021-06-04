from django.contrib.auth.models import AbstractUser

class Bibliotecaria(AbstractUser):
    pass


# class Books(models.Model):
#     numero_id = models.DecimalField(primary_key=True , max_digits=4, unique=True, blank=False, null=False)
#     nome_livro = models.TextField(blank=False, null=False)
#     slug = models.SlugField(nome_livro)
#     autores = models.TextField( default='Desconhecido', null=False)
#     # situacao = models.CharField(max_length=10)
#     cadastrado_em = models.DateTimeField(auto_now_add=True)
#     ultima_alteracao = models.DateTimeField(auto_now=True)
#     responsavel_alteracao = models.ForeignKey(User, on_delete=models.CASCADE)
