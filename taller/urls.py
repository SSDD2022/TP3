from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="taller"),
    path('galeria/',views.galeria,name="galeria"),
    path('cursos/',views.cursos,name="cursos"),
    path('alumnos/', views.alumnos,name="alumnos"),
    path('cursos/inscripcion/<int:id_curso>/', views.inscripcion, name="inscripcion_curso"),
    path('cursos/inscripcion/', views.inscripcion, name="inscripcion"),
    path('agregar_trabajo/', views.agregar_trabajo, name="agregar_trabajo")
    ]
