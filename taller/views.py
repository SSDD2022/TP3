from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'pagina' : 'taller\index.html',
              }
    return render(request,"taller\index.html",context)
# Prueba
