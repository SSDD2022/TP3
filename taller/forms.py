from django import forms

class Inscripcion_form(forms.Form):
    CURSOS = ['Cerámica para niños', 'Cerámica para adultos', 'Alfarería', 'Esmaltado', 'Especialización en arte precolombino']
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email", required=True)
    dni = forms.CharField(label="Numero de Documento", required=True, widget=forms.NumberInput())
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", required=True, widget=forms.SelectDateWidget(years=range(1930,2023)))
    telefono = forms.CharField(widget=forms.NumberInput(),label="Numero de Telefono", required=True) 
    cursos = forms.MultipleChoiceField(required=False,  widget=forms.CheckboxSelectMultiple(choices = CURSOS))
