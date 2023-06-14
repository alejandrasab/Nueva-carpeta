class Pokemon:
    pass
    def __init(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)
class Piachu (Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: '.format(self.nombre, tipoataque)
class charmander(Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)
    
nuevo_pokemon = Piachu('boby','electrico')
print(nuevo_pokemon.descripcion)
print(nuevo_pokemon.ataque('impacto trueno'))