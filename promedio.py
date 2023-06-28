'''hacer un programa que tome las tres notas de un estudiante y digan la nota final del curso, la primera y segunda nota vale 30% y la tercera vale
 40%'''

def calcularNota(n1, n2, n3): #usare una funcion que calcule las tres notas
    return (n1*0.3) + (n2*0.3) + (n3*0.4)  #la funcion me retornara las notas ingresadas calculadas por el percent correspondiente


n1 = float(input("Ingrese su primera nota: "))
n2 = float(input("Ingrese su segunda nota: "))
n3 = float(input("Ingrese su tercera nota: "))

notaFinal = calcularNota(n1, n2, n3) #resultado de las notas

print("la nota final es:", round(notaFinal,1))


