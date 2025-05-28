#segundo examen
print('---CALCULA TU PUNTAJE EN EL SEGUNDO EXAMEN UNI---')
print('Matemáticas: ')
print('¿Cuántas buenas?: ')
buenasM = int(input('> '))
print('¿Cuántas malas?: ')
malasM = int(input('> '))
puntajeM = buenasM * 15 - malasM * 3
print(f'Tu puntaje es: {puntajeM}')
puntajeEFD20 = (puntajeM/600)*20
if puntajeM >= 300:
    print('¡Aprobaste!')
    print(f'Sacaste {puntajeEFD20} de 20')
else:
    print('No aprobaste')
    print(f'Sacaste {puntajeEFD20} de 20')