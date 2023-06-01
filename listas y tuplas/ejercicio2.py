#CREA UN PROGRAMA QUE SOLICITE DOS LISTAS CON 5 CUNMEROS CADA UNA Y MUESTRALE LOS NUMEROS EN COMUN DE AMBAS LISTAS
print("algrega los 5 numeros de tu primera lista")
lista1 = input()
print("agrega los 5 numeros de tu segunda lista")
lista2 = input()
interseccion = list(set(lista1) & set(lista2))
print("los numeros en comun de ambas listas es: ", interseccion)
