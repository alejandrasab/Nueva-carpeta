#EJERCICIO 1:elimina el ultimo numero y añadelo al principio
lista = [12, 23,5,29,92,64]
lista.insert(0,lista[5])
lista.pop()
print(lista)


#EJERCICIO 2:Mueve el segundo elemento a la utima posicion
listaDos = [12, 23,5,29,92,64]
listaDos.insert(6, listaDos[1])
listaDos.remove(listaDos[1])
print(listaDos)

#EJERCICIO 3: Añade el numero 14 al principio de la lista
listaTres = [12, 23,5,29,92,64]
listaTres.insert(0,14)
print(listaTres)

#EJERCICIO 4: Suma todos los numeros de la lista y añade el resultado al final de la lista
listaCuatro = [12, 23,5,29,92,64]
suma = sum(listaCuatro)
listaCuatro.insert(6, suma)
print(listaCuatro)

#Ejercicio 5: fusiona l lista actual con la siguiente [4, 11, 32]
listaCinco = [12, 23,5,29,92,64]
agregar = [4, 11, 32]
listaCinco.extend(agregar)
print(listaCinco)

#EJERCICIO 6: elimina los numeros impares de la lista
listaSeis = [12, 23,5,29,92,64]
listaSeisN =[]
i=0
sizeList = len(listaSeis)
for elemento in listaSeis:
    if elemento %2>0:
        listaSeisN.append(elemento)
print(listaSeisN)

#EJERCICIO 7: Ordena los numeros de la lista en forma ascendente
listaSiete = [12, 23,5,29,92,64]
listaSiete.sort()
print(listaSiete)

#EJERCICIO 8: lista vacia
listaOcho = [12, 23,5,29,92,64]
listaOcho.clear()
print(listaOcho)
