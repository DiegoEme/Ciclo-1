# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:03:58 2020

@author: USUARIO
"""
distancias = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

def check_dict(distancias):
    
    bandera = False
    answer = ''
    
    for key, value in distancias.items():
        if value < 0:
            answer = 'Por favor revisar los datos de entrada.'
            return answer
        elif value == 0:
            if key[0] != key[1]:
                answer = 'Por favor revisar los datos de entrada.'
                return answer
        elif key[0] == key[1]:
            if value != 0:
                 answer = 'Por favor revisar los datos de entrada.'
                 return answer
        else:
            bandera = True
    return bandera
    
    
print(check_dict(distancias))