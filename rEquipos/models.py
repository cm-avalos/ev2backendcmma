from django.db import models

# Create your models here.
class Equipos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    grafica = models.CharField(max_length=50)
    memoria= models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)