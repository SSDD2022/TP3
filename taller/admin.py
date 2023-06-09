from django.contrib import admin
from taller.models import Curso, CursoDescripcion, Alumno, Turno, Inscripcion, Trabajo
from taller.forms import AltaAlumnoForm

# Register your models here.
admin.site.register(Curso)
admin.site.register(CursoDescripcion)
admin.site.register(Turno)
admin.site.register(Inscripcion)

class TrabajoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha', 'curso_id', 'destacado']
admin.site.register(Trabajo, TrabajoAdmin)

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','mail']
    list_editable = ['nombre','apellido']
    list_display_links = ('mail',)
    search_fields = ['nombre']
    form = AltaAlumnoForm
admin.site.register(Alumno, AlumnoAdmin)
# class InscripcionInline(admin.TabularInline):
#     model = Turno.alumnos.through
# class AlumnoAdmin(admin.ModelAdmin):
#     inlines = [
#         InscripcionInline,
#     ]
# class TurnoAdmin(admin.ModelAdmin):
#     inlines = [
#         InscripcionInline,
#     ]
#     exclude = ('alumnos',)