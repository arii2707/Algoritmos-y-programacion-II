#EJERCICIO Nª2
#Programa para calcular el area de un rectangulo y que muestra un mensaje personalizado

#Solicitar al usuario que ingrese la base del rectangulo y altura del mismo
base = float(input("Introduce la base del rectangulo: "))
altura = float(input("Introduce la altura del rectangulo: "))

#Calculamos el area del rectangulo
area = base*altura
print(f"El area del rectangulo es: {area}")

 #Verificamos si el area es mayor a 40 y la altura es mayor a 10
if area > 40 and altura > 10:
 print("¡Holaa, el area es mayor a 40 y la altura es mayor a 10!")

