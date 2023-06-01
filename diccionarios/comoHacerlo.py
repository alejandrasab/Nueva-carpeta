estudiante = {
	"nombre": "alejandra sanchez",
	"edad": 19,
	"nota_media": 8.5,
	"repetidor" : False
}

#acceder al valor de una clave
edad = estudiante["edad"] # devuelve el valor de 'edad'
nota_media = estudiante.get("nota_media") # devuelve el valor de 'nota_media'
# Insertar o actualizar un valor:
#estudiante["edad"] = 25 # actualiza el valor de 'edad'
#estudiante["suspensos"] = 3 # inserta una nueva pareja clave - valor

# insertar una pareja clave - valor o actualizar si ya existe:
estudiante.update({'aprobados':'8'})

#DEVUELVE LAS CLAVES DEL DICCIONARIO
#print(estudiante.keys())
#DEVUELVE TODOS LOS VALORES DEL DICCIONARIO
#print(estudiante.values())
#VACIA EL DICCIONARIO
#print(estudiante.clear())
#devuelve true o false dependiendo si el diccionario tiene la clave
#print( "nota_media" in estudiante )
#ELIMINA LA CLAVE DEL DICCIONARIO Y DEVUELVE SU VALOR ASOCIADO 
estudiante.pop("edad")
print (estudiante)

