num = int(input('Ingrese un numero y compruebe si es multiplo de 2,3,4,5: '))
 
if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0:
    print(num, 'es multiplo de 2, 3, 4, 5')
else:
    print(num, 'no es multiplo de 2, 3, 4, 5')