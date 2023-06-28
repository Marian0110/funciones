"""18.5 = bajo peso
18.5 - 24.9 = normal
25.0 - 29.9 = sobre peso
30.0 . 34.9 = obesidad

IMC = peso / (estatura * estatura)
"""
peso = float(input("Ingrese el peso (kg)"))
altura = float(input("Ingrese la altura (ms)"))

def calcularIMC(p, a):
    return p / (a + a)

def nivelPeso(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif IMC >= 18.5 and IMC <= 24.9:
        return "normal"
    elif IMC >= 25.0 and IMC <= 29.9:
        return "normal"
    else:
        return "bye"





print("Su nivel de peso es:", nivelPeso(calcularIMC))