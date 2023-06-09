from typing import Any, Optional
from django.contrib import admin
from django import utils
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.http.request import HttpRequest
from taller.models import Curso, CursoDescripcion, Alumno, Turno, Inscripcion, Trabajo
from taller.forms import AltaAlumnoForm

# Register your models here.
admin.site.register(Curso)
admin.site.register(CursoDescripcion)
admin.site.register(Turno)


class TrabajoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha', 'curso_id', 'destacado']
admin.site.register(Trabajo, TrabajoAdmin)


class InscripcionInline(admin.TabularInline):
    model = Inscripcion  # Turno.alumnos.through (si no se creo, y en Turno usar exclude de alumnos)
    extra = 2  # Filas para dar de alta

@admin.display (description='Edad')
def alumno_edad(objeto):
    return utils.timezone.now().year - objeto.fecha_nacimiento.year
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','mail',alumno_edad,'alumno_edad2']

    @admin.display (description='Edad2')
    def alumno_edad2(self, objeto):
        return utils.timezone.now().year - objeto.fecha_nacimiento.year
    
    list_editable = ['nombre','apellido']
    list_display_links = ('mail',)
    search_fields = ['nombre']
    form = AltaAlumnoForm
    inlines = (InscripcionInline,)

