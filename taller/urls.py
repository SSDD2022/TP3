from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="taller"),
    path('galeria/',views.galeria,name="galeria"),
    path('cursos/',views.cursos,name="cursos"),
    path('alumnos/', views.alumnos,name="alumnos"),
    ]