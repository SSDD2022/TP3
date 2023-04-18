from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'pagina' : 'taller\index.html',
              }
    return render(request,"taller\index.html",context)

def galeria(request):
    context = {}
    return render(request,"taller\galeria.html",context)

def cursos(request):
    context = {}
    return render(request,"taller\cursos.html",context)
