from django import forms
from django.core.exceptions import ValidationError
from taller.validaciones import ValMail
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

