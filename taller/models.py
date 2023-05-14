from django.db import models

# Create your models here.
class Curso (models.Model):
    curso_id = models.IntegerField(verbose_name='Código',primary_key=True,auto_created=False,
                                   blank=False,null=False,help_text='Código de curso',
                                   #validators=NotImplemented*/
                                       )
    titulo = models.CharField(max_length=50,verbose_name='Curso',
                              blank=False,null=False,help_text='Nombre del curso',
                              #validators=NotImplemented
                              )
    imagen = models.CharField(max_length=30,verbose_name='Imagen',
                              blank=False,null=False,help_text='Imagen curso',
                              #validators=NotImplemented
                              )


class CursoDescripcion (models.Model):
    # Primary key generada automaticamente
    class Meta:
        unique_together = ["curso_id", "posicion_id"]
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    posicion_id = models.IntegerField(verbose_name='Posición',unique=False,auto_created=False,
                                     blank=False,null=False,help_text='Posición de la descripción',
                                     #validators=NotImplemented
                                     )
    descripcion = models.CharField(max_length=150,verbose_name='Descripción',
                                   blank=False,null=False,help_text='Descripción',
                                   #validators=NotImplemented
                                   )



#class Turno (models.Model, Curso)
#   
#
#        self.tipo_participante = tipo_participante
#        self.imagen = imagen
#        self.cupo = cupo
#        self.visual = visual