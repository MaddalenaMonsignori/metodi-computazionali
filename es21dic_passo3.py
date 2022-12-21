import es7dic_reco as rc
from es7dic_reco import Event
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
              
#PASSO 3

#leggo i file.csv
f1=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M0.csv')
f2=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M1.csv')
f3=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M2.csv')
f4=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M3.csv')


'''Ogni riga del file contiene l'informazione su un sensore che è stato colpito (Hit).
Per ogni Hit viene riportata:
identificatore del modulo [0-3]
identificatore del sensore [0-4]
distanza temporale in ns dall'inizio della presa dati

Gli Hit sono ordiati temporalmente all'interno di ciascun file.
I dati rappresentano un secondo di acquisizione dati.'''

#immagazzino i dati dei csv in array
modulo1=f1['mod_id']
detector1=f1['det_id']
tempi1=f1['hit_time']
modulo2=f2['mod_id']
detector2=f2['det_id']
tempi2=f2['hit_time']
modulo3=f3['mod_id']
detector3=f3['det_id']
tempi3=f3['hit_time']
modulo4=f4['mod_id']
detector4=f4['det_id']
tempi4=f4['hit_time']


hitarray1=np.empty(0)
hitarray2=np.empty(0)
hitarray3=np.empty(0)
hitarray4=np.empty(0)

#per ogni file creo un array di hit

for i in range(len(modulo1)):
      hitarray1 = np.append(hitarray1, np.array([ rc.Hit(modulo1[i],detector1[i],tempi1[i]) ]) )#l'uscita rappresenta un data frame devo trasformarlo in array
for i in range(len(modulo2)):
      hitarray2 = np.append(hitarray2, np.array([ rc.Hit(modulo2[i],detector2[i],tempi2[i]) ]))
for i in range(len(modulo3)):
      hitarray3 = np.append(hitarray3, np.array([ rc.Hit(modulo3[i],detector3[i],tempi3[i]) ]))
for i in range(len(modulo4)):
      hitarray4 = np.append(hitarray4, np.array([ rc.Hit(modulo4[i],detector4[i],tempi4[i]) ]))

#ordino temporalmente gli hits

hitordinati=np.empty(0)
hitordinati=np.concatenate((hitarray1, hitarray2, hitarray3, hitarray4))
hitordinati=np.sort(hitordinati)

#calcolo differenza tempi tra un hit e il successivo
deltat=np.diff(hitordinati)

#applico maschera--> differenze di tempi solo positive
mask=deltat > 0
difftime=np.zeros(len(deltat[mask]))

for i in range(len(difftime)):
    difftime[i]=np.log10(deltat[mask][i])

#faccio un istogramma
plt.hist(difftime, bins=30, color='violet')
plt.title('delta t fra hit consecutivi')
plt.show()

#in sublot per mettere scala log ax.set

#separo i vari hit in event separati quando la differenza di tempo tra 2 hit e' piu' grande di un tot (piu' grande di 10**2.2)

array_event=np.empty(0)
for i in len(hitordinati-1):
    diff=hitordinati[i+1]-hitordinati[i]
    if(diff > 10**2.2):
        array_event=np.append(array_event, Event)
        array_event[-1].aggiorna_event(hitordinati[i]) #il -1 indica che prendo solo l'ultimo elemento
    else:
        array_event[-1].aggiorna_event(hitordinati[i])
        
