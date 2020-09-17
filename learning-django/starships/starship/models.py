from django.db import models

# Create your models here.
class Starship(models.Model):
  name = models.CharField(max_length=128)
  registry = models.CharField(max_length=16)
  shipclass = models.enums.Choices()