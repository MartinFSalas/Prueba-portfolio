#a) Diferencia de porcentaje entre el curso actual y:
#El mas rapido de otros cursos
#El mas lento de otros cursos
#El promedio de los cursos

otros_cursos_min = 2.5

otros_cursos_prom = 4

otros_cursos_max = 7

curso_actual = 1.5

#Diferencias de duración

diferencia_con_min = 100 - curso_actual / otros_cursos_min * 100

diferencia_con_prom = 100 - curso_actual / otros_cursos_prom * 100

diferencia_con_max = 100 - curso_actual / otros_cursos_max * 100

#b) Porcentaje de material inservible que se reduce en:
#El promedio de los cursos
#El curso actual 

otros_cursos_crudo = 5

curso_actual_crudo = 3.5

#Material inservible en porcentaje

material_inservible_otros_cursos = 100 - otros_cursos_prom / otros_cursos_crudo * 100

material_inservible_curso_actual = 100 - curso_actual / otros_cursos_crudo * 100

#c) Ver 10 horas de este curso, a cuantas horas de otros cursos equivale? y al reves?

horas_curso_actual = 10

horas_otros_cursos = 10

equivalencia_curso_min = horas_curso_actual * curso_actual / otros_cursos_min

equivalencia_curso_prom = horas_curso_actual * curso_actual / otros_cursos_prom

equivalencia_curso_max = horas_curso_actual * curso_actual / otros_cursos_max

#Porcentajes

print(f"La diferencia en porcentaje del curso actual con el minimo es de: {diferencia_con_min} %")
print(f"La diferencia en porcentaje del curso actual con el promedio es de: {diferencia_con_prom} %")
print(f"La diferencia en porcentaje del curso actual con el maximo es de: {diferencia_con_max} %")
print(f"El material inservible de otros cursos es:  {material_inservible_otros_cursos} %")
print(f"El material inservible de este curso es:  {material_inservible_curso_actual} %")

print(equivalencia_curso_max)