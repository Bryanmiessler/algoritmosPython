num = int(input('Ingrese un numero y compruebe si es multiplo de 2, 3 o 4: '))
 
if num % 2 == 0 or num % 3 == 0 or num % 4 == 0:
    print(num, 'es multiplo de 2, 3 o 4')
else:
    print(num, 'no es multiplo de 2, 3 o 4')