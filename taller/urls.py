from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('',views.index,name="taller"),
   path('galeria/',views.galeria,name="galeria"),
   path('cursos/',views.cursos,name="cursos"),
 #  re_path(r'^cursos/inscripcion/(?P<id_curso>[0-9]+)/$', views.inscripcion, name="inscripcion"),
 #  re_path(r'^cursos/inscripcion/(?P<id_curso>\d{1,2})/$', views.inscripcion, name="inscripcion"),
   path('cursos/inscripcion/<int:id_curso>/', views.inscripcion, name="inscripcion"),
   path('cursos/inscripcion/', views.inscripcion, name="inscripcion"),
   path('agregar_trabajo/', views.agregar_trabajo, name="agregar_trabajo"),
   path('cambiar_destacado/<int:trabajo_id>/', views.cambiar_destacado, name='cambiar_destacado'),
   path('contacto/<motivo>/', views.contacto, name="contacto"),
   path('contacto/', views.contacto, name="contacto"),
   path('alta_alumnos/', views.alta_alumnos,name="alta_alumnos"),
   path('cons_alumnos/', views.cons_alumnos,name="cons_alumnos"),
   path('cons_cursos/', views.cons_cursos,name="cons_cursos"),
   path('gestionar_contactos/', views.gestionar_contactos,name="gestionar_contactos"),
   ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)