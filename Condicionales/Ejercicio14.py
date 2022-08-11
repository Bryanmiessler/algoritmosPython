num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if num1 < num2 and num2 < num3:
    print(num2,'es el numero que se encuentra en medio')
elif num3 < num2 and num2 < num1:
    print(num2, 'es el numero que se encuentra en medio')
elif num2 < num1 and num1 < num3:
    print(num1,'es el numero que se encuentra en medio')
elif num3 < num1 and num1 < num2:
    print(num1,'es el numero que se encuentra en medio')
elif num2 < num3 and num3 < num1:
    print(num3,'es el numero que se encuentra en medio')
elif num1 < num3 and num3 < num2:
    print(num3,'es el numero que se encuentra en medio')
else:
    print('Los numeros son iguales')
