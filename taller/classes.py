
class Visual ():
     def __init__ (self,fheadingX,fcollapseCX,fcollapseX):
        self.fheadingX = fheadingX     # "flush-headingOne"
        self.fcollapseCX = fcollapseCX # "#flush-collapseOne"
        self.fcollapseX = fcollapseX   # "flush-collapseOne"

class CursoOld ():
    def __init__ (self,id,titulo,descripcion,imagen,cupo,visual):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
#        self.tipo_participante = tipo_participante
        self.imagen = imagen
        self.cupo = cupo
        self.visual = visual