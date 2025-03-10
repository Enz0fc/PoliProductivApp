from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
class Profesor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return self.nombre
class Seccion(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='secciones')
    nombre = models.CharField(max_length=5)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.materia} - {self.nombre}"
class Horario(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='horarios')
    dia_semana = models.CharField(max_length=10, choices=[
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo')
    ])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.seccion} - {self.dia_semana} {self.hora_inicio}-{self.hora_fin}"
class Evaluacion(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='evaluaciones')
    nombre = models.CharField(max_length=50, choices=[
        ('Primer Parcial', 'Primer Parcial'),
        ('Segundo Parcial', 'Segundo Parcial'),
        ('Primer Final', 'Primer Final'),
        ('Segundo Final', 'Segundo Final')
    ])
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.seccion} - {self.nombre} ({self.fecha})"
