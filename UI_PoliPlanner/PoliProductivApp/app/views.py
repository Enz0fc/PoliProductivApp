from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Carrera, Materia
import json
datos = {}
def index(request):
    carreras = Carrera.objects.all()
    semestres = list(range(1,11))
    
    
        
    
    context = {
        'carreras': carreras,
        'semestres':semestres,
    }
    
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Convertir el cuerpo de la petición a JSON
            datos.update(data)
            return JsonResponse({"mensaje": "Datos recibidos", "data": datos})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    
    return render(request,'app/index.html',context)

def actualizar_contexto(request):
    if request.method == 'POST':
        contexto_nuevo ={
            'materias': list(Materia.objects.filter(nivel__in=datos['semestres'], carrera=int(datos['carrera'])).values_list('nombre', flat=True))
        }
        
        
        nuevoDiv = render_to_string('app/paso3.html',contexto_nuevo)
        print("Nuevo div:",nuevoDiv)
        return JsonResponse({'nuevoDiv': nuevoDiv})
