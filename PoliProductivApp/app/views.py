from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Carrera, Materia
import json

def index(request):
    carreras = Carrera.objects.all()
    return render(request, 'app/index.html', {'carreras': carreras})

def get_semestres(request):
    carrera_id = request.GET.get('carrera_id')
    semestres = Materia.objects.filter(carrera=carrera_id).values_list('nivel',flat=True)
    return JsonResponse(list(set(semestres)), safe=False)

def get_materias(request):
    semestre_id = list(request.GET.get('semestre_ids'))
    for x in semestre_id:
        if x==',':
            semestre_id.remove(x)

    carrera_id = request.GET.get('carrera_id')
    materias = Materia.objects.filter(nivel__in=semestre_id, carrera=carrera_id).values('nombre').distinct()
    return JsonResponse(list(materias), safe=False)

def get_secciones(request):
    materia_id = request.GET.get('materia_id')
    carrera_id = request.GET.get('carrera_id')
    secciones = Materia.objects.filter(carrera=carrera_id,nombre=materia_id).values('nombre','seccion').distinct()
    return JsonResponse(list(secciones), safe=False)