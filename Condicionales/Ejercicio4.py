print('Programa que comprueba si año es bisiesto o no')
anio = int(input('Introduzca el año que quiere comprobar: '))
 
if anio % 4 != 0: #no divisible entre 4
    print('El año',anio,'no es bisiesto')
elif anio % 4 == 0 and anio % 100 != 0: #divisible entre 4 y no entre 100 o 400
    print('El año',anio,'es bisiesto')
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: #divisible entre 4 y 10 y no entre 400
    print('El año',anio,'no es bisiesto')
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: #divisible entre 4, 100 y 400
    print('El año',anio,'es bisiesto')