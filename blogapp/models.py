from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=30, unique=True)
    subtitulo = models.CharField(max_length=40)
    texto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    # image = StdImageField(upload_to='static/img/', variations={'thumbnail': {"width": 300, "height": 400, "crop": True}}, blank=True, null=True)
    #tag
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # test
    
    def __str__(str):
        return self.titulo
        
        