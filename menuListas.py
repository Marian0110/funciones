#prueba 2: mostrar menu con entradas a comprar por usuario: menores $2500, adulto $5000, adultos mayores $1000. 
#mostrar cantidades, descuentos si es menor 10% o adulto 5%, el sistema debe permitir anular la compra y seguir mostrando el menu

menu = True
compras = []

while menu:
    try:
        print(" -------Entradas---------\n\
 1)Menores......-....$2500\n\
 2)Adultos...........$5000\n\
 3)Adultos Mayores...$1000\n\
 4)Anular compra\n\
 5)Salir del menu\n\
 ------------------------")
        entrada = int(input(" ingrese una opcion: "))
        if entrada < 1 or entrada > 5:
            print("opcion fuera de rango, intente de nuevo")
        elif entrada == 5:
            print("Saldras del menu.")
            menu = False 
        elif entrada == 4:
            if compras:
                ultima_compra = compras.pop()
                print(f"la compra de {ultima_compra['cantidad']} entradas de {ultima_compra['tipo']} ha sido anulada exitosamente")
            else:
                print("no hay compras para anular")
        else:
            if entrada == 1:
                tipo = "Menores"
                precio = 2500
            elif entrada == 2:
                tipo = "Adultos"
                precio = 5000
            elif entrada == 3:
                tipo = "Adultos Mayores"
                precio = 1000
            cant = int(input("Ingrese cantidad de entradas: "))
            dia_desc = input("Ingrese dia de asistencia: ")
            if dia_desc.lower() == "viernes":
                entradas = cant * precio
                if tipo == "Menores":
                    desc = entradas * 0.10
                elif tipo == "Adultos":
                    desc = entradas * 0.05
                else:
                    desc = 0
                total = entradas - desc
            else:
                desc = 0
                total = entradas
            compras.append({"tipo": tipo, "precio": precio, "descuento": desc, "cantidad": cant, "total": total })
            print(f"compra de {cant} entradas {tipo} realizada con exito.")
            opc = input("Desea realizar otra compra? (si/no): ")
            if opc.lower() == "no":
                print("-------Boleta--------")
                subTotal = 0
                descTotal = 0
                for compra in compras:
                    subTotal += compra['cantidad'] * compra['precio']
                    descTotal += compra['descuento']
                    print(f"°{compra['cantidad']} Entradas {compra['tipo']}:    ${compra['cantidad'] * compra['precio']}")
                print("-------------------------")
                print(f"Subtotal: {round(subTotal)}")
                print(f"Descuentos: {round(descTotal)}")
                print("-------------------------")
                total_Final = subTotal - descTotal
                print(f"Total a pagar: {round(total_Final)}")
                print("-------------------------")
                print("   Gracias por su compra!")
                menu = False

    except ValueError:
        print("Solo se permiten numeros,intente de nuevo")