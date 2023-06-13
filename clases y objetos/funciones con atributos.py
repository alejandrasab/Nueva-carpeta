

class Persona:
    edad = 27
    nombre = "victor"
    pais = "mexico"

doctor = Persona()

print ("la edad es: ",doctor.edad)
#es mejor escribir esto usando geattr
print("la edad es: ", getattr(doctor, "edad"))

#para saber si el atributo existe en la clase
print("el doctor tiene una edad?", hasattr(doctor,"edad"))

#para hacer cambios
setattr(doctor, 'nombre','alejandra')
print(doctor.nombre)

#eliminar atribujot de ojeto
#se utiliza el nombre de la clase
delattr(Persona, 'pais')
print(hasattr(doctor,'pais'))

