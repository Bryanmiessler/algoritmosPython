operador = input('Introduzca un operador aritmetico: ')
num1 = int(input('Introduzca el primer numero: '))
num2 = int(input('Introduzca el segundo numero: '))

if operador == '+':
    resultado = num1 + num2
    print('Usando el operador',operador,'el resultado sería: ',resultado)
elif operador == '-':
    resultado = num1 - num2
    print('Usando el operador',operador,'el resultado sería: ',resultado)
elif operador == '*':
    resultado = num1 * num2
    print('Usando el operador',operador,'el resultado sería: ',resultado)
elif operador == '/':
    resultado = num1 / num2
    print('Usando el operador',operador,'el resultado sería: ',resultado)
elif operador == '%':
    resultado = num1 % num2
    print('Usando el operador',operador,'el resultado sería: ',resultado)
else:
    print('Introduzca un operador válido')
    
