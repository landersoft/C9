from django.db import models

# Create your models here.
class Autor(models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
