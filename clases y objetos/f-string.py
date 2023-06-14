#PARA ACORDARME
#escribir "% s" nos ayuda a concatenar en string
#curso = "python"
#print("tutoriales de % s"%curso)

#nombre = "alejandra"
#edad = 19
#print("hola soy, % s y tengo % s años"%(nombre,edad))

#str.format()
#print("qur tal soy {} y mi edad es {} años".format(nombre,edad))

#f-string es para hacer lo mismo pero es mas practico para leer codigo
#print(f"hola soy {nombre} y tengo {edad} años")

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
       return f"hola soy, {self.nombre} {self.apellido} tengo  {self.edad} años"
    
nuevoestudiante = Estudiante("alejandra","sanchez",19)
print(f"{nuevoestudiante}")

