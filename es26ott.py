import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate
import math


df=pd.read_csv('/home/mm010044/Scaricati/metodi-computazionali/esercitazione4/vel_vs_time.csv') #il metodo read di pandas apre il file csv con pathname quello tra ' '

#estraggo el colonne della tabella contenuta nel file vel_vs_time.csv ora contenuto in df
velocita=df['v']
tempo=df['t']

#grafico velocita-tempo
plt.plot(tempo , velocita , color='cyan') 
plt.xlabel('Tempo [s]')
plt.ylabel('Velocita [m/s]')
plt.show()

'''
def funzione(t):
    for i in range(0,len(tempo)):
        if t == tempo[i]:
            v=velocita[i]
            return v
            print(v)
        break
'''

#integra i campioni sull'asse y ( primo parametro) corrispondenti ai campioni sull'asse x (secondo parametro)
print('Integrale:',  integrate.simpson(velocita, tempo)) #penso che il valore dell'integrale sia la lunghezza totale della traiettoria

#calcoli i valori delle singole posizioni per fare poi il grafico
n=len(tempo)
posizione=np.zeros(n)

#calcolo l'array delle posizioni applicando al funzione integrate.simpson a ciascuna coppia di intervalli --> tra 0 e 1, poi tra 0 e 2... 
for i in range (0, n):
    posizione[i]=integrate.simpson(velocita[:i+1], tempo[:i+1]) #in questo caso vuol dire che l'intervallo della velocita(e del tempo) su cui integro e' quello che va da 0(sottinteso visto che ci sono i :) e i+1 ad ogni ciclo
    print(i, ": ",posizione[i], "\n")

#grafico posizione-tempo
plt.plot(tempo, posizione, color='cyan') 
plt.xlabel('Tempo [s]')
plt.ylabel('Posizione [m]')
plt.show()
