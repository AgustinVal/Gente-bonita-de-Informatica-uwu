'''
Problema:
Se necesita conocer el rendimiento de un auto, este se obtiene
mediante la formula kms/litro
'''
#Inputs 
kms = float(input("kms? "))
litros = float(input("litros? "))

#Constantes 
rend_prom = 0
best_rend = 0
second_rend = 0
suma = 0
num_de_llamados = 0

while (kms != 0):
    rend_actual = kms / litros
    suma += rend_actual
    num_de_llamados +=1

    #Si... se me olvido como usar el print uwu, es culpa de metodologias
    print("rendimiento=", rend_actual) 

    if(rend_actual > best_rend): 
        second_rend = best_rend #Se guarda el antiguo mayor valor en el segundo
        best_rend = rend_actual #Se guarda el actual en el mayor valor
    elif(rend_actual > second_rend): #Ya se sabe que no es mayor al mejor
        second_rend = rend_actual

    kms = float(input("kms? "))
    if(kms != 0):
        litros = float(input("litros? "))

#Ya se inserto kms = 0, por tanto se imprimen los resultados finales
print("resultados finales:")
print("rendimiento promedio=", suma / num_de_llamados)
print("mejor rendimiento=", best_rend)
print("2° mejor rendimiento", second_rend)


















