from django import forms
from django.core.exceptions import ValidationError

CURSOS = ((1, 'Cerámica para niños'),
                  (2, 'Cerámica para adultos'),
                  (3, 'Alfarería'),
                  (4, 'Esmaltado'), 
                  (5, 'Especialización en arte precolombino'))
class Inscripcion_form(forms.Form): 
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
    curso = forms.ChoiceField(choices=CURSOS,)
