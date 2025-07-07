from itertools import product

from rest_framework import serializers

from .models import Estudiante, Curso, Costo, Inscripcion
from .validators import validar_nombre


# SERIALIZER ESTUDIANTE
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


# SERIALIZER CURSO
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


# SERIALIZER COSTO
class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = '__all__'


# SERIALIZER INSCRIPCION
class InscripcionSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer(read_only=True)
    curso = CursoSerializer(read_only=True)
    costo = CostoSerializer(read_only=True)

    estudiante_id = serializers.PrimaryKeyRelatedField(
        queryset=Estudiante.objects.all(), source='estudiante', write_only=True
    )
    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), source='curso', write_only=True
    )
    costo_id = serializers.PrimaryKeyRelatedField(
        queryset=Costo.objects.all(), source='costo', write_only=True, allow_null=True, required=False
    )

    class Meta:
        model = Inscripcion
        fields = [
            'id',
            'estudiante',
            'curso',
            'costo',
            'fecha_inscripcion',
            'pagado',
            'estudiante_id',
            'curso_id',
            'costo_id',
        ]


