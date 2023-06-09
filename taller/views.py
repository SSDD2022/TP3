from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from django import utils
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.forms import ModelForm
from . import classes
from . import forms
from taller.models import Curso, CursoDescripcion, Trabajo, Contacto, Turno, Alumno, Inscripcion
from taller.forms import AltaAlumnoForm, AltaTurnoForm, AltaInscripcionForm, AltaInscripcionForm2
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Para validar que el usuario pertenezca a cierto grupo
def administrativo(user):
    return user.groups.filter(name='AdmTaller').exists()

def alumno(user):
    return user.groups.filter(name='Alumno').exists()

# Create your views here.
def index(request):
    context = { 'pagina' : 'taller/index.html',
              }
    return render(request,"taller/index.html",context)

def galeria(request):

    destacados = Trabajo.objects.filter(destacado=True)
    #momentaneo hasta tomar los datos de la BD ---------------------
    #trabajos =[{'imagen':'galeria/i1.jpg','titulo':'TITULO 1','autor':'Fulano','fecha':2005,'destacado':True},{'imagen':'galeria/i2.jpg','titulo':'TITULO 2','autor':'Sultano','fecha':2010,'destacado':False},{'imagen':'galeria/i3.jpg','titulo':'TITULO 3','autor':'Mengano','fecha':2015,'destacado':False},{'imagen':'galeria/i4.jpg','titulo':'TITULO 4','autor':'Juan','fecha':2017,'destacado':True},{'imagen':'galeria/i5.jpg','titulo':'TITULO 5','autor':'Vale','fecha':2013,'destacado':True},{'imagen':'galeria/i6.jpg','titulo':'TITULO 4','autor':'Silvia','fecha':2022,'destacado':False},{'imagen':'galeria/i7.jpg','titulo':'TITULO 7','autor':'Adri','fecha':2012,'destacado':True}]
    #---------------------------------------------------------------
    
    trabajos = Trabajo.objects.all().order_by("-fecha")

 #   for trabajo in trabajos:
 #       if trabajo.destacado:
 #           destacados.append(trabajo)

    context = {'trabajos':trabajos, 'destacados':destacados}
    
    return render(request,"taller/galeria.html",context)

@permission_required('taller.cambiar_destacado')
def cambiar_destacado(request, trabajo_id):
    trabajo = Trabajo.objects.get(id=trabajo_id)
    trabajo.destacado = not trabajo.destacado
    trabajo.save()
    return redirect('galeria')

def cursos(request):

    ListadoCursos = []
    cursillo = Curso.objects.order_by('curso_id')
    for c in cursillo:
        v = classes.Visual("flush-heading"+str(c.curso_id),"#flush-collapse"+str(c.curso_id),
                           "flush-collapse"+str(c.curso_id))
        x = classes.CursoOld(c.curso_id, c.titulo,[],
                             'taller/img/' + c.imagen,c.disponible,v)
        descripcioncilla = CursoDescripcion.objects.filter(curso_id=c.curso_id).order_by('posicion_id')
        for desc in descripcioncilla.all():
            x.descripcion.append(desc.descripcion)
        ListadoCursos.append(x)

    context = { 'cursos': ListadoCursos }
    return render(request,"taller/cursos.html",context)

@login_required
@user_passes_test(administrativo)
def cons_alumno(request, id):
    context = {}
    try:
        alumno = Alumno.objects.get(alumno_id=id)
    except Alumno.DoesNotExist:
        raise Http404('Alumno inexistente')
    context['alumno'] = alumno

    listado = Inscripcion.objects.filter(alumno_id=id).values( "id","turno_id__curso_id","turno_id__curso_id__titulo","turno_id__descripción").order_by("turno_id__curso_id__titulo","turno_id__descripción")
    #.query
    context['listado'] = listado
    return render(request, 'taller/cons_alumno.html', context)

def cons_cursos(request):
    context = { 'pagina' : 'Consulta de cursos',
              }
    return render(request,'taller/cons_cursos.html',context)

@login_required
@user_passes_test(administrativo)
def inscripcion(request, id_curso=None):
    if request.method == 'POST':
        #POST
        inscripcion_form = forms.Inscripcion_form(request.POST)
        if inscripcion_form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Inscripción realizada correctamente')
            return redirect(reverse('cursos'))
        else:
#            for field in inscripcion_form:
#                for error in field.errors:
#                    messages.add_message(request, messages.ERROR,error)
             messages.add_message(request, messages.ERROR,"Por favor verifica los datos")
    else:
        #GET
        inscripcion_form = forms.Inscripcion_form(initial={'cursos':id_curso})

    context = {'form': inscripcion_form}
    return render(request,'taller/inscripcion.html' ,context)

@login_required
@user_passes_test(alumno)
def agregar_trabajo(request):
    if request.method == 'POST':
        #POST
        agregar_trabajo_form = forms.agregar_trabajo_form(request.POST, request.FILES)
         # Validaciones
        if agregar_trabajo_form.is_valid():
            nuevo_trabajo = Trabajo(
                titulo=agregar_trabajo_form.cleaned_data['titulo'], 
                autor=agregar_trabajo_form.cleaned_data['autor'], 
                imagen=agregar_trabajo_form.cleaned_data['imagen'],
                fecha=agregar_trabajo_form.cleaned_data['fecha'],
                curso_id=agregar_trabajo_form.cleaned_data['curso_id']
            ) 
            nuevo_trabajo.save()
            messages.add_message(request, messages.SUCCESS, 'Trabajo agregado a la galería Correctamente', extra_tags="mensaje_exitoso")
            return redirect(reverse('galeria'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocurrió un error')

    else:
        #GET
        agregar_trabajo_form = forms.agregar_trabajo_form()
    
    context = {'form': agregar_trabajo_form}
    return render(request, "taller/agregar_trabajo_galeria.html", context)

def contacto(request,motivo=None):
    if request.method == 'POST':
        #POST
        contacto_form = forms.Contacto(request.POST)
        if contacto_form.is_valid():
            motivo = contacto_form.cleaned_data["motivo"]
            nombre = contacto_form.cleaned_data["nombre"]
            apellido = contacto_form.cleaned_data["apellido"]
            mail = contacto_form.cleaned_data["mail"]
            comentario = contacto_form.cleaned_data["comentario"]
            contacto = Contacto (motivo=motivo,nombre=nombre,apellido=apellido,
                                 mail=mail,comentario=comentario)
            contacto.save()
            messages.add_message(request, messages.SUCCESS, 'Mensaje recibido correctamente')
            if motivo != 'INS':
               return redirect(reverse('taller'))
            else:
               return redirect(reverse('cursos'))         
        else:
            messages.add_message(request, messages.ERROR,"Por favor verifica los datos")
    else:
        #GET
        contacto_form = forms.Contacto(initial={'motivo':motivo})

    context = {'form': contacto_form}
    return render(request,"taller/contacto.html",context)
class GestionarContactos(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model=Contacto
    context_object_name = 'Contacto'
    template_name = 'taller/gestionar_contactos.html'
    fields=["id","revisado","fecha","motivo","nombre","apellido","mail","comentario"]
    ordering = ["revisado","fecha"]
    def test_func(self):
        return administrativo(self.request.user)

@login_required
@user_passes_test(administrativo)
def cambiar_contacto(request, id):
    cont = Contacto.objects.get(id=int(id))
    cont.revisado = True
    cont.save()
    return redirect(reverse('gestionar_contactos')) 

@login_required
@user_passes_test(administrativo)
def alta_alumno(request):
    context ={}

    if request.method == "POST":
        form = AltaAlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Alumno dado de alta correctamente')
            return redirect(reverse("alta_alumno"))
        else:
            messages.add_message(request, messages.ERROR,"Por favor verifica los datos")
    else:
        form = AltaAlumnoForm()

    context['form'] = form
    return render(request, 'taller/alta_alumnos.html', context)

@login_required
@user_passes_test(administrativo)
def alta_turno(request):
    context ={}

    if request.method == "POST":
        form = AltaTurnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Turno dado de alta correctamente')
            return redirect(reverse("alta_turno"))
        else:
            messages.add_message(request, messages.ERROR,"Por favor verifica los datos")
    else:
        val_inicial={'anio':utils.timezone.now().year}
        primer_curso = Curso.objects.filter(titulo__contains='adultos').first()
        # primer_curso = Curso.objects.first()
        # if primer_curso is not None:
        #     primer_curso = Curso.objects.filter(curso_id__gt=primer_curso.curso_id).first()
        if primer_curso is not None:
            val_inicial['curso_id'] = primer_curso

        if primer_curso is not None:
            val_inicial['curso_id'] = primer_curso
        form = AltaTurnoForm(initial=val_inicial)

    context['form'] = form
    return render(request, 'taller/alta_turno.html', context)

class GestionarTurnos(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model=Turno
    context_object_name = 'Turno'
    template_name = 'taller/gestionar_turnos.html'
    exclude=["id","alumnos"]
    ordering = ["-anio","curso_id","destinatario","experiencia","-cupo"]
    def test_func(self):
        return administrativo(self.request.user)
class GestionarAlumnos(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model=Alumno
    context_object_name = 'Alumno'
    template_name = 'taller/gestionar_alumnos.html'
    ordering = ["nombre","apellido"]
    def test_func(self):
        return administrativo(self.request.user)
    
@login_required
@user_passes_test(administrativo)
def alta_inscripcion(request,id=None):
    context ={}

    if request.method == "POST":
        form = AltaInscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inscripcion dada de alta correctamente')
            #return redirect(reverse("alta_inscripcion"),id)
            return redirect(reverse("gestionar_turnos"))
        else:
            messages.add_message(request, messages.ERROR,"Por favor verifica los datos")
    else:
        primer_curso = Curso.objects.filter(titulo__contains='adultos').first()
        val_inicial = {}
        val_inicial['turno_id'] = Turno.objects.get(turno_id=int(id))
        form = AltaInscripcionForm(initial=val_inicial)

    context['form'] = form
    return render(request, 'taller/alta_inscripcion.html', context)

@login_required
@user_passes_test(administrativo)
def alta_inscripcion2(request,id=None):
    context ={}
    if request.method == "POST":
        form = AltaInscripcionForm2(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inscripcion dada de alta correctamente')
            return(redirect( reverse('cons_alumno') + str(id)))
        else:
            messages.add_message(request, messages.ERROR,"Por favor verifica los datos")
    else:
        val_inicial = {}
        val_inicial['alumno_id'] = Alumno.objects.get(alumno_id=int(id))
        context['alumno_id'] = Alumno.objects.get(alumno_id=int(id))
        form = AltaInscripcionForm2(initial=val_inicial)

    context['form'] = form
    return render(request, 'taller/alta_inscripcion2.html', context)

@login_required
@user_passes_test(administrativo)
def cons_turno(request, id):
    context = {}
    try:
        turno = Turno.objects.get(turno_id=id)
    except Turno.DoesNotExist:
        raise Http404('Turno inexistente')
    context['turno'] = turno

 #   form = Inscripcion.objects.filter(turno_id=id).select_related()
    listado = Inscripcion.objects.filter(turno_id=id).values( "id","alumno_id__nombre","alumno_id__apellido","alumno_id__mail").order_by("alumno_id__nombre","alumno_id__apellido")
    #.query
    context['listado'] = listado
    return render(request, 'taller/cons_turno.html', context)

@login_required
@user_passes_test(administrativo)
def baja_inscripcion(request, id, origen):
    ins = Inscripcion.objects.get(id=id)
    alumno = ins.alumno_id.alumno_id
    turno = ins.turno_id.turno_id
    ins.delete()
    if origen == 'A':
        url = reverse('cons_alumno') + str(alumno)
    else: #   if origen == 'T':
        url = reverse('cons_turno') + str(turno)
    return redirect(url) 