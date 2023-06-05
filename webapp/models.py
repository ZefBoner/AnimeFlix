from django.contrib.auth.models import AbstractUser
from django.db import models


class Animes(models.Model):
    id_anime = models.AutoField(primary_key=True)
    nombre_anime = models.CharField(max_length=100)
    descripcion_anime = models.CharField(max_length=500, default='no.jpg')
    imagen_anime = models.CharField(max_length=50, default='no.jpg')
    portada_anime = models.CharField(max_length=50, default='no.jpg')

    def __str__(self):
        return self.nombre_anime


class Episodios(models.Model):
    id_episodio = models.AutoField(primary_key=True)
    nombre_episodio = models.CharField(max_length=100)
    temporada = models.IntegerField(default=0)
    episodio = models.IntegerField(default=0)
    episodio_anime = models.ForeignKey(Animes, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre_episodio


class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    episodio = models.ForeignKey(Episodios, on_delete=models.CASCADE, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
