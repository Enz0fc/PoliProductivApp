from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()
    seccion = models.CharField(max_length=5)
    profesor = models.CharField(max_length=100)
    primer_parcial = models.DateTimeField(null=True,blank=True)
    segundo_parcial = models.DateTimeField(null=True,blank=True)
    primer_final = models.DateTimeField(null=True,blank=True)
    segundo_final = models.DateTimeField(null=True,blank=True)
    horario_semanal = models.JSONField(default=dict)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return "{self.nombre} {self.seccion}"