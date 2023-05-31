from django.contrib import admin
from taller.models import Curso, CursoDescripcion, Alumno, Turno, Inscripcion

# Register your models here.
admin.site.register(Curso)
admin.site.register(CursoDescripcion)
admin.site.register(Alumno)
admin.site.register(Turno)
admin.site.register(Inscripcion)
