import pandas as pd
from datetime import datetime


arhivo_excel = 'horarios.xlsx'

xls = pd.ExcelFile(f'resources/{arhivo_excel}')
nombreDeHoja = 'IEK'


df = xls.parse(nombreDeHoja,skiprows=10)

df.to_csv('resources/horarios.cvs',index=False)



def horarios_seccion_profesor(asignatura,seccion,enfasis=None):
    diccionario_horario_seccion_profesor ={
        'Seccion': None,
        'Docente': None,
        'Horarios': {
            'Lunes': None,
            'Martes': None,
            'Miercoles': None,
            'Jueves': None,
            'Viernes': None,
            'Sabado': None
        }
    }

    for index in range(len(df)):
        materia = df['Asignatura'][index]
        turno = df['Sección'][index] 
        if type(turno) == float:
            turno = 'NA'
        profesor = f'{df['Tít'][index]} {df['Nombre'][index]} {df['Apellido'][index]}'
        
        dias = diccionario_horario_seccion_profesor['Horarios']

        if ( materia == asignatura) and (turno == seccion):
            diccionario_horario_seccion_profesor['Docente'] = profesor
            diccionario_horario_seccion_profesor['Seccion'] = turno
            #almacenan nan en caso que no haya algun horario ese dia
            dias['Lunes'] = df['Lunes'][index] 
            dias['Martes'] = df['Martes'][index]
            dias['Miercoles'] = df['Miércoles'][index]
            dias['Jueves'] = df['Jueves'][index]
            dias['Viernes'] = df['Viernes'][index]
            dias['Sabado'] = df['Sábado'][index]
    
    return diccionario_horario_seccion_profesor


def string_a_datetime(fecha_str,hora):
    fecha_str_sin_dia = " ".join(fecha_str.split()[1:])
    fecha = datetime.strptime(fecha_str_sin_dia, "%d/%m/%y")
    fecha_completa = datetime.combine(fecha, hora)
    return fecha_completa

def secciones_por_asignatura(asignatura):
    secciones = []
    for index in range(len(df)):
        if df['Asignatura'][index] == asignatura:
            secciones.append(df['Sección'][index])
    
    return secciones



dato = df['Hora.1'][0]
print(type(dato))