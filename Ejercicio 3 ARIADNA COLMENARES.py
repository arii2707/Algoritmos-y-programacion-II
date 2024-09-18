#EJERCICIO Nª3
#Programa que almacena una contraseña en una variable y verifica si es correcta

#Almacenamos la contraseña en una variable
contraseña_guardada = "TaylorSwift4ever"

#Solicitar al usuario que ingrese la contraseña
contraseña_usuario = input("Introduce la contraseña: ")

if contraseña_guardada.lower() == contraseña_usuario.lower(): #Convertimos ambas contraseñas en minuscula utilizando .lower 
 print("La contraseña es correcta")
else:
     print("La contraseña es incorrecta")
 
