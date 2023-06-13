class Coche:
    def __init__(self, matricula, marca, kilometros_recorridos, gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.gasolina = gasolina
    
    def avanzar(self, kilometros):
        if self.gasolina - (kilometros * 0.1) >= 0:
            self.kilometros_recorridos += kilometros
            self.gasolina -= kilometros * 0.1
        else:
            print("Es necesario repostar para recorrer la cantidad indicada de kilómetros.")
    
    def repostar(self, litros):
        self.gasolina += litros

mi_coche = Coche("ABC123", "Ford", 0, 50)
print(mi_coche.gasolina)  # 50

mi_coche.avanzar(50)
print(mi_coche.kilometros_recorridos)  # 50
print(mi_coche.gasolina)  # 45

mi_coche.avanzar(100)
print(mi_coche.kilometros_recorridos)  # 150
print(mi_coche.gasolina)  # 35

mi_coche.avanzar(40)
print(mi_coche.kilometros_recorridos)  # 190
print(mi_coche.gasolina)  # 31

mi_coche.avanzar(180)
print(mi_coche.kilometros_recorridos)  # 370
print(mi_coche.gasolina)  # 13

mi_coche.repostar(10)
print(mi_coche.gasolina)  # 23 

