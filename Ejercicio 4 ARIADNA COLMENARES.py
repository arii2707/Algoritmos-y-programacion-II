#EJERCICIO Nª4
#Programa para dividir a un grupo de alumnos en dos grupos A y B

#solicitar al usuario que ingrese su nombre
nombre = input("Introduce tu nombre: ")

 #solicitar al usuario que ingrese su sexo (M para mujer, H para hombre)
sexo = input("Introduce tu sexo (M para mujer, H para hombre):")

#Determinamos a que grupo pertenece el usuario utulizando if-else

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Eres parte del grupo: {grupo}")
    
