from django.db import models
from datetime import datetime
from django import utils


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

MOT_Contacto = (('SUG', 'Sugerencia'),
                ('CON', 'Consulta'),
                ('SUS', 'Suscripción')
               ) 
class Contacto (models.Model):
    motivo = models.CharField(max_length=3,verbose_name='Motivo', choices=MOT_Contacto,
                              blank=False,null=False,help_text='Motivo del contacto') 
    nombre = models.CharField(max_length=30,verbose_name='Nombre',
                              blank=False,null=False,help_text='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido',
                              blank=False,null=False,help_text='Apellido')
    mail = models.EmailField(max_length=30,verbose_name='Mail',
                             blank=False,null=False,help_text='Mail')
    comentario = models.CharField(max_length=500,verbose_name='Comentario',
                                  blank=True,null=True,help_text='Comentario')
    fecha = models.DateField(verbose_name="Fecha",
                             blank=False,null=False,help_text='Fecha',
                             default=utils.timezone.now
                             #default=datetime.strptime(datetime.today().strftime('%Y-%m.%d'),'%Y-%m.%d')
                             #validators=NotImplemented
                             )
    revisado = models.BooleanField(verbose_name='Revisado',
                             blank=False,null=False,help_text='Revisado',default=False)
    @property
    def motivo_desc (self):
        for mot in Contacto.motivo.field.choices:
           if mot[0] == self.motivo:
               return mot[1]
        return self.motivo

class Alumno(models.Model):
    alumno_id = models.IntegerField(verbose_name='Alumno',primary_key=True,auto_created=False,
                                   blank=False,null=False,help_text='Código de alumno',
                                   #validators=NotImplemented
                                   )
    nombre = models.CharField(max_length=50,verbose_name='Nombre',
                              blank=False,null=False,help_text='Nombre del alumno',
                              #validators=NotImplemented
                              )
    apellido = models.CharField(max_length=50,verbose_name='Apellido',
                                blank=False,null=False,help_text='Apellido del alumno',
                                #validators=NotImplemented
                             )
    fecha_nacimiento = models.DateField(verbose_name="Nacimiento",
                                        blank=False,null=False,help_text='Fecha de nacimiento',
                                        #validators=NotImplemented
                                       )
    mail = models.EmailField(max_length=30,verbose_name='Mail',
                             blank=False,null=False,help_text='Mail de contacto')
    celular = models.CharField(max_length=20,verbose_name='Celular',
                               blank=False,null=False,help_text='Celular de contacto',
                               #validators=NotImplemented
                              )  #+54 9 11 1111-2222

class Turno (models.Model):
    class Experiencia(models.TextChoices):
        SE = "SE", "Sin Experiencia"
        CE = "CE", "Con Experiencia"
        AV = "AV", "Avanzado"
    class Edad(models.TextChoices):
        N = "N", "Niños"
        J = "J", "Jóvenes"
        A = "A", "Adultos"

    turno_id = models.IntegerField(verbose_name='Turno',primary_key=True,auto_created=False,
                                   blank=False,null=False,help_text='Código de turno',
                                   #validators=NotImplemented
                                  )
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    descripción = models.CharField(max_length=50,verbose_name='Dictado',
                               blank=False,null=False,help_text='Datos del turno',
                               #validators=NotImplemented
                              )  # lunes y jueves de 8 a 10
                                 # martes de 18 a 20 y sábados de 10 a 12
    anio = models.IntegerField(verbose_name='Año',unique=False,auto_created=False,
                               blank=False,null=False,help_text='Año de dictado',
                               #validators=NotImplemented
                              )
    destinatario = models.CharField(max_length=1,verbose_name='Destinatarios',
                               blank=False,null=False,help_text='Destinatarios',
                               choices=Edad.choices,
                               default=Edad.J,
                               #validators=NotImplemented
                              )
    experiencia = models.CharField(max_length=2,verbose_name='Experiencia',
                               blank=False,null=False,help_text='Experiencia',
                               choices=Experiencia.choices,
                               default=Experiencia.SE,
                               #validators=NotImplemented
                              )
    cupo = models.IntegerField(verbose_name='Cupo',unique=False,auto_created=False,
                               blank=False,null=False,help_text='Cupo',
                               #validators=NotImplemented
                              )
    alumnos = models.ManyToManyField(Alumno,through='Inscripcion')

class Inscripcion (models.Model):
    # Primary key generada automaticamente
    class Meta:
        unique_together = ["alumno_id", "turno_id"]
    alumno_id = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    turno_id = models.ForeignKey(Turno,on_delete=models.CASCADE)
class Trabajo(models.Model):
    imagen = models.FileField(upload_to='galeria/')
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    fecha = models.DateField(verbose_name="Fecha", default='1900-01-01')
    curso = models.CharField(max_length=100, verbose_name="Curso")
    destacado = models.BooleanField(default=False)