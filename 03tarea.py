def fibonacci(n):
    if n <= 0:
        print("El número de elementos debe ser mayor que cero.")
        return

    a, b = 0, 1

    if n >= 1:
        print(a, end=" ")
    if n >= 2:
        print(b, end=" ")

    for i in range(2, n):
        siguiente_numero = a + b
        print(siguiente_numero, end=" ")
        a, b = b, siguiente_numero

# Pedir al usuario que ingrese el número de elementos de la sucesión a generar
n = int(input("Ingrese el número de elementos de la sucesión de Fibonacci a generar: "))

# Llamar a la función para generar la sucesión de Fibonacci
fibonacci(n)
