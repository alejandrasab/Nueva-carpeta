
class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f"pastel({self.ingredientes !r})"
    @classmethod
    def Pastel_chocolate(cls):
        return cls(['harina','leche', 'chocolate'])
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['harina', 'lehce', 'vainilla'])
    
print(Pastel.Pastel_vainilla())

#METODO ESTATICO
import math
class Pastel_dos:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return (f'Pastel_dos({self.ingredientes}, 'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel_dos(['arina', 'azuar', 'leche', 'crema',],4)
print(nuevo_pastel.tamaño_area(12))
    

