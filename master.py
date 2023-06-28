import re

registro_personas = []

def validar_rut(rut):
    rut = rut.upper().replace(".", "").replace("-", "")
    if not re.match(r"^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$", rut):
        return False
    rut = rut.split("-")
    num = int(rut[0])
    dv = rut[1]

    suma = 0
    multiplo = 2
    while num != 0:
        suma += (num % 10) * multiplo
        num = num // 10
        multiplo += 1
        if multiplo == 8:
            multiplo = 2

    digito = 11 - (suma % 11)
    if digito == 10:
        digito = "K"
    elif digito == 11:
        digito = "0"

    if str(digito) == dv:
        return True
    else:
        return False

def grabar_persona():
    print("Ingrese los datos de la persona:")
    rut = input("Rut: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    estado_civil = input("Estado Civil (C = Casado, S = Soltero, V = Viudo): ")
    fecha_afiliacion = input("Fecha de Afiliación: ")

    if validar_rut(rut):
        if edad > 18:
            if estado_civil in ["C", "S", "V"]:
                persona = {
                    "Rut": rut,
                    "Nombre": nombre,
                    "Edad": edad,
                    "Estado Civil": estado_civil,
                    "Fecha de Afiliación": fecha_afiliacion
                }
                registro_personas.append(persona)
                print("Persona registrada exitosamente.")
            else:
                print("Error: Estado civil inválido.")
        else:
            print("Error: La persona debe ser mayor de 18 años.")
    else:
        print("Error: Rut inválido.")

def buscar_persona():
    rut = input("Ingrese el Rut de la persona a buscar: ")
    for persona in registro_personas:
        if persona["Rut"] == rut:
            print("Información de la persona:")
            print("Rut:", persona["Rut"])
            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["Edad"])
            print("Estado Civil:", persona["Estado Civil"])
            print("Fecha de Afiliación:", persona["Fecha de Afiliación"])
            return
    print("Persona no encontrada.")

def listar_solteros():
    solteros = [persona for persona in registro_personas if persona["Estado Civil"] == "S"]
    if not solteros:
        print("No hay personas solteras registradas.")
    else:
        print("Personas solteras:")
        for persona in solteros:
            print("Rut:", persona["Rut"])
            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["Edad"])
            print("Estado Civil:", persona["Estado Civil"])
            print("Fecha de Afiliación:", persona["Fecha de Afiliación"])

def mostrar_menu():
    print("---- Menú ----")
    print("1. Grabar persona")
    print("2. Buscar persona")
    print("3. Listar solteros")
    print("4. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu
