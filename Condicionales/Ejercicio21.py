# Realizar un algoritmo que calcule el valor a pagar por la compra de un producto sabiendo que se le cobra un 19% de IVA, 
# Se le descuenta un 9%. si la cantidad de productos está entre 100 y 200, 
# Se le descuenta un 11%. si la cantidad de productos está entre 201 y  499.
# Se le descuenta un 12,55%. si la cantidad de productos es superior a 499.

valorProducto = float(input('Ingrese el valor del producto: '))
cantidadProductos = int(input('Ingrese la cantidad de productos: '))
precioXcantidad = valorProducto*cantidadProductos
iva = precioXcantidad*0.19

if cantidadProductos >= 100 and cantidadProductos <= 200:
    descuento9 = precioXcantidad * 0.09
    valorNeto9 = precioXcantidad + iva - descuento9
    
    print('El valor a pagar por el/los productos es de',valorNeto9, 'aplicando un descuento del 9%')
elif cantidadProductos >= 201 and cantidadProductos <= 499:
    descuento11 = precioXcantidad * 0.11
    valorNeto11 = precioXcantidad + iva - descuento11
    
    print('El valor a pagar por el/los productos es de',valorNeto11, 'aplicando un descuento del 11%')
elif cantidadProductos > 499:
    descuento1255 = precioXcantidad * 0.1255
    valorNeto1255 = precioXcantidad + iva - descuento1255
    print('El valor a pagar por el/los productos es de',valorNeto1255, 'aplicando un descuento del 12,55%')
else:
    print('Ingrese un valor valido')


