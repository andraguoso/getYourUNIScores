#tercer examen
print('---CALCULA TU PUNTAJE DEL TERCER EXAMEN UNI---')
print('Física: ')
print('¿Cuántas buenas?: ')
buenasF = int(input('> '))
print('¿Cuántas malas?: ')
malasF = int(input('> '))
puntajeF = buenasF * 15 - malasF * 3
print(f'Hasta el momento, en Física tienes: {puntajeF}')
print('Química: ')
print('¿Cuántas buenas?: ')
buenasQ = int(input('> '))
print('¿Cuántas malas?: ')
malasQ = int(input('> '))
puntajeQ = buenasQ * 10 - malasQ * 2
print(f'En Química, tienes {puntajeQ}')
puntajeTotal = puntajeF + puntajeQ
print(f'En total, tienes {puntajeTotal}')
puntajeEFD20 = (puntajeTotal/500)*20
if puntajeTotal >= 250:
    print('¡Aprobaste!')
    print(f'Sacaste {puntajeEFD20} de 20')
else:
    print('Desaprobaste')
    print(f'Sacaste {puntajeEFD20} de 20')