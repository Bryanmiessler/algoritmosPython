# Realice un algoritmo que permita calcular el valor bruto, valor neto, valor iva y valor descuento por
# la compra de un producto de acuerdo a los siguientes criterios.
# El iva es del 19%
# Si el día es lunes, al valor bruto se aplica un descuento del 10%.
# Si el día es martes o miércoles el descuento es del 15%
# Si el día es jueves el descuento es del 12%
# Si el día es viernes el descuento es del 8%
# Si el día es sábado el descuento es del 5%
# Si el día es domingo el descuento es del 3%
# Cuando el usuario compra una cantidad superior a 100 productos se aplica un descuento adicional del 2% al valor bruto.

valorProducto = float(input('Ingrese el valor del producto: '))
cantidadProductos = int(input('Ingrese la cantidad de productos: '))
precioXcantidad = valorProducto*cantidadProductos
dia = input('Ingrese el día de la compra: ')
iva = precioXcantidad * 0.19

if dia == 'lunes':
    if cantidadProductos > 100:
        descuentoCantidad = precioXcantidad * 0.02
        precioXcantidad = precioXcantidad - descuentoCantidad
        
        print('Por la compra superior a 100 articulos obtuvo un descuento del 2% equivalente a', descuentoCantidad,'pesos')
        
    descuentoLunes = precioXcantidad * 0.10
    valorNetoLunes = precioXcantidad + iva - descuentoLunes
    
    print('El valor bruto del producto es de',precioXcantidad,'pesos')
    print('El descuento del 10% sobre el producto es de',descuentoLunes,'pesos')
    print('El valor del iva sobre el producto es de',iva,'pesos')
    print('El valor neto del producto es de',valorNetoLunes,'pesos')
    
        
elif dia == 'martes' or dia == 'miercoles':
    if cantidadProductos > 100:
        descuentoCantidad = precioXcantidad * 0.02
        precioXcantidad = precioXcantidad - descuentoCantidad
        
        print('Por la compra superior a 100 articulos obtuvo un descuento del 2% equivalente a', descuentoCantidad,'pesos')
        
    descuentoMyM = precioXcantidad * 0.15
    valorNetoMyM = precioXcantidad + iva - descuentoMyM
    
    print('El valor bruto del producto es de',precioXcantidad,'pesos')
    print('El descuento del 15% sobre el producto es de',descuentoMyM,'pesos')
    print('El valor del iva sobre el producto es de',iva,'pesos')
    print('El valor neto del producto es de',valorNetoMyM,'pesos')
elif dia == 'jueves':
    if cantidadProductos > 100:
        descuentoCantidad = precioXcantidad * 0.02
        precioXcantidad = precioXcantidad - descuentoCantidad
        
        print('Por la compra superior a 100 articulos obtuvo un descuento del 2% equivalente a', descuentoCantidad,'pesos')
        
    descuentoJueves = precioXcantidad * 0.12
    valorNetoJueves = precioXcantidad + iva - descuentoJueves
    
    print('El valor bruto del producto es de',precioXcantidad,'pesos')
    print('El descuento del 12% sobre el producto es de',descuentoJueves,'pesos')
    print('El valor del iva sobre el producto es de',iva,'pesos')
    print('El valor neto del producto es de',valorNetoJueves,'pesos')
elif dia == 'viernes':
    if cantidadProductos > 100:
        descuentoCantidad = precioXcantidad * 0.02
        precioXcantidad = precioXcantidad - descuentoCantidad
        
        print('Por la compra superior a 100 articulos obtuvo un descuento del 2% equivalente a', descuentoCantidad,'pesos')
        
    descuentoViernes = precioXcantidad * 0.08
    valorNetoViernes = precioXcantidad + iva - descuentoViernes
    
    print('El valor bruto del producto es de',precioXcantidad,'pesos')
    print('El descuento del 8% sobre el producto es de',descuentoViernes,'pesos')
    print('El valor del iva sobre el producto es de',iva,'pesos')
    print('El valor neto del producto es de',valorNetoViernes,'pesos')
elif dia == 'sabado':
    if cantidadProductos > 100:
        descuentoCantidad = precioXcantidad * 0.02
        precioXcantidad = precioXcantidad - descuentoCantidad
        
        print('Por la compra superior a 100 articulos obtuvo un descuento del 2% equivalente a', descuentoCantidad,'pesos')
        
    descuentoSabado = precioXcantidad * 0.05
    valorNetoSabado = precioXcantidad + iva - descuentoSabado
    
    print('El valor bruto del producto es de',precioXcantidad,'pesos')
    print('El descuento del 5% sobre el producto es de',descuentoSabado,'pesos')
    print('El valor del iva sobre el producto es de',iva,'pesos')
    print('El valor neto del producto es de',valorNetoSabado,'pesos')
elif dia == 'domingo':
    if cantidadProductos > 100:
        descuentoCantidad = precioXcantidad * 0.02
        precioXcantidad = precioXcantidad - descuentoCantidad
        
        print('Por la compra superior a 100 articulos obtuvo un descuento del 2% equivalente a', descuentoCantidad,'pesos')
        
    descuentoDomingo = precioXcantidad * 0.03
    valorNetoDomingo = precioXcantidad + iva - descuentoDomingo
    
    print('El valor bruto del producto es de',precioXcantidad,'pesos')
    print('El descuento del 3% sobre el producto es de',descuentoDomingo,'pesos')
    print('El valor del iva sobre el producto es de',iva,'pesos')
    print('El valor neto del producto es de',valorNetoDomingo,'pesos')
else:
    print('Error al comprobar valores ingresados')
        