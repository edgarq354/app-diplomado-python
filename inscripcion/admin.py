from django.contrib import admin

from .models import Estudiante, Curso, Costo, Inscripcion

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Costo)

# Clase personalizada para Inscripcion
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'costo', 'fecha_inscripcion', 'pagado')
    ordering = ('-fecha_inscripcion',)
    search_fields = ('estudiante__nombres', 'estudiante__apellidos', 'curso__nombre')
    list_filter = ('pagado', 'curso')

admin.site.register(Inscripcion, InscripcionAdmin)

