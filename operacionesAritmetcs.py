#programa que pida dos numeros al usuario y una operacion matematica a jecutar
# operaciones: suma, resta, mult, div, exponenciacion, radicacion

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def div(a, b):
    return a / b

def exponenciacion(a, b):
    return a ** b

def radicacion(a, b): #radicando e indice radical e.g: raiz cuadrada de 8 (8 es radicando y indice es 2) la operacion puede ser tipo 8 ** (1/2) osea siempre (1/x)
    return a ** (1/b)


n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
print("1) Suma \n 2) Resta \n 3) Multiplicacion \n 4) Division \n 5) Exponenciacion \n 6) Radicacion")
opc = int(input("Ingrese opcion: "))

#creando condicionales
if opc == 1:
    print(n1, " + ", n2, " = ", suma(n1, n2))
elif opc == 2:
    print(n1, " - ", n2, " = ", resta(n1, n2))
elif opc == 3:
    print(n1, " * ", n2, " = ", multiplicacion(n1, n2))
elif opc == 4:
    print(n1, " / ", n2, " = ", div(n1, n2))
elif opc == 5:
    print(n1, " ^ ", n2, " = ", exponenciacion(n1, n2))
elif opc == 6:
    print(n1, "^ 1/", n2, " = ", radicacion(n1, n2))
else:
    print("Ingrese un numero valido")