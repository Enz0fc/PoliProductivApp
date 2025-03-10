from django.contrib import admin
from .models import Carrera, Materia, Profesor, Seccion, Horario, Evaluacion

admin.site.register(Carrera)
admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Seccion)
admin.site.register(Horario)
admin.site.register(Evaluacion)