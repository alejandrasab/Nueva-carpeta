
class Matematicas:
    def suma(self):
        self.n1= 2
        self.n2= 3
s = Matematicas()
s.suma()
print (s.n1 +s.n2)

#_init_
#¿esto que no es lo mismo que si no se pusera el _int_ y solo se pusiera como en el primer ejercicio?
class Ropa:
    def __init__(self):
        self.marca = "c&a"
        self.talla = "M"
        self.color = "negro"

camisa = Ropa()
print(camisa.talla)
print( camisa.marca)

#para agregar las variables 
class Calculadora:
    #se ponen dentro del _init_ las variables que agregare
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

#aqui es donde se definen los valores de las variables
operacion = Calculadora(2,3)
print (operacion.suma)





