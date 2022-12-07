import math
import numpy as np


#definisco una funzione che restituisca la somma dei primi n numeri naturali
def somma (n):
    s=0
    for i in range(n+1): #devo mettere n+1 perche'for i in range(valore) ha l'ultimo estremo escluso quindi arriva fino a valore -1
        s=s+i
    return s
#definisco una funzione che restituisca la somma delle radici dei primi n numeri naturali
def somma_radici(n):
    s=0
    for i in range(n+1):
        s=s+np.sqrt(i)
    return s

'''prova
sum=somma(2)
print(sum)
sum1=somma_radici(2)
print(sum1)
 '''
