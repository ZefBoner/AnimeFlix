from django.db import models

# Create your models here.
class Animes(models.Model):
    id_anime = models.IntegerField(primary_key=True)
    nombre_anime = models.CharField(max_length=100)
