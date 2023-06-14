
class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return' {} tiene {}'.format(self.nombre, self.año)
    
    def comentario(self,frase):
        return '{} dice {}'.format(self.nombre,frase)


doctor = Persona('jose',26)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario('hola que tal'))

#modificar un atributo
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
#print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)