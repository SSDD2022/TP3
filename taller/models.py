from django.db import models
from datetime import datetime
from django import utils
from django.db.models import Sum
from taller.validaciones import ValCelular, ValMail, ValEdadAlumno

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
    def __str__(self):
        return self.titulo
    @property
    def disponible(self):
        cupos = Turno.objects.filter(curso_id=self.curso_id).values("cupo").aggregate(Sum('cupo'))
        cupos = list(cupos.values())[0]
        insc = Inscripcion.objects.filter(turno_id__curso_id=self.curso_id).count()
        return (cupos > insc)
    class Meta:
        ordering = ["titulo"]

class CursoDescripcion (models.Model):
    # Primary key generada automaticamente
    class Meta:
        unique_together = ["curso_id", "posicion_id"]
    curso_id = models.ForeignKey(Curso, related_name='descripciones', on_delete=models.CASCADE)
    posicion_id = models.IntegerField(verbose_name='Posición',unique=False,auto_created=False,
                                     blank=False,null=False,help_text='Posición de la descripción',
                                     #validators=NotImplemented
                                     )
    descripcion = models.CharField(max_length=150,verbose_name='Descripción',
                                   blank=False,null=False,help_text='Descripción',
                                   #validators=NotImplemented
                                   )
    def __str__(self):
        return f'{self.descripcion}'
    class Meta:
        ordering = ["curso_id","posicion_id"]

MOT_Contacto = (('SUG', 'Sugerencia'),
                ('CON', 'Consulta'),
                ('SUS', 'Suscripción'),
                ('INS', 'Inscripción')
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
    alumno_id = models.AutoField(primary_key=True)
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
                                        validators=[ValEdadAlumno]
                                       )
    mail = models.EmailField(max_length=30,verbose_name='Mail',
                             blank=False,null=False,help_text='Mail de contacto',
                             validators=[ValMail])
    celular = models.CharField(max_length=20,verbose_name='Celular',
                               blank=False,null=False,help_text='Celular de contacto',
                               validators=[ValCelular]
                              ) 
    
    @property
    def edad (self):
        return utils.timezone.now().year - self.fecha_nacimiento.year
    def __str__(self):
#        return self.nombre
        return f'{self.nombre} {self.apellido} ({self.edad})'
    class Meta:
        ordering = ["nombre","apellido"]

    
class Turno (models.Model):
    class Experiencia(models.TextChoices):
        SE = "SE", "Sin Experiencia"
        CE = "CE", "Con Experiencia"
        AV = "AV", "Avanzado"
    class Edad(models.TextChoices):
        N = "N", "Niños"
        J = "J", "Jóvenes"
        A = "A", "Adultos"
    turno_id = models.AutoField(primary_key=True)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name='Curso')
    descripción = models.CharField(max_length=50,verbose_name='Dictado',
                               blank=False,null=False,#help_text='Datos del turno',
                               #validators=NotImplemented
                              )  # lunes y jueves de 8 a 10
                                 # martes de 18 a 20 y sábados de 10 a 12
    anio = models.IntegerField(verbose_name='Año de dictado',unique=False,auto_created=False,
                               blank=False,null=False,#help_text='Año de dictado',
                               #validators=NotImplemented
                              )
    destinatario = models.CharField(max_length=1,verbose_name='Destinatarios',
                               blank=False,null=False,#help_text='Destinatarios',
                               choices=Edad.choices,
                               default=Edad.J,
                               #validators=NotImplemented
                              )
    experiencia = models.CharField(max_length=2,verbose_name='Experiencia',
                               blank=False,null=False,#help_text='Experiencia',
                               choices=Experiencia.choices,
                               default=Experiencia.SE,
                               #validators=NotImplemented
                              )
    cupo = models.IntegerField(verbose_name='Cupo',unique=False,auto_created=False,
                               blank=False,null=False,#help_text='Cupo',
                               #validators=NotImplemented
                              )
    alumnos = models.ManyToManyField(Alumno,through='Inscripcion')
    @property
    def destinatario_desc (self):
        for d in Turno.destinatario.field.choices:
           if d[0] == self.destinatario:
               return d[1]
        return self.destinatario
    @property
    def experiencia_desc (self):
        for e in Turno.experiencia.field.choices:
           if e[0] == self.experiencia:
               return e[1]
        return self.experiencia
    @property
    def vacantes (self):
        return self.cupo - Inscripcion.objects.filter(turno_id = self.turno_id).count()
    def __str__(self):
        return f'{self.curso_id} - {self.descripción} - {self.destinatario_desc} - {self.experiencia_desc}'
    @property
    def desc_larga(self):
        return f'{self.curso_id} - {self.descripción} - {self.destinatario_desc} - {self.experiencia_desc}'
    class Meta:
        ordering = ["curso_id","descripción"]

class Inscripcion (models.Model):
    # Primary key generada automaticamente
    class Meta:
        unique_together = ["alumno_id", "turno_id"]
    alumno_id = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    turno_id = models.ForeignKey(Turno,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.turno_id} / {self.alumno_id}'
    class Meta:
        ordering = ["turno_id","alumno_id"]

class Trabajo(models.Model):
    imagen = models.FileField(upload_to='galeria/')
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha", default='1900-01-01')
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name='Curso')
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return f"OBRA: {self.titulo} - AUTOR: {self.autor.nombre} {self.autor.apellido} - FECHA: {self.fecha}"
