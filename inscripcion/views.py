from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view

from .forms import InscripcionForm
from .models import Estudiante, Curso, Costo
from .serializers import (EstudianteSerializer, CostoSerializer)


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def estudiantes(request):
    post_nombre = request.POST.get('nombres')
    if post_nombre:
        q = Estudiante(nombres=post_nombre)
        q.save()

    filtro_nombre = request.GET.get('nombres')
    # import pdb; pdb.set_trace()

    if filtro_nombre:
        estudiantes = Estudiante.objects.filter(nombre__contains=filtro_nombre)
    else:
        estudiantes = Estudiante.objects.all()

    return render(request, 'form_estudiantes.html', {
        "estudiantes": estudiantes
    })

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class EstudianteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

@api_view(['GET'])
def estudiante_count(request):
    try:
        cantidad = Estudiante.objects.count()
        return JsonResponse({
                'cantidad': cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)



#CURSO
def costos(request):
    post_nombre = request.POST.get('tipo')
    if post_nombre:
        q = Costo(tipo=post_nombre)
        q.save()

    filtro_nombre = request.GET.get('tipo')
    # import pdb; pdb.set_trace()

    if filtro_nombre:
        costos = Costo.objects.filter(nombre__contains=filtro_nombre)
    else:
        costos = Costo.objects.all()

    return render(request, 'form_costos.html', {
        "estudiantes": costos
    })

class CostoViewSet(viewsets.ModelViewSet):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer


class CostoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer

@api_view(['GET'])
def estudiante_count(request):
    try:
        cantidad = Estudiante.objects.count()
        return JsonResponse({
                'cantidad': cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)



  

@api_view(['POST'])
def enviar_mensaje(request):
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({'message': 'Mensaje enviado correctamente'},
                            status=200)
    else:
        return JsonResponse({'message': cs.errors}, status=200)
