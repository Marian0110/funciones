
afiliados = []

def validarRut(rut):
    largo = False #comprobacion si no cumple el rut con el largo requerido
    digitoVerificador = False #comprobacion si no tiene letra
    numer = False #comprobacion si no hay numeros
    guion = False
    if len(rut) > 7 and len(rut) <= 10:
        largo = True
    for i in range(len(rut)):
        if rut[i].isnumeric():
            numer = True
        if rut[i].lower() == "k":
             digitoVerificador = True
        if rut[i] == "-":
            guion = True
    if largo and numer and guion and digitoVerificador:
        return True
    else:
        return False
    
def grabarPersona():
    print("Ingrese los datos de la persona")
    
    rut = input("Ingrese rut: ")
    verify = validarRut(rut)
    if verify:
        print("rut ingresado exitosamente")
    else:
        print("rut no valido")
        
    nombre = input("Ingrese el nombre: ")
    edad =  int(input("Ingrese la edad: "))
    estadoCivil = input("Ingrese estado civil, Casado (C), Soltero (S), Viudo (V): ")
    fechaAfiliacion = input("Ingrese fecha de afiliacion: ")

    if validarRut(rut):
        if edad > 18:
            if estadoCivil in ["C", "S", "V"]:
                persona = {
                "Rut": rut,
                "Nombre": nombre,
                "Edad": edad,
                "estadoCivil": estadoCivil,
                "fechaAfiliacion": fechaAfiliacion }

    afiliados.append(persona)
            