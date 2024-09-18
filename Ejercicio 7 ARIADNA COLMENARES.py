#EJERCICIO Nª7
#Este programa asigna una calificación de letra basada en una calificación numérica (0-100)\.

#SolicitaMOS al usuario que ingrese una calificación
calificacion = int(input("Introduce tu calificación (0-100): "))

# DeterminaMOS la calificación de letra correspondiente
if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif 0 <= calificacion < 60:
    letra = "F"

#Muetra la calificación de letra
print(f"Holaa, tu calificación es: {letra}")
