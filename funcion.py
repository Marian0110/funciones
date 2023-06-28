"""palabra clave def seguido del nombre deseado para la funcion"""
#las funciones pueden tener tantos argumentos como se quiera, def mi_funcion():​

# instrucciones

# Existen 4 tipos de funciones:

# Sin argumentos y sin retorno
# Sin argumentos y con retorno
# Con argumentos y sin retorno
# Con argumentos y con retorno



#funcion sin argumentos / sin retorno
def saludo ():
    print("hola py")
    
saludo()

#funcion con argumento / sin retorno
def despedir(nombre):
    print("goodbye", nombre)

def suma():
    n1 = 10
    n2 = 34
    return n1 + n2


#retornando valores pedidos
def resta(a, b):
    restar = a - b
    print(f"la resta de estos numeros es de: {restar}")
    

a = int(input("ingresa el primer numero"))
b = int(input("ingresa el segundo numero"))
resta(a,b)


