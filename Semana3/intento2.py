# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:37:42 2020

@author: USUARIO


"""


def check_dict(distancias):
    
   
    bandera = False
    answer= ''
    
    for key, value in distancias.items():
        if value < 0 :
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


#######
#######
#######

def distancia_ruta_inicial(ruta_inicial, distancias):
    
    
    kilometros = 0
    i = 0
    while i < len(ruta_inicial)-1:
        
        
        
        a = ruta_inicial[i]
        b = ruta_inicial[i + 1]
    
        tupla = (a, b)
        #print(tupla)
        kilometros += distancias[tupla]
        
        i += 1
    
    return kilometros
   
    
#######
#######
#######


def cambio(tupla, ruta_copia):
    
    nueva_lista = ruta_copia.copy()
    
    a = tupla[0]
    b = tupla[1]
    
    posicion_uno = nueva_lista.index(a)
    posicion_dos = nueva_lista.index(b)
    
    temp1 = nueva_lista[posicion_uno]
    temp2 = nueva_lista[posicion_dos]
    
    nueva_lista[posicion_uno] = temp2
    nueva_lista[posicion_dos] = temp1
    
    return nueva_lista

#######
#######
#######





#######
#######
#######

def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    
    check_data = check_dict(distancias)
    
    if check_data == True:
        #empiece a hacer las comparaciones
        ruta_copia = ruta_inicial.copy()
        
        bandera_final = False
        
        distancia_ruta = distancia_ruta_inicial(ruta_inicial, distancias)
        
        i = 1
        
        while i <= len(ruta_copia) - 2:
            
            a = ruta_inicial[i]
            j = i + 1
            
            while j <= len(ruta_copia) - 2:
                b = ruta_copia[j] 
                
                tupla = (a, b)
                #print(tupla)
                #aqui va la funcion cambio()
                lista_cambiada = cambio(tupla, ruta_copia)
                distancia_lista_cambiada = distancia_ruta_inicial(lista_cambiada, distancias)
                
                if (distancia_lista_cambiada < distancia_ruta):
                    
                    mejor_ruta = lista_cambiada
                    distancia_ruta = distancia_lista_cambiada
                    
                    mejor_distancia = distancia_lista_cambiada
                    
                    bandera_final = True
                    
                                   
                j += 1
                
                if (bandera_final == True and i == len(ruta_inicial) - 3):
                    i = 0
                    ruta_copia = mejor_ruta
                    bandera_final = False
                if(bandera_final == False and i == len(ruta_inicial) - 3):
                    
                    answer = '-'.join(mejor_ruta)
                    return {"ruta": answer, "distancia": mejor_distancia}
                
            i += 1
                
                
   
    else:
        return 'Por favor revisar los datos de entrada.'


    return {"ruta": answer, "distancia": mejor_distancia}




    
    
    

