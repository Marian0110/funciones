#calcular el IVA de una compra, 19% sobre el valor total de la compra

def calcularIVA(p): # p as precioCompra
    IVA = p * 0.19 #calculo del iva sobre el precioCompra
    return IVA

precioCompra = float(input("Ingrese le valor de su compra: "))
IVA = calcularIVA(precioCompra) #IVA es igual a la accion de la funcion, parametro p se reemplaza por precioCompra

print("El valor de la compra sin IVA es", precioCompra)
print("El valor de la compra total con IVA es", (precioCompra + IVA))