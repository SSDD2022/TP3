from rest_framework import serializers
from .models import Curso, CursoDescripcion

class CursoSerializer(serializers.ModelSerializer):
    descripciones = serializers.StringRelatedField(many=True)  # es related en models.CursoDescripcion

    class Meta:
        model = Curso
        fields = ['curso_id','titulo','descripciones']


class CursoDescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoDescripcion
        fields = ['posicion_id','descripcion']

class CursoSerializer2(serializers.ModelSerializer):
    descripciones = CursoDescripcionSerializer(many=True, read_only=True)  # es related en models.CursoDescripcion

    class Meta:
        model = Curso
        fields = ['curso_id','titulo','descripciones']
