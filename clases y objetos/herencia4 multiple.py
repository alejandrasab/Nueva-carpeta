#la herencia multiple se refiere a la posibilidad de crar una clase a partir de clases superiores.
class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando...")
    def ocupado(self):
        print("ocupado...")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("tomando fotos...")

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print("reproduciendo musica")
    def reproducirvideo(self):
        print("reproducir un video...")

class smartphone(Telefono,Camara,Reproduccion):
    #__del__ es un destructor que al contrario de __init__ deconstruye la funcion
    def __del__(self):
        print("telefono apagado")

movil = smartphone()
#dir se usa como un directorio de funciones
#print(dir(movil))

print(movil.fotografia())

