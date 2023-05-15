from django.db import models

# Create your models here.
class Trabajo(models.Model):
    imagen = models.FileField(upload_to='galeria/')
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    fecha = models.DateField(verbose_name="Fecha", default='1900-01-01')
    curso = models.CharField(max_length=100, verbose_name="Curso")
    destacado = models.BooleanField(default=False)