from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from . import classes
from . import forms
from taller.models import Curso, CursoDescripcion, Trabajo, Contacto


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
                             'taller/img/' + c.imagen,True,v)
        descripcioncilla = CursoDescripcion.objects.filter(curso_id=c.curso_id).order_by('posicion_id')
        for desc in descripcioncilla.all():
            x.descripcion.append(desc.descripcion)
        ListadoCursos.append(x)
    ListadoCursos[4].cupo = False

    context = { 'cursos': ListadoCursos }
    return render(request,"taller/cursos.html",context)

def alumnos(request):
    context = { 'pagina' : 'taller/alumnos.html',
              }
    return render(request,'taller/alumnos.html',context)

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

def agregar_trabajo(request):
    if request.method == 'POST':
        #POST
        agregar_trabajo_form = forms.agregar_trabajo_form(request.POST, request.FILES)
         # Validaciones
        if agregar_trabajo_form.is_valid():
            nuevo_trabajo = Trabajo(
                titulo=agregar_trabajo_form.cleaned_data['titulo'], 
                autor=agregar_trabajo_form.cleaned_data['autor'], 
                imagen=agregar_trabajo_form.cleaned_data['imagen']
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
            if motivo == 'SUG':
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
