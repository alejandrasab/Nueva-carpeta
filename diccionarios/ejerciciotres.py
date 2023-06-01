#Crea un programa que permita introducir a un profesor las notas de sus estudiantes (máximo 10 estudiantes)
def introducir_notas():
    estudiantes = {}
    num_estudiantes = int(input("Introduce el numro de estudiantes máximo 10: "))
    for i in range(1, num_estudiantes + 1):
        nombre = input(f"Introduce el nombre del estudinte {i}: ")
        nota = float(input(f"Introduce la nota del estudiante {i}: "))
        estudiantes[str(i)] = {
            "nombre": nombre,
            "nota": nota
        }
    return estudiantes



def mostrar_notas(estudiantes):
    aprobados = []
    suspendidos = []
    total_notas = 0
    num_estudiantes = len(estudiantes)

    for estudiante in estudiantes.values():
        total_notas += estudiante["nota"]

        if estudiante["nota"] >= 6:
            aprobados.append(estudiante["nombre"])
        else:
            suspendidos.append(estudiante["nombre"])
    print("Estudiantes aprobados:")
    for estudiante in aprobados:
        print("- " + estudiante)
    print("Estudiantes suspendidos:")

    for estudiante in suspendidos:
        print("- " + estudiante)
    nota_media = total_notas / num_estudiantes
    print("Nota media de la clase: " + str(nota_media))


estudiantes = introducir_notas()
mostrar_notas(estudiantes)

def eliminar_estudiante(estudiantes):
    estudiante_eliminar = input("Escribe el nombre del estudiante que quieres eliminar: ")
    for clave, estudiante in estudiantes.items():
        if estudiante["nombre"] == estudiante_eliminar:
            del estudiantes[clave]
            print("El estudiante", estudiante_eliminar, "ha sido eliminado.")
            return
    print("no se encontro ningun estudiante ocn el nombre de: ", estudiante_eliminar)

eliminar = int(input("si quieres eliminar a un estudiante escribe 1: "))
if eliminar == 1:
    eliminar_estudiante(estudiantes)
else:
    print("bueno...")



