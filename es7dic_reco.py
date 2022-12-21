
'''Definisco una classe Hit in cui un oggetto di tipo Hit deve contiene informazioni su:
Id Modulo
Id Sensore
Time Stamp rivelazione
'''
class Hit():
    
    def __init__(self, id_modulo, id_sensore, time):
        self.id_modulo = id_modulo
        self.id_sensore = id_sensore
        self.time= time
    def __lt__(self, other):
        return self.time < other.time
    def __sub__(self, other):
        return self.time - other.time

'''Definisco la classe Event in cui un oggetto di tipo Event deve contiene informazioni su:
Numero di Hit
Time Stamp del primo Hit
Time Stamp dell'ultimo Hit
Durata temporale
Array di tutti gli Hit
'''

class Event():

    def __init__(self):
        self.num_hit = 0
        self.time_primo_hit = 0
        self.time_ultimo_hit = -1
        self.durata_tempo= -1
        self.array_hit=np.empty([])

#e' necessario inserire una funzione aggiorna event perche' nel costruttore init non so come passare come parametro un array e in piu' num_hit, time_primo_hit, time_ultimo_hit, durata_tempo dipendono dal contenuto dell'array quindi devo calcolarli
    def aggiorna_event(array):
        self.num_hit=self.num_hit+1
        self.array_hit=np.append(self.arrray_hit, h)
        self.time_primo_hit=self.array_hit[0].time
        self.time_ultimo_hit=h.time
        self.durata_tempo=h.time-self.array_hit[0]

#stampa le info su event
    def stampa_event():
        print('Numero di hit totali: ', self.num_hit)
        print('Istante del primo hit: ', self.time_primo_hit)
        print('Istante ultimo hit: ', self.time_ultimo_hit)
        print('Durata temporale: ', self.durata_tempo)
        print('Array hit: ', self.array_hit)
