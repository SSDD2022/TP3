from django import utils
import re

# Validaciones

def ValMail (mail):
    EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if mail and not re.match(EMAIL_REGEX, mail):
         return False
    return True
 
def ValCelular (celular):
    AREA_PARENTESIS_Y_NRO = r"(^\([1-9]{1,1}[0-9]{1,3}\) [1-9]{1,1}[0-9]{7,7}+$)"
    AREA_Y_NRO = r"(^[1-9]{1,1}[0-9]{1,3} [1-9]{1,1}[0-9]{7,7}+$)"
    NRO = r"(^[1-9]{1,1}[0-9]{7,7}+$)"
    if celular and \
       not (re.match(AREA_PARENTESIS_Y_NRO, celular) or re.match(AREA_Y_NRO, celular) or re.match(NRO, celular)):
         return False
    return True

def ValEdadGrupo (grupo,fecha_nacimiento):
     edad = utils.timezone.now().year - fecha_nacimiento.year
     if grupo == 'N':
          # Niños
          return edad >= 8 and edad < 13
     if grupo == 'J':
          # Jóvenes
          return edad >= 13 and edad < 19
     if grupo == 'A':
          # Adultos
          return edad >= 20
     return False

def ValEdadAlumno (fecha_nacimiento):
     return ValEdadGrupo('N', fecha_nacimiento)
