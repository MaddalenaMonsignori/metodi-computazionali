import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import csv
import pandas as pd



######## Definisco le funzioni

#Definisco la funzione V_in che ha come argomento t e restituisce 1 per valori pari di t e -1 per valori dispari di t
def V_in(t):
    if(int(t)%2==0): #devo trasformare t in int altrimenti l'operatore % non da' il risultato desiderato (i due numeri tra cui applico % devono essere interi
        return 1
    else:
        return -1
    

#Definisco una funzione che contiene il secondo membro dell'equazione differenziale in cui passo come parametro una funzione ff e la tratto come oggetto --> quando chiamero' eq_dif la funzione generica ff sara' sostituita da V_in (vedi qunado uso metodo .odeint)
def eq_dif(V_out, t , ff, RC):
    eq=(1/RC)*(ff(t)-V_out)
    return eq



####### Definisco array dei tempi

V0=0 #condizione iniziale eq diff
a=0 # inizio intervallo dei tempi
b=10 #fine intervallo dei tempi
N=1000 #numero di suddivisioni dell'intervallo dei tempi
passo=(b-a)/N #passo intervallo dei tempi
array_tempi=np.arange(a, b, passo) #array con tutti i valori dell'intervallo deitempi



###### Faccio il grafico di V_in

input=np.zeros(len(array_tempi)) #creo un array vuoto dove immagazzinero i risultati dati dalla chiamata della funzione V_in
for i in range(len(array_tempi)): #faccio un ciclo for dove applico V_in a ciascun valore dell'array dei tempi
    input[i]=V_in(array_tempi[i])

plt.title('V_in in funzione del tempo', color='red', fontsize=14)
plt.plot(array_tempi, input, color='red')
plt.show()



##### Definisco l'array delle soluzioni Vout prima come array vuoto e poi lo riempo applicando il metodo integrate.odeint rispettivamente per RC=1, RC=0.1, RC=0.01

Vout= np.empty(0)
Vout1=np.empty(0)
Vout2=np.empty(0)
Vout=integrate.odeint(eq_dif, V0, array_tempi, args=(V_in, 1)) #Calcola l'array delle soluzioni eq diff. L'ordine in cui scrivo i parametri e' importante --> come args c'e' la funzione V_in passata come parametro e RC
Vout1=integrate.odeint(eq_dif, V0, array_tempi, args=(V_in, 0.1))
Vout2=integrate.odeint(eq_dif, V0, array_tempi, args=(V_in, 0.01))



#### Grafico per RC=1

fig,ax = plt.subplots(figsize=(9,6))
plt.title('Vout in funzione del tempo (RC=1)', color='violet', fontsize=14)
plt.plot(array_tempi, Vout, color='violet')
plt.plot(array_tempi, input, color='red')
plt.xlabel('t')
plt.ylabel('Vout')
plt.show()
    
    

#### Grafico per RC=0.1

fig,ax = plt.subplots(figsize=(9,6))
plt.title('Vout in funzione del tempo (RC=0.1)', color='limegreen', fontsize=14)
plt.plot(array_tempi, Vout1, color='limegreen')
plt.plot(array_tempi, input, color='red')
plt.xlabel('t')
plt.ylabel('Vout')
plt.show()



#### Grafico per RC=0.01

fig,ax = plt.subplots(figsize=(9,6))
plt.title('Vout in funzione del tempo (RC=0.01)', color='yellow', fontsize=14)
plt.plot(array_tempi, Vout2, color='yellow')
plt.plot(array_tempi, input, color='red')
plt.xlabel('t')
plt.ylabel('Vout')
plt.show()


###### tabelle con dati: array dei tempi e Vout per RC=1, RC=0.1, RC=0.01

mydf=pd.DataFrame(columns=['Tempi', 'Vout (RC=1)','Vout (RC=0.1)','Vout (RC=0.01)'  ])
mydf['Tempi']=array_tempi
mydf['Vout (RC=1)']=Vout
mydf['Vout (RC=0.1)']=Vout1
mydf['Vout (RC=0.01)']=Vout2
print(mydf)

###### Converto la tabella in file.csv
mydf.to_csv('/home/mm010044/metodi-computazionali/Vout_t.csv')


