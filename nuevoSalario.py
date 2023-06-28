#calcular el nuevo salario de un empleado si tuvo un aumento del x%


def calculoIncrement(salario, x):#calculo entre salario y porcentaje
    nuevoSalario = salario + (salario * (x/100))
    return nuevoSalario

salarioActual = float(input("Ingrese el salario actual: "))
increment = float(input("Ingrese el porcentaje de incremento: "))
nuevoSalario = calculoIncrement(salarioActual, increment)

print("el nuevo salario es de:", round(nuevoSalario))

