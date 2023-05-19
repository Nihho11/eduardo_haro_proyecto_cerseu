from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido =  models.CharField(max_length=20)
    DNI = models.CharField(max_length=8, default='00000000')

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
