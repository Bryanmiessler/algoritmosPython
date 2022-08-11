# Realice un algoritmo que permita leer un usuario y clave y si el usuario es igual a “admin” y
# la clave igual a “@2022” mostrar un mensaje de bienvenida
# en caso contrario un mensaje indicando acceso denegado.
usuario = input('Introduzca su usuario:')
contraseña = input('Introduzca su contraseña')

if usuario == 'admin' and contraseña == '@2022':
    print('¡Bienvenido!')
else:
    print('Acceso denegado')