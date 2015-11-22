# Create your models here.

from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
   autor = models.ForeignKey('auth.User')
   titulo =  models.CharField(max_length=200)
   texto = models.TextField()
   fechacreacion = models.DateTimeField(default=timezone.now)
   fechapublicacion = models.DateTimeField(blank=True, null=True)
   

def publish(self):
  self.fechapublicacion = timezone.now()
  self.save()

def __str__(self):
  return self.titulo

