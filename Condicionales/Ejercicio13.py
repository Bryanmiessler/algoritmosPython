ordenamiento = input('ingrese el tipo de ordenamiento que desea(ascendente o descendente): ')
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))


if ordenamiento == 'ascendente':
    if num1 > num2 and num2 > num3:
        print(num3,num2,num1)
    elif num1 > num3 and num3 > num2:
        print(num2,num3,num1)
    elif num2 > num1 and num1 > num3:
        print(num3,num1,num2)
    elif num2 > num3 and num3 > num1:
        print(num1,num3,num2)
    elif num3 > num2 and num2 > num1:
        print(num1,num2,num3)
    elif num3 > num1 and num1 > num2:
        print(num2,num1,num3)
    elif num3 == num1 and num1 > num2:
        print(num2,num1,num3)
    elif num3 == num2 and num2 > num1:
        print(num1,num2,num3)
    elif num2 == num1 and num1 > num3:
        print(num3,num1,num2)
    elif num2 == num3 and num3 > num1:
        print(num1,num3,num2)
    elif num1 == num2 and num2 > num3:
        print(num3,num2,num1)
    elif num1 == num3 and num3 > num2:
        print(num2,num3,num1)
    else:
        print('Todos los numeros son iguales')
elif ordenamiento == 'descendente':
    if num1 > num2 and num2 > num3:
        print(num1,num2,num3)
    elif num1 > num3 and num3 > num2:
        print(num1,num3,num2)
    elif num2 > num1 and num1 > num3:
        print(num2,num1,num3)
    elif num2 > num3 and num3 > num1:
        print(num2,num3,num1)
    elif num3 > num2 and num2 > num1:
        print(num3,num2,num1)
    elif num3 > num1 and num1 > num2:
        print(num3,num1,num2)
    elif num3 == num1 and num1 > num2:
        print(num3,num1,num2)
    elif num3 == num2 and num2 > num1:
        print(num3,num2,num1)
    elif num2 == num1 and num1 > num3:
        print(num2,num1,num3)
    elif num2 == num3 and num3 > num1:
        print(num2,num3,num1)
    elif num1 == num2 and num2 > num3:
        print(num1,num2,num3)
    elif num1 == num3 and num3 > num2:
        print(num1,num3,num2)
    else:
        print('Todos los numeros son iguales')
else:
    print('Ingrese un ordenamiento valido')
