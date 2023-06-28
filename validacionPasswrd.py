#crear programa que valide si una contraseña es segura. Tiene que tener mas de 8 caracteres, al menos una letra mayuscula, almenos un numero

#como se hacen estas verificaciones:

# print(len("cadena"))
# print("a".isupper())
# print("a".isnumeric())
# cadena = "hola"
# for i in range(len(cadena)):
#     print(cadena[i])

def comprobarPassword(password):
    largo = False #comprobacion si no cumple la password con el largo requerido
    mayus = False #comprobacion si no tiene mayuscula
    numer = False #comprobacion si noy numeros
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True
    
    if largo and mayus and numer:
        return True
    else:
        return False
    
password = input("Ingrese contraseña: ")
verify = comprobarPassword(password)
if verify:
    print("Contraseña segura")
else:
    print("Contraseña no segura")