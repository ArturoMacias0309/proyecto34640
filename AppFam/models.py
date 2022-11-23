from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    birthdate = models.DateField()
    edad = models.IntegerField()