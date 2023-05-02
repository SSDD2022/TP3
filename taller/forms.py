from django import forms

TYPE_CHOICES = [
    ("Cerámica para niños"),
    ("Cerámica para adultos"),
    ("Alfarería"),
    ("Esmaltado"),
    ("Especialización Arte Precolombino"),
]

class Inscripcion_form(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email", required=True)

class agregar_trabajo_form(forms.Form):
    imagen = forms.FileField(label = "imagen", required=True)
    titulo = forms.CharField(label="Título", required=True)
    autor = forms.CharField(label="Autor", required=True)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #curso = forms.ChoiceField(choices=TYPE_CHOICES,)
