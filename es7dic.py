import es7dicsomme as sp #importo il moduloche mi serve(programma python contenente funzioni e definizioni)
#VISTO CHE es7dicsomme e es7dic SONO NELLA STESSA CARTELLA metodi-computazionali PER IMPORTARE IL MODULO NON SERVE FARE COMANDI AGGIUNTIVI MA BASTA SOLO L'import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#richiamo le funzioni definite nel modulo somma e somma_radici per verificare il corretto funzionamento
a=sp.somma(2)
print(a)
b=sp.somma_radici(2)
print(b)



#leggo i file.csv
f1=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M0.csv')
f2=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M1.csv')
f3=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M2.csv')
f4=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/e09/hit_times_M3.csv')

#printo i csv per vedere i nomi delle colonne e immagazzinarli successivamente in degli array
print(f1)
print(f2)
print(f3)
print(f4)

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


#faccio istogramma dei tempi del  primo modulo

plt.hist(tempi1, bins=100, color='red') #ti fa vedere quanti eventi cadono entro i 100 intervalli dei tempi dell'istogramma
plt.title('Hit per intervallo')
plt.show()


#faccio istogramma degli intervalli delta_t degli hit del primo modulo
differenze_tempi1=np.diff(tempi1)
mask1=differenze_tempi1>0
log_differenze=np.log(differenze_tempi1[mask1]) #metto la maschera su differenze tempi in modo tale da escludere in log_differenze non ci sia il log di valori minori(impossibile) uguali a 0(meno infinito)
plt.hist(log_differenze, bins=50, color='green')
plt.show()
