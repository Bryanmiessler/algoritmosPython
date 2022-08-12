# Realice un algoritmo que permita determinar si una persona tiene riesgo de tener coronavirus.
# El algoritmo debe preguntar a la persona por cada uno de los siguientes síntomas.
# ¿Tiene Fiebre?
# ¿Tiene Tos?
# ¿Tiene Dificultades para respirar.?
# ¿Tiene Dolor de garganta.?
# ¿Tiene Dolor de cabeza.?
# ¿Tiene Dolores musculares.?
# ¿Tiene Fatiga.?
# ¿Tiene Congestión nasal.?
# Si todas las respuestas son afirmativas el algoritmo deberá mostrar el mensaje "Posibilidad del 90% o más de estar contagiado de coronavirus ".
# Si las respuestas afirmativas están entre 4 y 7 mostrar  "Posibilidad del 40% al 89.99% de estar contagiado de coronavirus ".
# Si las respuestas afirmativas son inferiores 4. Mostrar"Posibilidad inferior al 40% de estar contagiado de coronavirus ".
contador = 0
fiebre = input('¿Tiene Fiebre?: ')
if fiebre == 'si':
    contador += 1
tos = input('¿Tiene Tos?: ')
if tos == 'si':
    contador += 1
difRespirar = input('¿Tiene Dificultades para respirar.?: ')
if difRespirar == 'si':
    contador += 1
dolorGarganta = input('¿Tiene Dolor de garganta.?: ')
if dolorGarganta == 'si':
    contador += 1
dolorCabeza = input('¿Tiene Dolor de cabeza.?: ')
if dolorCabeza == 'si':
    contador += 1
dolorMuscular = input('¿Tiene Dolores musculares.?: ')
if dolorMuscular == 'si':
    contador += 1
fatiga = input('¿Tiene Fatiga.?: ')
if fatiga == 'si':
    contador += 1
congestion = input('¿Tiene Congestión nasal.?: ')
if congestion == 'si':
    contador += 1
    
if contador == 8:
    print('Posibilidad del 90% o más de estar contagiado de coronavirus')
elif contador >= 4 and contador <= 7:
    print('Posibilidad del 40% al 89.99% de estar contagiado de coronavirus')
elif contador < 4:
    print('Posibilidad inferior al 40% de estar contagiado de coronavirus')
else:
    print('Error al comprobar los datos')