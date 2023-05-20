from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('',views.index,name="taller"),
   path('galeria/',views.galeria,name="galeria"),
   path('cursos/',views.cursos,name="cursos"),
   path('alumnos/', views.alumnos,name="alumnos"),
 #  re_path(r'^cursos/inscripcion/(?P<id_curso>[0-9]+)/$', views.inscripcion, name="inscripcion"),
 #  re_path(r'^cursos/inscripcion/(?P<id_curso>\d{1,2})/$', views.inscripcion, name="inscripcion"),
   path('cursos/inscripcion/<int:id_curso>/', views.inscripcion, name="inscripcion"),
   path('cursos/inscripcion/', views.inscripcion, name="inscripcion"),
   path('agregar_trabajo/', views.agregar_trabajo, name="agregar_trabajo"),
   path('contacto/<motivo>/', views.contacto, name="contacto"),
   path('contacto/', views.contacto, name="contacto")
   ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)