from django.shortcuts import render
from . import classes

# Create your views here.
def index(request):
    context = { 'pagina' : 'taller\index.html',
              }
    return render(request,"taller\index.html",context)

def galeria(request):
    context = {}
    return render(request,"taller\galeria.html",context)

def cursos(request):
    c1 = classes.Curso('Cerámica para niños',
               'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
               'INFANTIL',
               'taller\img\curso-ceramica_niños2.jpg')
    c2 = classes.Curso('Cerámica para adultos',
               'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
               'ADULTO',
               'taller\img\curso-ceramica_adultos3.jpg')
    c3 = classes.Curso('Alfarería',
               'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
               'ADULTO',
               'taller\img\curso-alfareria_adultos9.png')
    c4 = classes.Curso('Esmaltado',
               'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
               'ADULTO',
               'taller\img\curso-esmaltado2.jpg')
    c5 = classes.Curso('Especialización en arte precolombino',
               'Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
               'ADULTO',
               'taller\img\curso-arte_precolombino.jpg')
    ListadoCursos = [ c1, c2, c3, c4, c5 ]
    context = { 'cursos': ListadoCursos}
    return render(request,"taller\cursos.html",context)
