from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.conf import settings
from django import utils
from taller.validaciones import ValMail, ValCelular, ValEdadAlumno 
from taller.models import Alumno, Turno, Curso
import re


class Inscripcion_form(forms.Form):
        CURSOS = ((1, 'Cerámica para niños'),
                  (2, 'Cerámica para adultos'),
                  (3, 'Alfarería'),
                  (4, 'Esmaltado'), 
                  (5, 'Especialización en arte precolombino'))
        nombre = forms.CharField(label="Nombre", required=True)
        apellido = forms.CharField(label="Apellido", required=True)
        mail = forms.EmailField(label="Email", required=True)
        dni = forms.CharField(label="Numero de Documento", required=True, widget=forms.NumberInput())
        fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", required=True, widget=forms.SelectDateWidget(years=range(1930,2023)))
        telefono = forms.CharField(widget=forms.NumberInput(),label="Numero de Telefono", required=True) 
        cursos = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = CURSOS, required=False)
        def clean_cursos (self):
             data = self.cleaned_data["cursos"]
             if len(data) == 0:
                 raise ValidationError ( 'Por favor seleccioná un curso ...')


class agregar_trabajo_form(forms.Form):
    imagen = forms.FileField(label="imagen", required=True)
    titulo = forms.CharField(label="Título", required=True)
    autor = forms.CharField(label="Autor", required=True)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #curso = forms.ChoiceField(choices=TYPE_CHOICES,)

class Contacto(forms.Form):
    MOTIVOS = (('SUG', 'Sugerencia'),
               ('CON', 'Consulta'),
               ('SUS', 'Suscripción')
              )    
    motivo = forms.ChoiceField(choices = MOTIVOS, required=True) 
    nombre = forms.CharField(max_length=30,label="Nombre", required=True)
    apellido = forms.CharField(max_length=50,label="Apellido", required=True)
    mail = forms.EmailField(max_length=30,label="Email", required=True)
    comentario = forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":"5"}),required=False)
    def clean_mail (self):
        mail = self.cleaned_data["mail"]
        if mail and not ValMail(mail):
            error_dict = { 'mail': 'Mail inválido' }
            raise forms.ValidationError (error_dict)
        return self.cleaned_data.get('mail')
    def clean (self):
        motivo = self.cleaned_data["motivo"]
        comentario = self.cleaned_data["comentario"]
        if motivo != 'SUS' and len(comentario) == 0:
#          self.fields['comentario'].widget.attrs['placeholder'] = 'Por favor completa el comentario ...'
            error_dict = { 'comentario': 'Ingresa el comentario' }
            raise forms.ValidationError (error_dict)
        return self.cleaned_data

class AltaAlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields=["nombre","apellido","fecha_nacimiento","mail","celular"]
        widgets = { "fecha_nacimiento" : forms.DateInput(format='%d-%m-%Y', attrs={'class':'form-control', 'placeholder':'Fecha de nacimiento', 'type':'date'}),
                  }
    def clean_mail (self):
        mail = self.cleaned_data["mail"]
        if not mail or not ValMail(mail):
            raise forms.ValidationError ('Mail inválido')
        return self.cleaned_data.get('mail')  
    def clean_celular (self):
        celular = self.cleaned_data["celular"]
        if not celular or not ValCelular(celular):
            raise forms.ValidationError ('Formato: (11) 11111111')
        return self.cleaned_data.get('celular')
    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data["fecha_nacimiento"]
        if not fecha or not ValEdadAlumno (fecha):
            raise forms.ValidationError ('Aún no tiene 8 años')
        return self.cleaned_data.get('fecha_nacimiento')        

class AltaTurnoForm(forms.ModelForm):
    class Meta:
        model=Turno
        exclude=["turno_id","alumnos"]
        fields = ["curso_id", "descripción", "anio", "destinatario", "experiencia", "cupo"]

    def clean_cupo(self):
        cupo = self.cleaned_data["cupo"]
        if not cupo or cupo <= 0:
            raise forms.ValidationError ('El cupo es positivo')
        return self.cleaned_data.get('cupo')
    def clean_anio(self):
        anio = self.cleaned_data["anio"]
        if not anio or anio < utils.timezone.now().year:
            raise forms.ValidationError ('Año actual o futuro') 
        return self.cleaned_data.get('anio')  

  

        



         