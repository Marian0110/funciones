""" arreglos, es un conjunto de datos en donde podremos almacenar cantidad de datos en una sola variable, deben ser homogeneos y finitos
tambien son llamados como matrices,vectores o arrays

se clasifican en 3 tipos:
1)unidimensionales: es un vector de un piso (por asi decirlo)
2)Bidimensionales: vectores de dos pisos
3)Multidimensionales: vectores de mas pisos(complejo)

se podria decir que los arreglos son colecciones como lo son las listas"""

"""arreglos unidimensionales"""
#Para declarar un array en python se importa de la biblioteca de numpy (number python)
import numpy

arreglo = numpy.array ([1, 2, 4, 5])

print(len(arreglo)) #indica el tamaño del arreglo
print(arreglo.shape) #indica la forma del arreglo (,)

#para recorrer un arreglo
arreglo2 = numpy.array([2, 3, 4, 5])

for i in arreglo2:
    print(i)

#crear arreglos directos con intervalos
arreglo3 = numpy.arange(4)
print(arreglo3) #crea un arreglo hasta 4 (-1) osea, [0 1 2 3]
arreglo4 = numpy.arange(4,9)
print(arreglo4) #crea un arreglo desde el 4 hasta el 9(-1) con un intervalo de 1, osea, [4 5 6 7 8]
arreglo5 = numpy.arange(4.0)
print(arreglo5) #crea un arreglo hasta el 4(-1) en decimales, osea, [0. 1. 2. 3.]
arreglo6 = numpy.arange(3,9,3)
print(arreglo6) #crea un arreglo desde el 3 hasta el 9 con paso de 3, osea, [3 6]


#para copiar arreglos
#primera forma: con este metodo el arreglo original quedara grabado en el otro arreglo por defecto
array1 = numpy.array([10, 20, 30, 50])
array2 = array1
print(array2)
array2[3] = 40 #en el indice 3 cambio el 50 por 40
print(array2)
print(array1)
#segunda forma: al agregar el metodo .copy() los arreglos se mantienen con sus valores correspondientes
array1 = numpy.array([1, 2, 3, 5])
array2 = array1.copy()
print(array2)
array2[3] = 4 #se cambia el 3 por el 4
print(array2)
print(array1)

#para guardar datos en un arreglo atraves del ingreso de datos (input)
guardar_dato = numpy.array(["pepe", 2, 3, 4, 5]) #para ingresar un dato str en el arreglo debe existir algun valor en str tambn
guardar_dato[1] = input("Ingrese su nombre: ")
for i in range(len(guardar_dato)):  #para guardar los datos en un arreglo debe hacerce de esta forma, usando el range y el metodo len, de otra forma como por ejemplo poniendo solo la variable guardar_dato, el sistema arroja un error.
    print(f"el valor { i + 1} del arreglo es {guardar_dato[i]}")

#operaciones con los arreglos:
arreglo7 = numpy.array([2, 4, 6, 8])
arreglo7 += 1 #le añade uno mas a cada valor del indice
print(arreglo7) 

arreglo8 = numpy.array([2, 4, 6, 8])
arreglo8 **= 2 #potencia el valor de cada indice por 2
print(arreglo8)

"""en general se le pone el operador mas el igual para modificar los valores por cada indice de un array"""

arreglo9 = numpy.ones(5) #este metodo imprime unos(ones) hasta el rango dado (5)
print(arreglo9)
arreglo10 = arreglo9 + 1 #imprime puros 2 hasta el rango 5
print(arreglo10) 
# y asi sucesivamente
arreglo11 = numpy.ones(10)
arreglo11 += 5
print(arreglo11)

#operatoria con dos o mas arrays:
arreglo12 = numpy.array([3, 5, 6, 8])
arreglo13 = numpy.array([2, 6, 3, 2])
print(arreglo12 + arreglo13) #imprime la suma de cada valor con su indice correspondiente, osea, [5 11 9 10]

arreglo14 = numpy.array([2, 4, 3, 6])
arreglo15 = numpy.array([2, 4, 2, 1])
print(arreglo14 == arreglo15)  #se define si cada valor de cada indice igual es el mismo valor, retorna un True o False en caso de

arreglo16 = numpy.array([12, 34, 56, 20])
arreglo17 = numpy.array([18, 30, 20, 23])
print(arreglo16 > arreglo17) #define el mayor

#y asi sucesivamente lo mismo con cualquier operador 

#algunos metodos con los arreglos:
#.min()
arreglo18 = numpy.array([30, 60, 2, 120])
print(arreglo18.min()) #retorna el numero mas pequeño dentro del arreglo

#.max()
arreglo19 = numpy.array([30, 60, 90, 120])
print(arreglo19.max()) #retorna el numero mayor 

#.sum()
arreglo20 = numpy.array([30, 60, 2, 120])
print(arreglo20.sum())  #suma los valores dentro del arreglo

#.mean() este metodo calcula el promedio de un arreglo (numeros) (funcion propia de NumPy)
arreglo21 = numpy.array([5.6, 3.4, 2.3, 3.1, 6, 7])
print(arreglo21.mean())

#.diag() este metodo muestra los elementos en diagonal (funcion propia de NumPy)


"""Arreglos Bidimensionales"""
#Una matriz bidimensional está compuesta por filas y columnas, se usan dos argumentos que actuan como las coordenadas, la poscicion de la fila 
#y la poscicion de la columna.

import numpy as np
#los arreglos bidimensionales se definen asi:
matriz = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
#Para mostrar las coordenadas de un elemento
print(matriz[0, 1]) #retorna el elemento 2

print(matriz[:, 3]) #el : ingresa a las matrices totales que hay y el indice 3 al valor de la poscicion de las matricis
print(matriz[1, :]) #retorna la matriz señalada 
print(matriz[1,::-1]) #retorna la matriz señalada en reversa

matriz2 = np.zeros(4) #retorna una matriz de puros ceros (Unidimensional) (1 fila de 4 columnas)
print(matriz2) 
matriz3 = np.zeros((3, 5)) #retorna una matriz de puros ceros (Bidimensional) (3 filas 5 columnas)
print(matriz3) 
matriz4 = np.ones(3) #retorna una matriz de puros unos (Unidimensional) (1 fila de 3 columnas)
print(matriz4) 
matriz5 = np.ones((2, 3)) #retorna una matriz de puros unos (Bidimensional) (2 filas 3 columnas)
print(matriz5) 
matriz7 = np.diag([1, 2, 3, 4]) #retorna una matriz con los valores dados en diagonal (Bidimensional)
print(matriz7) 

#Para sumar todo lo que hay en las filas:
matriz8 = np.array([[50, 40, 30],
                    [30, 20, 10]])
print(matriz8.sum())

#Para sumar una fila especifica
matriz9 = np.array([[10, 5, 20],
                    [30, 5, 4]])
print(f"la suma de la fila 0 {matriz9[0, :].sum()}")
print(f"la suma de la fila 1 {matriz9[1, :].sum()}")


#Operaciones con un arreglo bidimensional(dos dimensiones)
matriz10 = np.array([[4, 6],
                     [3, 5],
                     [3, 5],
                     [2, 3]])
print(matriz.ndim) #esta funcion indica la cantidad de dimensiones que tiene una matriz, en este caso retorna 2 porque tiene filas y columnas

print(matriz10.size) #esta funcion indica la cantidad de elementos tanto en filas como columnas
print(matriz10.shape) # indica la cantidad de filas, columnas 4, 3

#concatenar dos matrices:
m1 = np.array([[22, 33, 44],
               [11, 55, 66]])
m2 = np.array([[20, 30, 40],
               [10, 50, 60]])
#se usa la funcion concatenate de NumPy para concatenar las matrices, y se agrega el axis(eje)
print(np.concatenate((m1, m2), axis = 0)) #cuando el axis es a 0, su eje se concatena a lo largo de las filas
print(np.concatenate((m1, m2), axis = 1)) #cuando el axis es a 1, su eje se concatena a lo largo de las columnas

#ejemplos axis:
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Suma a lo largo del eje 0 (columnas)
suma_columnas = np.sum(arr, axis=0)
# Resultado: [5, 7, 9]

# Suma a lo largo del eje 1 (filas)
suma_filas = np.sum(arr, axis=1)
# Resultado: [6, 15]

arr1 = np.array([[1, 2, 3],
                [4, 5, 6]])

# Media a lo largo del eje 0 (columnas)
media_columnas = np.mean(arr1, axis=0)
# Resultado: [2.5, 3.5, 4.5]

# Media a lo largo del eje 1 (filas)
media_filas = np.mean(arr1, axis=1)
# Resultado: [2.0, 5.0]

arr2 = np.array([[1, 2, 3],
                [4, 5, 6]])

# Máximo a lo largo del eje 0 (columnas)
max_columnas = np.max(arr2, axis=0)
# Resultado: [4, 5, 6]

# Máximo a lo largo del eje 1 (filas)
max_filas = np.max(arr2, axis=1)
# Resultado: [3, 6]

