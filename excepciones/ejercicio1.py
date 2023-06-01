#Crea un programa que acceda a la posición que el usuario indique de la lista. No olvides capturar las excepciones que puedan surgir en caso de que el usuario introduzca un índice incorrecto o que no exista en la lista.
lista = [6, 14, 11, 3, 2, 1, 15, 19]

try:
    indice = int(input("Introduce el índice de la lista a acceder: "))
    elemento = lista[indice]
    print("El elemento en la posición", indice, "es:", elemento)
except IndexError:
    print("El índice no llega a tanto. La lista tiene", len(lista), "elementos.")
except ValueError:
    print("Este numero no es valido.")
