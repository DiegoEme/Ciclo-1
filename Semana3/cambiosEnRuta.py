# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:53:55 2020

@author: USUARIO
"""
distancias = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'H']
copia_ruta = ['H', 'A', 'B', 'C', 'D', 'E', 'H']

#Cambios en la ruta inicial
a= ruta_inicial[1]
b= ruta_inicial[3]
tupla = (a, b)

def cambio(tupla, copia_ruta):
    
    nueva_lista = copia_ruta.copy()
    
    a = tupla[0]
    b = tupla[1]
    
    posicion_uno = nueva_lista.index(a)
    posicion_dos = nueva_lista.index(b)
    
    temp1 = nueva_lista[posicion_uno]
    temp2 = nueva_lista[posicion_dos]
    
    nueva_lista[posicion_uno] = temp2
    nueva_lista[posicion_dos] = temp1
    
    return nueva_lista
print(cambio(tupla, copia_ruta))
    









