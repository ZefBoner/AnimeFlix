from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class Animes(models.Model):
    id_anime = models.IntegerField(primary_key=True)
    nombre_anime = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_anime

class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50, unique=True)  # Añade unique=True para evitar nombres de usuario duplicados
    apellido = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    estaviendoanime = models.ForeignKey(Animes, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Validar si el nombre de usuario ya existe antes de guardar
        if Usuarios.objects.filter(usuario=self.usuario).exists():
            raise ValidationError('El nombre de usuario ya existe. Por favor, elige otro nombre de usuario.')

        super().save(*args, **kwargs)

