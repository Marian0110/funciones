
afiliados = []

def validarRut(rut):
    largo = False #comprobacion si no cumple el rut con el largo requerido
    digitoVerificador = False #comprobacion si no tiene letra
    numer = False #comprobacion si no hay numeros
    guion = False
    if len(rut) > 10:
        largo = True
    # for i in range(len(rut)):
    #     if rut[i].isnumeric():
    #         numer = True
    #     if rut[i].lower() == "K" or rut[i] in range(0, 9):
    #          digitoVerificador = True
    #     if rut[i] == "-":
    #         guion = True
    if largo:
        return True
    else:
        return False
    
rut = input("Ingrese rut: ")
verify = validarRut(rut)
if verify:
    print("rut ingresado exitosamente")
else:
    print("rut invalido")



# def grabarPersona():
#     rut = int(input("Ingrese el Rut: "))

#     nombre = input("Ingrese el nombre: ")
#     edad =  int(input("Ingrese la edad: "))
#     estadoCivil = input("Ingrese estado civil, Casado (C), Soltero (S), Viudo (V): ")
#     fechaAfiliacion = input("Ingrese fecha de afiliacion: ")

