#EJERCICIO Nª5
#Programa para valuar el rendimiento de los trabajadores de Corpoelec y calcular su bonificacion anual

puntuacion = float(input("Introduce tu puntuacion (0.0, 0.4, 0.6 o mas): "))

#Definimos la cantidad base para la bonificacion
bonificacion_base = 2400

#Determinamos el nivel de rendimiento y calculamos la bonificacion

if puntuacion == 0.0:
 rendimiento = "bajo"
bonificacion = bonificacion_base * puntuacion
if puntuacion == 0.4:
 rendimiento = "medio"
 bonificacion = bonificacion_base * puntuacion
elif puntuacion >= 0.6:
 rendimiento = "alto"
 bonificacion = bonificacion_base * puntuacion


#Moatrar el nivel de rendimiento y la bonificacion
print(f"Tu nivel de rendimiento es: {rendimiento}")
print(f"Recibiras una bonificacion de: {bonificacion} $")
