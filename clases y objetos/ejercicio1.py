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
print(f'comence con {mi_coche.gasolina} de gasolina')

mi_coche.avanzar(30)
print(f'kilometros recorridos: {mi_coche.kilometros_recorridos}')  
print(f'tengo: {mi_coche.gasolina}L de gasolina')  

mi_coche.repostar(10)
print(f'y como repostee ahora tengo {mi_coche.gasolina}L de gasolina')  

