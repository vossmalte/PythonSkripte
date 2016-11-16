# Diverse Möglichkeiten, Primzahlen zu errechnen

#from multiprocessing import Process
from time import clock          # Uhr-Modul zum Messen der Zeit
primzahl=[]
def jedemitjedem(max:int=50000):             # sehr langsam
    "dividiert jede Zahl mit jeder darunterliegenden Zahl..."
    primzahl=[]
    ts=clock()
    x = 2               
    while x < max:     
        y = 2           
        while y < x**5:        #nur bis hälfte, weil sonst anderer Teiler <2...
            if x % y == 0:  
                break       
            y += 1
        else:
            primzahl.append(x)  
        x += 1
    te=clock()
    print(te-ts)
    return primzahl


def jededurchPrimzahl(max:int=1000):
    "Division einer Testzahl durch die bisher bekannten primzahlen, aber nicht größer x**.5"
    primzahl=[]         #liste leer
    ts=clock()          #für zeitmessung
    x=3         #beginne test bei 3, nächstgrößere zur kleinsten bekannten Primzahl 2
    primzahl.append(2)      #Zwei als Kleinste bekannte Primzahl
    while x < max:           # primzahlen Bis... im Intervall [0;...]
        z=x**0.5                #Quadratwurzel des Dividenden
        for i in primzahl:      #gehe durch liste der bisher gefundenen primzahlen
            if i<=z:            #größter theoretischer Teiler ist die quadratwurzel
                if x%i==0:      #x lässt sich restlos durch eine primzahl teilen...
                    break       #nächste zahl ausprobieren
            else:               #divisor größer als wurzel von dividend...
                primzahl.append(x)      #an liste anfügen
                break           #nächste zahl ausprobieren
        x += 2                  #dividenden um 2 erhöhen
    te=clock()      #für zeitmessung
    print(te-ts)            #drucke zeitmessung
    print(len(primzahl))        #drucke anzahl der Primzahlen im o.g. intervall
    return primzahl


if __name__=="__main__":
    jededurchPrimzahl()
    

"""
liste bis max...
vielfache aus der liste löschen
"""


