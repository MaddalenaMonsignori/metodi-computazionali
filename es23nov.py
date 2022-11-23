import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy

#la funzione random_walker() genera casualmente la traiettoria di una particella in 2D. i suoi parametri sono il valore del passo della particella, che e' costante per ogni singolo spostamento successivo, e il numero di passi complessivi che fa la particella

def random_walked(step, N_STEP):

        pos_x=np.zeros(N_STEP) #creo un array di zeri che poi conterra'le posiazioni x successive della particella
        pos_y=np.zeros(N_STEP) #creo un array di zeri che poi contrra' le posizioni y successive della particella
        posx=0 #inizializzo a 0 la posizione iniziale sulle x
        posy=0 #inizializzo a 0 la posizione iniziale sulle y
        angolo=np.random.uniform(low=0, high=2*np.pi, size=N_STEP)#con la funzione np.random.uniform() genero N numeri casuali in un intervallo a scelta in questo caso tra 0 e 2pi --> questi valori generati casualmente corrispondono agli angolo casuali con i quali la particella si sposta di volta in volta e quindi gli angoli con cui cambia direzione
        
        for j in range(N_STEP): #con questo ciclo genero gli array pos_x e pos_y che contengono le posizioni successive della particella durante il suo moto casuale(visto che uso la funzione random.uniform())
            posx=posx+step*np.cos(angolo[j]) #sulle x devo moltiplicare il passo costante, relativo a ciascuno spostamento successico, per il cos dell'angolo generato casualmente
            posy=posy+step*np.sin(angolo[j]) #sulle y devo moltiplicare il passo costante, relativo a ciascun spostamento successivo, per il sin delll'angolo gneerato casualmente
            pos_x[j]=posx
            pos_y[j]=posy

        return pos_x, pos_y





#faccio un grafico con 5 random walker(traiettorie) ciascuno con 1000 passi
for i in range(5):
        deltax, deltay=random_walked(3, 1000)
        plt.plot(deltax, deltay)
plt.show()

#faccio un grafico con 100 random walker(traiettorie) ciascuno con 10 passi

for i in range(100):
        deltax10, deltay10= random_walked(3, 10)
        plt.plot(deltax10, deltay10)
plt.show()

#faccio un grafico con 100 random walker(traiettorie) ciascuno con 100 passi

for i in range(100):
        deltax100, deltay100= random_walked(3, 100)
        plt.plot(deltax100, deltay100)
plt.show()

#faccio un grafico con 100 random walker(traiettorie) ciascuno con 1000 passi

for i in range(100):
        deltax1000, deltay1000= random_walked(3, 1000)
        plt.plot(deltax1000, deltay1000)
plt.show()




    
