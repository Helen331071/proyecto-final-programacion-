# ==========================================
# GENERADOR SEGURO DE CONTRASEÑAS
# Autor: Helen Villanueva
# Curso: Lógica de Programación
# ==========================================

import random
import string
#Bucle principal que mantiene el programa en ejecución hasta que el usuario decida salir.
while True:

    print("\n===================================")
    print(" GENERADOR SEGURO DE CONTRASEÑAS ")
    print("===================================")
    #Validación de datos para evitar errores de entrada
    
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
#Verificación de que un valor esté dentro de un rango
            if longitud > 0:
                break # Interrupción del bucle interno una vez que se valida correctamente la entrada
            else:
                print("La longitud debe ser mayor que 0.")

        except ValueError:
            #Detección de errores cuando se ingresan datos no numéricos
            print("Por favor, ingrese un número válido.")

    # Ingreso de parámetros de seguridad configurables
    usar_mayusculas = input("¿Desea incluir letras mayúsculas? (s/n): ").lower()
    usar_minusculas = input("¿Desea incluir letras minúsculas? (s/n): ").lower()
    usar_numeros = input("¿Desea incluir números? (s/n): ").lower()
    usar_simbolos = input("¿Desea incluir símbolos especiales? (s/n): ").lower()
##Inicio de la lista de caracteres disponibles que se usará para generar la contraseña
    caracteres = ""
    #Evaluación de parámetros para generar el conjunto de caracteres de forma dinámica.

    if usar_mayusculas == "s":
        caracteres += string.ascii_uppercase

    if usar_minusculas == "s":
        caracteres += string.ascii_lowercase

    if usar_numeros == "s":
        caracteres += string.digits

    if usar_simbolos == "s":
        caracteres += "!@#$%&*+-_?"
        #Control que evita ejecutar el generador sin datos.

    if len(caracteres) == 0:
        print("ERROR: Debe seleccionar al menos un tipo de carácter.")

    else: #Definición de la variable que almacenará la salida del programa
        contrasena = ""
        # Bucle que se repite un número fijo de veces según la variable ‘longitud

        for i in range(longitud):
            # Selección aleatoria y unión de caracteres en una variable.
            contrasena += random.choice(caracteres)
# Mostrar el resultado final
        print("\n===================================")
        print("Contraseña generada:")
        print(contrasena)
        print("===================================")

    # Control para decidir si el programa continúa o se detiene
    opcion = input("\n¿Desea generar otra contraseña? (s/n): ").lower()
# Condición de salida del programa: el bucle se detiene si el valor de control es distinto de ‘s’
    if opcion != "s":
        print("\nGracias por utilizar el Generador Seguro de Contraseñas.")
        break