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
   path('alta_alumno/', views.alta_alumno,name="alta_alumno"),
   path('gestionar_alumnos/', views.GestionarAlumnos.as_view(), name = 'gestionar_alumnos'),
   path('gestionar_contactos/', views.GestionarContactos.as_view(),name="gestionar_contactos"),
   path('cambiar_contacto/<int:id>/',views.cambiar_contacto, name='cambiar_contacto'),
   path('alta_turno/', views.alta_turno, name = 'alta_turno'),
   path('gestionar_turnos/', views.GestionarTurnos.as_view(), name = 'gestionar_turnos'),
   path('cons_alumno/<int:id>/', views.cons_alumno, name = 'cons_alumno'),
   path('cons_alumno/', views.cons_alumno, name = 'cons_alumno'),
   path('alta_inscripcion/<int:id>/', views.alta_inscripcion, name = 'alta_inscripcion'),
   path('alta_inscripcion2/<int:id>/', views.alta_inscripcion2, name = 'alta_inscripcion2'),
   path('cons_turno/<int:id>/', views.cons_turno, name = 'cons_turno'),
   path('cons_turno/', views.cons_turno, name = 'cons_turno'),
   path('baja_inscripcion/<int:id>/<str:origen>', views.baja_inscripcion, name = 'baja_inscripcion'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)