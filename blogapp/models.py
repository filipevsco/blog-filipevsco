from django.db import models
from users.models import CustomUser


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    titulo = models.Charfield(max_lengh=30, unique=True)
    subtitulo = models.Charfield(max_length=40)
    texto = models.TextField()
    autor = models.ForeignKey(CustomUser, verbose_name=_(""), on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    # image = StdImageField(upload_to='static/img/', variations={'thumbnail': {"width": 300, "height": 400, "crop": True}}, blank=True, null=True)
    #tag
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)