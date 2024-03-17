import os
from django.conf import settings
import pandas as panditas
from .models import Alumno


class CargaAlumno():
    
    def carga_de_informacion(self, archivo):
        df = panditas.read_excel(archivo)
        for indice, fila in df.iterrows():
            horas_year = {}
            datos = []
            for nombre_columna, valor in fila.items():
                if 'hora' in nombre_columna.lower():
                    if panditas.isna(valor):
                        horas_year[nombre_columna] = 0
                    else:
                        horas_year[nombre_columna] = valor
                else:
                    if panditas.isna(valor):
                        datos.append('')
                    else:
                        datos.append(valor)
            if Alumno.objects.filter(rut=datos[0]).exists():
                alumno_tmp = Alumno.objects.get(rut=datos[0])
                if horas_year == alumno_tmp.horas_year:
                    pass
                else:
                    diccionario = alumno_tmp.horas_year
                    diccionario.update(horas_year)
                    alumno_tmp.horas_year = diccionario
                    alumno_tmp.save()
            else:
                alumno_nuevo = Alumno(
                                    rut=datos[0],
                                    nombre=datos[1],
                                    facultad=datos[2],
                                    carrera=datos[3],
                                    horas_year=horas_year,
                                    creditos=datos[4])
                alumno_nuevo.save()
        