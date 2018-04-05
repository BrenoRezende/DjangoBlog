from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100, unique = True)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    banner = models.ImageField(default = 'default.png', blank = True)
    autor = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.titulo

    def amostra_texto(self):
        return self.texto[:30] + '...'