letra = input('Ingrese solo una letra: ')
lonLetra = len(letra)

if lonLetra == 1:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('La letra ingresada es una vocal')
    else:
        print('La letra no es una vocal')
else:
    print('Ingrese solo una letra')