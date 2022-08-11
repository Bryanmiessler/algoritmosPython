edad = int(input('Ingrese edad: '))
 
if edad == 0 or edad == 1:
    print('Es bebe')
elif edad >= 2 and edad <= 10:
    print('Es niño')
elif edad >= 11 and edad <= 15:
    print('Es adolescente')
elif edad >= 16 and edad <= 25:
    print('Es joven')
elif edad >= 26 and edad <= 75:
    print('Es adulto')
elif edad >= 76 and edad <= 100:
    print('Es anciano')
elif edad >= 101 and edad <= 120:
    print('Es longevo')
elif edad > 120:
    print('Es muy longevo')
elif edad < 0:
    print('Fuera de rango')