print('Programa para saber si se puede aplicar a jovenes en acción')
lugarFormacion = input('¿Estudia en el sena o en ies?: ')
nivelFormacion = input('¿Que nivel de formacion esta cursando(tecnico profesional, tecnologo o profesional universitario)?: ')
periodosCursados = int(input('¿Cual es el numero de periodos que tiene matriculados?: '))


if lugarFormacion.lower() == 'sena':
    if nivelFormacion.lower() == 'tecnico profesional':
        print('Puedes aspirar a JeA')
    elif nivelFormacion.lower() == 'tecnologo':
        print('Puedes aspirar a JeA')
    elif lugarFormacion.lower() == 'sena' and nivelFormacion.lower() == 'profesional universitario':
        print('El Sena no cuenta con una oferta academica para certficar profesionales')
else:
    print('Ingresa valores validos')
    
if lugarFormacion.lower() == 'ies':
    if nivelFormacion.lower() == 'tecnico profesional' and periodosCursados <= 2:
        print('Puede aspirar a JeA')
    elif nivelFormacion.lower() == 'tecnologo' and periodosCursados <= 3:
        print('Puede aspirar a JeA')
    elif nivelFormacion.lower() == 'profesional universitario' and periodosCursados <= 4:
        print('Puede aspirar a JeA')
    else:
        print('No puedes aspirar a JeA')
else:
    print('Ingrese valores validos')