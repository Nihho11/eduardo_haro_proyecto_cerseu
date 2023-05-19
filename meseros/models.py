from django.db import models


class Meseros(models.Model):
    nombre = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=30, default='Peruano')
    edad = models.IntegerField

    def __str__(self):
        return "{}, {}".format(self.nombre, self.nacionalidad)

