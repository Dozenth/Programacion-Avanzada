def numerosPares(inicio, fin):
    if inicio <= 0 or fin <= 0 or fin <= inicio:
        print("Rango no válido. El programa ha terminado.")
        return

    pares = False

    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            print(num, end=" ")
            pares = True

    if not pares:
        print("No hay números pares dentro del rango.")

# Pedir al usuario que ingrese el rango
inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))

# Llamar a la función para imprimir los números pares
numerosPares(inicio, fin)
