#Crea un programa que recorra una lista y cree un diccionarioque contenga el numero de veces que aparece cada numero en la lista
def contar_numeros(lista):
    diccionario = {}
    for numero in lista:
        if numero in diccionario:
            diccionario[numero] += 1
        else:
            diccionario[numero]= 1
    return diccionario
lista =  [1, 2, 3, 4, 2, 3, 1, 2, 4, 4]         
resultado= contar_numeros(lista)
print(resultado)
