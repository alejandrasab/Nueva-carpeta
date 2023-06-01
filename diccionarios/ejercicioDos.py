#Crea un login que compruebe el diccionario y contraseña
usuarios = {
    "alexdx": {
        "nombre": "Alejandra",
        "apellido": "Sanchez",
        "password": "73737"
    },
    "ximenaxdx": {
        "nombre": "Ximena",
        "apellido" : "Graciano",
        "password" : "12345"
    },
    "rocioxdx" : {
        "nombre" : "Rocio",
        "apellido" : "Terromes",
        "password" : "12345"
    }
}
errores = 3
while errores > 0:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario in usuarios and contraseña == usuarios[usuario]["password"]:
        nombre = usuarios[usuario]["nombre"]
        apellido = usuarios[usuario]["apellido"]
        print(f"Hola, {nombre} {apellido}")
        break
    else:
        print(f"Los datos que ingresaste no son correctos. te quedan {errores - 1}")
        errores -= 1
if errores == 0:
    print("Ya no te quedan intentos.:(")