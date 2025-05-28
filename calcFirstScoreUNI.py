#primer examen
import time
print('---CALCULA TU PUNTAJE EN EL PRIMER EXAMEN UNI---')
print('Aptitud académica:')
print('¿Cuántas buenas de AA?: ')
buenasAA = int(input('> '))
print('¿Cuántas malas?: ')
malasAA =int(input('> '))
puntajeAA = buenasAA * 8 - malasAA * 1.6
print(f'Hasta el momento, en AA tienes: {puntajeAA}')
print('Humanidades:')
print('¿Cuántas buenas de H?: ')
buenasH = int(input('> '))
print('¿Cuántas malas?: ')
malasH = int(input('> '))
puntajeH = buenasH * 5.8 - malasH * 1.16
print(f'En Humanidades tienes : {puntajeH}')
puntajeTotal = puntajeAA + puntajeH
print(f'En total, en el primer examen UNI tienes: {puntajeTotal}')
puntajeEnFuncionDe20 = (puntajeTotal/745)*20
if puntajeTotal >= 320:
    print('¡Aprobaste!')
    print(f'Sacaste: {puntajeEnFuncionDe20} de 20')
else:
    print('No aprobaste, pero puedes remontar')
    print(f'Sacaste: {puntajeEnFuncionDe20} de 20')