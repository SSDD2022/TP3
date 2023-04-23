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
                ['El arte tiene importantes beneficios para los niños, jugando comparten y aprenden valores como el esfuerzo y la dedicación.',
                 'Mejora de la comunicación, pueden expresarse mediante sus obras.',
                 'Impulsa la creatividad e imaginación.',
                 'Incrementan su concentración, percepción y coordinación.'
                ],
               'INFANTIL',
               'taller\img\curso-ceramica_niños2.jpg',
               True)
    c2 = classes.Curso('Cerámica para adultos',
               ['Cuentes con experiencia o estés comenzando, un mundo de posibilidades se despliega a partir de un trozo de archilla.',
                'Objetos utilitarios como vasijas, platos, vasos, jarrones.',
                'Figuras, muñecos, accesorios para bisutería, souvenirs',
                'Obras de arte combinando formas y colores.',
                'Variedad de días y horarios'
               ],
               'ADULTO',
               'taller\img\curso-ceramica_adultos3.jpg',
               True)
    c3 = classes.Curso('Alfarería',
               ['Las piezas realizadas en el torno comúnmente son concluidas manualmente, permitiendo todo tipo de intervención.',
                'También esta técnica permite lograr una producción artesanal en serie',
                'Taller dirigido a adultos.',
                'Variedad de días y horarios'
               ],
               'ADULTO',
               'taller\img\curso-alfareria_adultos9.png',
               True)
    c4 = classes.Curso('Esmaltado',
               ['El uso de esmaltes permite crear capas brillantes y mates, traslúcidas y opacas.',
                'La manera de aplicar el producto varía según la forma de la pieza, su tamaño y también el acabado buscado.',
                'Diferentes técnicas de esmaltado (por vertido, inmersión, pincel o pistola), permiten lograr resultados únicos.',
                'Se trata de un curso avanzado para quienes quieren experimentar nuevas opciones de texturas y colores.'
               ],
               'ADULTO',
               'taller\img\curso-esmaltado2.jpg',
               True)
    c5 = classes.Curso('Especialización en arte precolombino',
               ['Investigamos el arte precolombino, desarrollado con materiales y herramientas disponibles en el entorno de las regiones en las que vivían las diferentes culturas.',
                'Realizaban vasijas, utensilios y recipientes en general, instrumentos musicales, máscaras, juguetes, esculturas, entre otras.',
                'Se destaca la representación de la naturaleza y la veneración a los dioses.',
                'Junto con figuras hechas en arcilla terracota que solían representar a mujeres y aludían a los ritos de la fertilidad.',
                'Curso anual teórico y práctico.'
               ],
               'ADULTO',
               'taller\img\curso-arte_precolombino.jpg',
               False)
    ListadoCursos = [ c1, c2, c3, c4, c5 ]
    context = { 'cursos': ListadoCursos}
    return render(request,"taller\cursos.html",context)
