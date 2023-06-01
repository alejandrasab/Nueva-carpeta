#Crea una aplicación reciba la clave de un diccionario y acceda a uno de sus valores. 
diccionario = {"hola1": "adios1", "hola2": "adios2", "hola3": "adios3"}

def obtener_valor_diccionario():
    try:
        clave = input("Ingresa una clave del diccionario: ")
        valor = diccionario[clave]
        print("El valor correspondiente a la clave '{}' es: {}".format(clave, valor))
    except KeyError:
        print("La clave ingresada no existe en el diccionario.")

obtener_valor_diccionario()