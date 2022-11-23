import numpy as np
import matplotlib.pyplot as plt
import scipy
import sys
import math

#definisco l'inversa della cumulativa
def funzione(y):
    res=2*np.arccos(1-2*y)
    return res

#genero nsample numeri casuali tra 0 e 1 da uare come argomento della funzione cumulativa inversa
nsample=10000
y=np.random.random(nsample)

#chiamo la funzione cumulativa inversa sui valori casuali generati e li immagazzino in x
x = funzione(y)

#faccio un istogramma della distribuzione cumulativa delle y
fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(y, bins=100, range=(0,1), color='pink',  ec='violet')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

#faccio un istogramma 
ax[1].hist(x, bins=100, range=(0, 2*np.pi), color='blue', ec='darkblue')
ax[1].set_title('Distribuzione secondo la funzione inversa')
ax[1].set_xlabel('x')
plt.show()

