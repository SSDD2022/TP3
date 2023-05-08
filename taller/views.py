from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from . import classes
from . import forms


# Create your views here.
def index(request):
    context = { 'pagina' : 'taller\index.html',
              }
    return render(request,"taller\index.html",context)

def galeria(request):

    destacados = []

    #momentaneo hasta tomar los datos de la BD ---------------------
    trabajos =[{'imagen':'galeria\i1.jpg','titulo':'TITULO 1','autor':'Fulano','fecha':2005,'destacado':True},{'imagen':'galeria\i2.jpg','titulo':'TITULO 2','autor':'Sultano','fecha':2010,'destacado':False},{'imagen':'galeria\i3.jpg','titulo':'TITULO 3','autor':'Mengano','fecha':2015,'destacado':False},{'imagen':'galeria\i4.jpg','titulo':'TITULO 4','autor':'Juan','fecha':2017,'destacado':True},{'imagen':'galeria\i5.jpg','titulo':'TITULO 5','autor':'Vale','fecha':2013,'destacado':True},{'imagen':'galeria\i6.jpg','titulo':'TITULO 4','autor':'Silvia','fecha':2022,'destacado':True},{'imagen':'galeria\i7.jpg','titulo':'TITULO 7','autor':'Adri','fecha':2012,'destacado':True}]
    #---------------------------------------------------------------
    
    for trabajo in trabajos:
        if trabajo["destacado"]:
            destacados.append(trabajo)

    context = {'trabajos':trabajos, 'destacados':destacados}
    
    return render(request,"taller\galeria.html",context)

def cursos(request):
    v1 = classes.Visual ("flush-headingOne","#flush-collapseOne","flush-collapseOne")
    c1 = classes.Curso(1, 'Cerámica para niños',
                ['El arte tiene importantes beneficios para los niños, jugando comparten y aprenden valores como el esfuerzo y la dedicación.',
                 'Mejora la comunicación, pueden expresarse mediante sus obras.',
                 'Impulsa la creatividad e imaginación.',
                 'Incrementan su concentración, percepción y coordinación.'
                ],
               'INFANTIL',
               'taller\img\curso-ceramica_niños2.jpg',
               True,
               v1)
    v2 = classes.Visual ("flush-headingTwo","#flush-collapseTwo","flush-collapseTwo")
    c2 = classes.Curso(2, 'Cerámica para adultos',
               ['Cuentes con experiencia o estés comenzando, un mundo de posibilidades se despliega a partir de un trozo de archilla.',
                'Objetos utilitarios como vasijas, platos, vasos, jarrones.',
                'Figuras, muñecos, accesorios para bisutería, souvenirs',
                'Obras de arte combinando formas y colores.',
                'Variedad de días y horarios'
               ],
               'ADULTO',
               'taller\img\curso-ceramica_adultos3.jpg',
               True,
               v2)
    v3 = classes.Visual ("flush-headingThree","#flush-collapseThree","flush-collapseThree")
    c3 = classes.Curso(3, 'Alfarería',
               ['Las piezas realizadas en el torno por lo común se concluyen manualmente, permitiendo todo tipo de intervención.',
                'También esta técnica permite lograr una producción artesanal en serie.',
                'Taller dirigido a adultos.',
                'Variedad de días y horarios'
               ],
               'ADULTO',
               'taller\img\curso-alfareria_adultos9.png',
               True,
               v3)
    v4 = classes.Visual ("flush-headingFour","#flush-collapseFour","flush-collapseFour")
    c4 = classes.Curso(4, 'Esmaltado',
               ['El uso de esmaltes permite crear capas brillantes y mates, traslúcidas y opacas.',
                'La manera de aplicar el producto varía según la forma de la pieza, su tamaño y también el acabado buscado.',
                'Diferentes técnicas de esmaltado (por vertido, inmersión, pincel o pistola), permiten lograr resultados únicos.',
                'Se trata de un curso avanzado para quienes quieren experimentar nuevas opciones de decoración.'
               ],
               'ADULTO',
               'taller\img\curso-esmaltado2.jpg',
               True,
               v4)
    v5 = classes.Visual ("flush-headingFive","#flush-collapseFive","flush-collapseFive")
    c5 = classes.Curso(5, 'Especialización en arte precolombino',
               ['Investigamos el arte precolombino, según el legado de diferentes culturas.',
                'Realizaban vasijas, utensilios y recipientes en general, instrumentos musicales, máscaras, juguetes, esculturas, entre otras.',
                'Se destaca la representación de la naturaleza y la veneración a los dioses.',
                'Junto con figuras hechas en arcilla terracota que solían representar a mujeres y aludían a los ritos de la fertilidad.',
                'Curso anual teórico y práctico.'
               ],
               'ADULTO',
               'taller\img\curso-arte_precolombino.jpg',
               False,
               v5)
    ListadoCursos = [ c1, c2, c3, c4, c5 ]
    context = { 'cursos': ListadoCursos}
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
               # messages.add_message(request, messages.INFO, 'Inscripción correcta')
               return redirect(reverse('cursos'))
    else:
        #GET
        inscripcion_form = forms.Inscripcion_form(initial={'cursos':id_curso})

    context = {'form': inscripcion_form}
    return render(request,'taller/inscripcion.html' ,context)

def agregar_trabajo(request):
    if request.method == 'POST':
        #POST
        agregar_trabajo_form = forms.agregar_trabajo_form(request.POST)
         # Validaciones
        if agregar_trabajo_form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Trabajo agregado a la galería Correctamente', extra_tags="mensaje_exitoso")
            return redirect(reverse('galeria'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocurrió un error')

    else:
        #GET
        agregar_trabajo_form = forms.agregar_trabajo_form()
    
    context = {'form': agregar_trabajo_form}
    return render(request, "taller/agregar_trabajo_galeria.html", context)

