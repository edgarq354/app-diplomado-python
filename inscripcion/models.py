import uuid

from django.db import models

from .validators import validar_par


# MODELO ESTUDIANTE
class Estudiante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True) 

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

# MODELO COSTOS
class Costo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f'{self.monto} - {self.tipo}'


# MODELO CURSO
class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    duracion_horas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


# MODELO INSCRIPCIÓN
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    costo = models.ForeignKey(Costo, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f'{self.estudiante} - {self.curso}'
