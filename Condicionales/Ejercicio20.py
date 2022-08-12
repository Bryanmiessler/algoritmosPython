figura = input('Ingrese una figura geometrica (cuadrado,circulo o rectangulo): ')
pi= 3.1416

if figura == 'circulo':
    radioCirculo = float(input('Ingrese el radio del circulo: '))
    
    areaCirculo = pi* radioCirculo**2
    perimetroCirculo = 2 * pi * radioCirculo
    
    print('El area del circulo es:',areaCirculo,'cm2 y el perimetro es: ', perimetroCirculo,'cm')
elif figura == 'cuadrado':
    ladoCuadrado = float(input('¿Cuanto mide cada lado del cuadrado?: '))
    
    areaCuadrado = ladoCuadrado*4
    perimetroCuadrado = ladoCuadrado * ladoCuadrado
    
    print('El area del cuadrado es: ',areaCuadrado, 'cm2 y su perimetro es: ',perimetroCuadrado,'cm')
elif figura == 'rectangulo':
    baseRectangulo = float(input('Ingrese la base del rectangulo: '))
    alturaRectangulo = float(input('Ingrese la altura del rectangulo: '))
    
    perimetroRectangulo = 2*(baseRectangulo + alturaRectangulo)
    areaRectangulo = baseRectangulo * alturaRectangulo
    
    print('El area del rectangulo es',areaRectangulo,'cm2 y su perimetro es de: ',perimetroRectangulo,'cm')
else:
    print('Ingrese "cuadrado", "circulo" o "rectangulo"')
