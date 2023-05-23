n= int(input("Cuantos numeros deseas ingresar: "))
A= 0
B= 0
i= 1
while i<= n:
	numero=int(input("Ingresar un numero: "))
	if numero<=0:
		A += 1
	else:
		B += 1
	i += 1

print("Numero  mayor a cero: ",B)
print("Numero  menores o igual a cero: ",A)
