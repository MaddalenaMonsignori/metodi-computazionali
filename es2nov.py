import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate
from scipy import optimize

df=pd.read_csv('/home/mm010044/Scaricati/metodi-computazionali/esercitazione4/fit_data.csv') #il metodo read di pandas apre il file csv con pathname quello tra ' '
print(df) #printo la tabella per vedere nomi colonne

array_y=df['y'] #immagazzina nell'array_y i dati presenti sulla colonna 'y' della tabella df
array_x=df['x'] #immagazzina nell'array_x i dati presenti sulla colonna 'x' della tabella df
log_x=np.log(array_x)

#Visto che sulle y ho il numero di conteggi(che in generale segue una distribuzione poissoniana), l'errore su ciascun conteggio sara' l'errore poissoniano dato dalla radice del numero conteggiato
err_y=np.sqrt(array_y)


#Definisco la funzione gaussiana che ha come argomento un array x e i parametri liberi media, sd, e coeff di normalizzazione da fittare successivamente
def gaussiana_lognorm(x, m ,s, coeff):
#serve che media, sigma e coeff siano parametri liberi altrimenti il fit non fa nulla
#coeff e' la y max ed e' all'incirca 100(lo vedi dal grafico appena sotto)--> e'il coeff di normalizzazione dei dati che io non conosco poiche' in questo caso ho una distribuzione di dati e non una distribuzione di probabilita'(ottengo la  distribzuione di probabilita' dividendo la gaussiana lognormale per il coeff di normalizzazione che equivale all'area sottesa alla curva dei dati) --> se coeff=1/radice(2pigreco) ho la gaussiana normalizzata a 1
    gaus=np.zeros(len(x))
    for i in range(len(x)):
        gaus[i]=coeff*math.exp(-0.5*((np.log(x[i])-m)/s)**2) #restituisce un array
    return gaus


#Faccio il grafico del numero conteggiato(array_x)) in funzione del numero di conteggi(array_y) con relativo errore (non verra' una distribuzione gaussiana poiche' su asse x non c'e' il log(x) ma solo la x data da fit_data.csv)    
plt.errorbar(array_x, array_y, err_y, color='salmon', fmt='o-')
plt.xlabel('Numero conteggiato')
plt.ylabel('Numero di conteggi')
plt.show()


#Faccio il grafico della distribuzione gaussiana (non fittata) che ha su asse x il logaritmo dei valori di x dati dal file fit_data.csv()(visto che so di avere distribuzione lognormale) e sulle y i valori dati dal file fit_data.csv (e contenuti in array_y)
plt.errorbar(log_x, array_y, err_y, color='royalblue', label='Dati misurati')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#Faccio il fit dei dati contenuti in fit_data.csv con la funzione lognormale gaussiana_lognorm definita sopra
params, params_covariance = optimize.curve_fit(gaussiana_lognorm, array_x, array_y, sigma=err_y, absolute_sigma=True)
print('media ottimizzata: ', params[0], ' sd ottimizzata: ', params[1], ' coef di norm ottimizzato: ', params[2] ) # params e' un array che contiene i parametri liberi di gaussiana_lognorm cioe' media, sd e coeff ottimizzati dal fit
print('params_covariance:', '\n',   params_covariance) #params_convariance e' una matrice 3x3 che contiene sulla diagonale gli errori al quadrato(varianza) dei parametri ottimizzati
print('errore media ott, sd ott, coeff norm ott: ', np.sqrt(params_covariance.diagonal())) #calcolo gli errori dei parametri ottimizzati facendo la radice degli elementi della diagonale di params_covariance

#Calcolo le y fittate ovvero le y calcolate con l'ottimizzazione inserendo come argomenti della funzione gaussiana_lognorm i valori di media sd e coeff ottimizzati
yfit=gaussiana_lognorm(array_x, params[0], params[1], params[2])

#Plotto la curva fittata
plt.errorbar(log_x, yfit, err_y, color='red', label='Dati fittati')
plt.show()


#Calcolo Chi quadrato
# chi2
chi2 =  np.sum( (yfit - array_y)**2 /array_y ) 

# gradi di libertà
ndof = len(array_x)-len(params)

print('Chi2: ', chi2, '\n', 'Chi2 ridotto: ', chi2/ndof)

