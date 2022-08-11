cantidadDolares = float(input('Introduzca los dolares a convertir: '))
moneda = input('Introduzca la moneda a la que desea convertir: ')
precioPeso = 4312.24

if moneda == 'pesos colombianos':
    dolaresConvertidos = cantidadDolares * precioPeso
    print(cantidadDolares,'dolares son equivalentes a', dolaresConvertidos)
else:
    print('Conversion no valida')
