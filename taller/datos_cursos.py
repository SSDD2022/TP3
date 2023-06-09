from django.test import TestCase
from taller.models import Curso, CursoDescripcion

# Create your tests here.
# Carga de datos de cursos
# 1er curso
c = Curso(curso_id = 1, titulo='Cerámica para niños',imagen='curso-ceramica_niños2.jpg')
c.save()
cursillo = Curso.objects.get(curso_id=1) 
cd= CursoDescripcion (curso_id = cursillo, posicion_id=1,
                      descripcion='El arte tiene importantes beneficios para los niños, jugando comparten y aprenden valores como el esfuerzo y la dedicación.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=2,
                             descripcion='Mejora la comunicación, pueden expresarse mediante sus obras.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=3,
                             descripcion='Impulsa la creatividad e imaginación.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=4,
                             descripcion='Incrementan su concentración, percepción y coordinación.')
cd.save()
# 2do curso
c = Curso(curso_id = 2, titulo='Cerámica para adultos',imagen='curso-ceramica_adultos3.jpg')
c.save()
cursillo = Curso.objects.get(curso_id=2) 
cd= CursoDescripcion (curso_id = cursillo, posicion_id=1,
                             descripcion='Cuentes con experiencia o estés comenzando, un mundo de posibilidades se despliega a partir de un trozo de archilla.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=2,
                             descripcion='Objetos utilitarios como vasijas, platos, vasos, jarrones.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=3,
                             descripcion='Figuras, muñecos, accesorios para bisutería, souvenirs')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=4,
                             descripcion='Obras de arte combinando formas y colores.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=5,
                             descripcion='Variedad de días y horarios')
cd.save()
# 3er curso
c = Curso(curso_id = 3, titulo='Alfarería',imagen='curso-alfareria_adultos9.png')
c.save()
cursillo = Curso.objects.get(curso_id=3) 
cd= CursoDescripcion (curso_id = cursillo, posicion_id=1,
                             descripcion='Las piezas realizadas en el torno por lo común se concluyen manualmente, permitiendo todo tipo de intervención.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=2,
                             descripcion='También esta técnica permite lograr una producción artesanal en serie.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=3,
                             descripcion='Taller dirigido a adultos.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=4,
                             descripcion='Variedad de días y horarios.')
cd.save()
# 4to curso
c = Curso(curso_id = 4, titulo='Esmaltado',imagen='curso-esmaltado2.jpg')
c.save()
cursillo = Curso.objects.get(curso_id=4) 
cd= CursoDescripcion (curso_id = cursillo, posicion_id=1,
                             descripcion='El uso de esmaltes permite crear capas brillantes y mates, traslúcidas y opacas.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=2,
                             descripcion='La manera de aplicar el producto varía según la forma de la pieza, su tamaño y también el acabado buscado.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=3,
                             descripcion='Diferentes técnicas de esmaltado (por vertido, inmersión, pincel o pistola), permiten lograr resultados únicos.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=4,
                             descripcion='Se trata de un curso avanzado para quienes quieren experimentar nuevas opciones de decoración.')
cd.save()
# 5to curso
c = Curso(curso_id = 5, titulo='Especialización en arte precolombino',imagen='curso-arte_precolombino.jpg')
c.save()
cursillo = Curso.objects.get(curso_id=5) 
cd= CursoDescripcion (curso_id = cursillo, posicion_id=1,
                             descripcion='Investigamos el arte precolombino, según el legado de diferentes culturas.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=2,
                             descripcion='Realizaban vasijas, utensilios y recipientes en general, instrumentos musicales, máscaras, juguetes, esculturas, entre otras.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=3,
                             descripcion='Se destaca la representación de la naturaleza y la veneración a los dioses.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=4,
                             descripcion='Junto con figuras hechas en arcilla terracota que solían representar a mujeres y aludían a los ritos de la fertilidad.')
cd.save()
cd= CursoDescripcion (curso_id = cursillo, posicion_id=5,
                             descripcion='Curso anual teórico y práctico.')
cd.save()

