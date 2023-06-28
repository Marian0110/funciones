#validar si es primo o no

def esPrimo(n): #numero divisible entre el 1 y el mismo
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False #si pasa la prueba y llega al primer return se ejecuta sino se ejecuta el segundo return que esta fuera del bucle
        return True

# for i in range(-12, 102): #validacion con un bucle con un rango desde -10 hasta el 100 de acuerdo a la funcion hecha
#     print(i, " ", esPrimo(i))

# num = int(input("ingrese un numero: "))
# print(esPrimo(num))

# print(esPrimo(7))