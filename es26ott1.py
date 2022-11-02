import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate
from scipy import optimize

#definisco le funzioni
def potenziale(k, x):
    pot=k*x**6
    return pot

#posso richiamare una funzione in un'altra mettendo negli argomenti di quella piu' esterna anche gli argomenti di quella piu' interna
def periodo(k, x0, m):
    x=np.arange(0, x0, 1) #intervallo di integrazione ceh va da 0 al valore x0 che metto come parametro e con passo 0.3 scelto arbitrariamente
    p=np.sqrt(1/(potenziale(k, x0)-potenziale(k,x)))
    per=np.sqrt(8*m)*integrate.simpson(p, x)
    return per

p_=np.zeros(90) #array che conterra i valori del periodo al variare di x0 che saranno nel grafico
j=0
x0_=np.arange(10, 100, 1) #array che conterra i valori di x0 che sono nel grafico

#calcolo i valori del periodo al variare di x0 con la funzione periodo
for i in range (10, 100, 1):
    
    p_[j]=periodo(1000, i, 3)
    print("periodo della", j , "sima x0 e': ", p_[j], "\n")
    j=j+1

#grafico del periodo al variare di x0
plt.plot(x0_, p_, color='red')
plt.xlabel('valori di x0')
plt.ylabel('valori del periodo')
plt.show()
