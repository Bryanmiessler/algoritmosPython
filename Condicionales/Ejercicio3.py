print('Programa para conocer numero de días por mes')
mes = input('Introduzca el nombre del mes: ')
 
if mes == 'Enero' or mes == 'Marzo' or mes == 'Mayo' or mes == 'Julio' or mes == 'Agosto' or mes == 'Octubre' or mes == 'Diciembre':
    print('El mes de',mes,'tiene 31 dias')
elif mes == 'Abril' or mes == 'Junio' or mes == 'Septiembre' or mes == 'Noviembre':
    print('El mes de', mes,'tiene 30 dias')
elif mes == 'Febrero':
    print('El mes de', mes,'tiene 28 dias')
else:
    print('Introduzca un mes valido')