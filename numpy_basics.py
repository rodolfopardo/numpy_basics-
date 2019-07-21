#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:34:10 2019

@author: rodolfopardo
"""

import numpy as np 

#Tenemos una matriz de numeros 

matriz = [[2,0,5,8], [1,3,7,4], [6,9,0,2], [10,11,12,13], [7,9,12,15], [33,1,31,27], [20,1,23,11], [14,16,18,20]]

#Tenemos una lista
print(matriz)
type(matriz)

len(matriz)


#Declaramos un array con no

new = np.array(matriz)

print(new)

#Conocemos su forma y dimensiones 

print(new.size)
print(new.shape)

#Cambiamos las dimensiones por un array de 4x8

new = new.reshape(4,8)
print(new.shape)
print(new)

#Ubicamos elementos 
#Ubicar todos los elementos del first row

new[0]

#Ubicar los tres primeros elementos del first row

new[0,0:3]

#Ubicar el elemento 15 
new[2,3]

#Ubicar el elemento 16 

new[3,5]

#Sacar la suma de todos los elementos de cada columna

np.sum(new, axis = 0)

#sacar la suma de todos los elementos de cada fila 

np.sum(new, axis = 1)

#Promedio de la primera fila y ultima fila

np.mean(new[0])
np.mean(new[3])

#Guardar valores máximos y minimos por fila

mayores_row = [np.max([i, ]) for i in new]
menores_row = [np.min([i, ]) for i in new]

#Guardar valores maximos y minimos por columnas
#Es otra forma de hacerlo

mayores_columns = np.max(new, axis = 0)
menores_columns = np.min(new, axis = 0)

#Agregar un nuevo array con nuevos datos y dimensiones

nuevos_datos = [65,98,54,23,54,21,12, 20]

nuevo_array = np.append(nuevos_datos,new)

len(nuevo_array)

nuevo_array1 = nuevo_array.reshape(10,4)
nuevo_array1

#Borrar los primeros elementos del nuevo array 

nuevo_array1 = np.delete(nuevo_array1, 0,0)

nuevo_array1
















