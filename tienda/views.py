from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'pagina' : 'tienda\index.html',
              }
    return render(request,"tienda\index.html",context)
