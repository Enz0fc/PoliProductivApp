from django.core.management.base import BaseCommand, CommandError
from app.models import Carrera,Materia

import pandas as pd
from datetime import datetime
import json 

def string_a_datetime(fecha_str,hora_entrada):
    hora = hora_entrada if not isinstance(hora_entrada,(float,str)) else None
    fecha_str_sin_dia = fecha_str[-8:] if isinstance(fecha_str,str) else None
    fecha = datetime.strptime(fecha_str_sin_dia, "%d/%m/%y") if isinstance(fecha_str_sin_dia,str) else None
    
    if fecha and hora:
        return datetime.combine(fecha, hora) 


def cargar_datos(ruta):
    try:
        archivo_excel = pd.ExcelFile(ruta)
    except:
        print('Ha ocurrido un error')
        return 'Error'
    hojas = archivo_excel.sheet_names[1:16]
    for hoja in hojas:
        asignatura, created = Carrera.objects.get_or_create(nombre=hoja)
        
        df = archivo_excel.parse(hoja,skiprows=10)
        for index, fila in df.iterrows():
            
            horario = {
                'Lunes': fila['Lunes'].strip().split(' - ') if isinstance(fila['Lunes'],str) else '',
                'Martes': fila['Martes'].strip().split(' - ') if isinstance(fila['Martes'],str) else '',
                'Miércoles': fila['Miércoles'].strip().split(' - ') if isinstance(fila['Miércoles'],str) else '',
                'Jueves': fila['Jueves'].strip().split(' - ') if isinstance(fila['Jueves'],str) else '',
                'Viernes': fila['Viernes'].strip().split(' - ') if isinstance(fila['Viernes'],str) else '',
                'Sábado': fila['Sábado'].strip().split(' - ') if isinstance(fila['Sábado'],str) else ''
                }
            
            Materia.objects.create(
                nombre = fila['Asignatura'],
                nivel = fila['Sem/Grupo'] if isinstance(fila['Sem/Grupo'],int) else fila['Nivel'] if isinstance(fila['Nivel'],int) else 0,
                seccion = fila['Sección'],
                profesor = f'{fila['Tít']} {fila['Nombre']} {fila['Apellido']}',
                primer_parcial = string_a_datetime(fila['Día'],fila['Hora']), 
                segundo_parcial = string_a_datetime(fila['Día.1'],fila['Hora.1']), 
                primer_final = string_a_datetime(fila['Día.2'],fila['Hora.2']),
                segundo_final = string_a_datetime(fila['Día.4'],fila['Hora.4']),
                horario_semanal = json.dumps(horario),
                carrera = asignatura
            )
    print('Datos creados correctamente')

class Command(BaseCommand):
    help = 'Carga datos iniciales en la base de datos'

    def add_arguments(self, parser):
        # Define un argumento llamado 'archivo'
        parser.add_argument('archivo', type=str, help='Ruta al archivo Excel')
    
    def handle(self, *args, **kwargs):
        ruta =  kwargs['archivo']
        try:
            cargar_datos(ruta)
        except FileNotFoundError:
            raise CommandError(f'El archivo "{ruta}" no existe.')
        '''except Exception as e:
            raise CommandError(f'Error al cargar los datos: {e}')'''
