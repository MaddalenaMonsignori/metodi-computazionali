import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 
from scipy import constants
from scipy import fft
from scipy import optimize

#Definisco la funzione noise per il fit che calcola i coefficienti di Fourier per il white, pink, red noise
def noise(f, a, b, c):
    n=a*(1/f**b)+c
    return n

#Leggo i 3 file .csv 
mydf1=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/get_data.py/data_sample1.csv')
mydf2=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/get_data.py/data_sample2.csv')
mydf3=pd.read_csv('/home/mm010044/Scaricati/get-mcf-data/get_data.py/data_sample3.csv')

#Printo i contenuti dei 3 file. csv per vedere il nome delle colonne e immagazzinare i dati
print(mydf1)
print(mydf2)
print(mydf3)


#Immagazzino i dati contenuti nelle colonne dei .csv dentro degli array
mydf1_time=mydf1['time'].values #il metodo .values trasforma i dati contenuti nel dataframe in array veri e propri di numpy --> se non lo mettessi mi includerebbe anche gli indici (tipici del formato del dataframe) e quando andrei a chiamare la funzione della trasfromata di Fourier(fft.fft) mi darebbe errore
mydf1_meas=mydf1['meas'].values
mydf2_time=mydf2['time'].values
mydf2_meas=mydf2['meas'].values
mydf3_time=mydf3['time'].values
mydf3_meas=mydf3['meas'].values


#Faccio i grafici delle misure in funzione del tempo contenute nei file .csv e immagazzinati in array
plt.plot(mydf1_time, mydf1_meas, color='violet')
plt.title('Data sample 1', color='violet')
plt.xlabel('Time')
plt.ylabel('Measure')
plt.show()

plt.plot(mydf2_time ,mydf2_meas, color='limegreen')
plt.title('Data sample 2', color='limegreen')
plt.xlabel('Time')
plt.ylabel('Measure')
plt.show()

plt.plot(mydf3_time ,mydf3_meas, color='yellow')
plt.title('Data sample 3', color='yellow')
plt.xlabel('Time')
plt.ylabel('Measure')
plt.show()


#Faccio la trasformata di Fourier delle misure
fourier1=fft.rfft(mydf1_meas) #contiene i coefficienti di fourier
fourier2=fft.rfft(mydf2_meas) #contiene i coefficienti di fourier
fourier3=fft.rfft(mydf3_meas) #contiene i coefficienti di fourier


#Calcolo le frequenze corrispondenti della trasformata di fourier.
#N.B se usi la funzione delle frequenze reali (rfft.freq) ti restituisce la meta' delle frequenze(visto che per la semionda positiva e negativa sono uguali te li da' una volta sola)
freq1=fft.rfftfreq(len(fourier1), d=1)
freq2=fft.rfftfreq(len(fourier2), d=1)
freq3=fft.rfftfreq(len(fourier3), d=1)


#Faccio i grafico dei 3 spettri di potenza --> sarebbe il grafico dei coefficienti di fourier in modulo al quadrato in funzione dell'indice

plt.plot(np.absolute(fourier1[:fourier1.size//2])**2, 'o', color='violet') #Faccio il plot solo della meta' dei coefficienti (presi in modulo ed elevati al quadrato) poiche' visto che si ripetono sia per la semionda positiva che negativa liprendo una sola volta
plt.xlabel('Indice')
plt.ylabel('$|c_k|^2$')
plt.title('Coeff in modulo al quadr in funzione indice 1', color='violet')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()

plt.plot(np.absolute(fourier2[:fourier2.size//2])**2, 'o', color='limegreen') #Faccio il plot solo della meta' dei coefficienti (presi in modulo ed elevati al quadrato) poiche' visto che si ripetono sia per la semionda positiva che negativa liprendo una sola volta
plt.xlabel('Indice')
plt.ylabel('$|c_k|^2$')
plt.title('Coeff in modulo al quadr in funzione indice 2', color='limegreen')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()

plt.plot(np.absolute(fourier3[:fourier3.size//2])**2, 'o',color='yellow') #Faccio il plot solo della meta' dei coefficienti (presi in modulo ed elevati al quadrato) poiche' visto che si ripetono sia per la semionda positiva che negativa liprendo una sola volta
plt.xlabel('Indice')
plt.ylabel('$|c_k|^2$')
plt.title('Coeff in modulo al quadr in funzione indice 3', color='yellow')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()


#Faccio i grafico dei 3 spettri di potenza in funzione della frequenza --> sarebbe il grafico dei coefficienti di fourier in modulo al quadrato in funzione della frequenza

plt.plot(freq1[:fourier1.size//2], np.absolute(fourier1[:fourier1.size//2])**2, 'o', color='violet') #Faccio il plot solo della meta' dei coefficienti (presi in modulo ed elevati al quadrato) poiche' visto che si ripetono sia per la semionda positiva che negativa li prendo una sola volta. Per quanto riguarda la frequenza la funzione .fftfreq gia' mi calcola la meta' delle frequenze pero' per essere sicura che gli array abbiano la stessa dimensione us uso fourier.size//2
plt.title('Data sample 1' )
plt.xlabel('Frequenza')
plt.ylabel('$|c_k|^2$')
plt.title('Coeff in modulo al quadr in funzione frequenza 1', color='violet')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()

plt.plot(freq2[:fourier2.size//2], np.absolute(fourier2[:fourier2.size//2])**2, 'o', color='limegreen') #Faccio il plot solo della meta' dei coefficienti (presi in modulo ed elevati al quadrato) poiche' visto che si ripetono sia per la semionda positiva che negativa li prendo una sola volta. Per quanto riguarda la frequenza la funzione .fftfreq gia' mi calcola la meta' delle frequenze pero' per essere sicura che gli array abbiano la stessa dimensione us uso fourier.size//2
plt.xlabel('Frequenza')
plt.ylabel('$|c_k|^2$')
plt.title('Coeff in modulo al quadr in funzione frequenza 2', color='limegreen')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()

plt.plot(freq3[:fourier3.size//2], np.absolute(fourier3[:fourier3.size//2])**2, 'o', color='yellow') #Faccio il plot solo della meta' dei coefficienti (presi in modulo ed elevati al quadrato) poiche' visto che si ripetono sia per la semionda positiva che negativa li prendo una sola volta. Per quanto riguarda la frequenza la funzione .fftfreq gia' mi calcola la meta' delle frequenze pero' per essere sicura che gli array abbiano la stessa dimensione us uso fourier.size//2
plt.xlabel('Frequenza')
plt.ylabel('$|c_k|^2$')
plt.title('Coeff in modulo al quadr in funzione frequenza 3', color='yellow')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()




#Fitto i dati dei coefficienti in modulo al quadrato in funzione della frequenza con la funzione noise
#il // fa la divisione tra interi
# NB ESCLUDI IL PRIMO VALORE DELLE FREQUENZE POICHE' E' 0 ALTRIMENTI DA' ERRORE
params1, params_covariance1=optimize.curve_fit(noise, freq1[1:fourier1.size//2], np.absolute(fourier1[1:fourier1.size//2])**2)
params2, params_covariance2=optimize.curve_fit(noise, freq2[1:fourier2.size//2], np.absolute(fourier2[1:fourier2.size//2])**2)
params3, params_covariance3=optimize.curve_fit(noise, freq3[1:fourier3.size//2], np.absolute(fourier3[1:fourier3.size//2])**2)


#Calcolo i valori fittati
# NB ESCLUDI IL PRIMO VALORE DELLE FREQUENZE POICHE' E' 0 ALTRIMENTI DA' ERRORE
four1fit=noise(freq1[1:fourier1.size//2], params1[0], params1[1], params1[2])
four2fit=noise(freq2[1:fourier2.size//2], params2[0], params2[1], params2[2])
four3fit=noise(freq3[1:fourier3.size//2], params3[0], params3[1], params3[2])


#Grafico normale e fit nei 3 casi
# NB ESCLUDI IL PRIMO VALORE DELLE FREQUENZE POICHE' E' 0 ALTRIMENTI DA' ERRORE
plt.plot(freq1[1:fourier1.size//2], np.absolute(fourier1[1:fourier1.size//2])**2, color='violet')
plt.plot(freq1[1:fourier1.size//2],four1fit, color='red')
plt.title('Fit 1', color='red')
plt.title('Non fit 1', color='violet')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()

plt.plot(freq2[1:fourier2.size//2], np.absolute(fourier2[1:fourier2.size//2])**2, color='limegreen')
plt.plot(freq2[1:fourier2.size//2],four2fit, color='green')
plt.title('Fit 2', color='green')
plt.title('Non fit 2', color='limegreen')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()

plt.plot(freq3[1:fourier3.size//2], np.absolute(fourier3[1:fourier3.size//2])**2, color='yellow')
plt.plot(freq3[1:fourier3.size//2],four3fit, color='green')
plt.title('Fit 3', color='green')
plt.title('Non fit 3', color='yellow')
plt.xscale('log') #scala logaritmica sia per la x che per la y
plt.yscale('log')
plt.show()


