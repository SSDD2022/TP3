from django.contrib import admin
from taller.models import Curso, CursoDescripcion, Alumno, Turno, Inscripcion, Trabajo

# Register your models here.
admin.site.register(Curso)
admin.site.register(CursoDescripcion)
admin.site.register(Alumno)
admin.site.register(Turno)
admin.site.register(Inscripcion)

class TrabajoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha', 'curso_id', 'destacado']
admin.site.register(Trabajo, TrabajoAdmin)
