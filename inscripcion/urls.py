from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'inscripciones', views.EstudianteViewSet)

urlpatterns = [ 

    path('inscripcion/', views.EstudianteCreateView.as_view(), name='inscripcion-create-list'),
    path('estudiantes/cantidad/', views.estudiante_count, name='estudiantes-count'),
    #path('inscripcion/filtrar/nombre/', views.inscripcion_en_nombre, name='inscripcion-unidades'),
    #path('reporte/inscripcion/', views.reporte_inscripciones, name='reporte-inscripcion'),
    path('enviar/mensaje/', views.enviar_mensaje, name='enviar-mensaje'),
    path('', include(router.urls)),
]
