from django.db import models

# Create your models here.
class Starship(models.Model):
  name = models.CharField(max_length=50)
  registry = models.CharField(max_length=50)
  crew = models.IntegerField()

  def __str__(self):
    return self.name