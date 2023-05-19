from django.db import models


class Platos(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
