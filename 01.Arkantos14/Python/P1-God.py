'''
Encontrar el area minima de un terreno en el que se puede
colocar dos casas rectangulares identicas de area a x b 
Estas pueden estar rotadas (una o ambas), tambien tocar sus
lados, pero como cualquier par de casas, no pueden solaparse :D
Para clase
'''
import numpy as np

#Datos
t = int(input()) #Numero de llamadas
lista_resul = np.zeros(t, dtype=int) #Vector de 0's de tamaño t, donde se pondran los resultados de las areas


#Se evalua cada par de datos, dejando el area obtenida guardada en el vector de zeros
for i in range(t):
    a, b = input().split() #Para introducir mas de un valor, separados por un espacio

    #Se introducen constantes convenientes
    lado_chico = min(int(a), int(b))
    lado_grande = max(int(a), int(b))

    if(2*lado_chico <= lado_grande):
        lista_resul[i] = lado_grande**2

    else: #(2*lado_chico > lado_grande): 
        lista_resul[i] = (2 * lado_chico)**2

#Se imprimen los resultados
for j in range(t):
    print(lista_resul[j])




    

        






    