#calcular la tabla de multiplicar de cualquier numero enterp dado desde el 0 al 12

def tablaDeMultiplicar(n1, n2):
    return str(n1) + " * " + str(n2) + " = " + str(n1*n2)


n = int(input("Ingrese un numero entero: "))

for i in range(0, 13):
    print(tablaDeMultiplicar(n, i))