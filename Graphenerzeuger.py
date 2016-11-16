# Zu den Programmieren Abschlussaufgaben WS 1516
# Zufällig Graphen

from random import random

class Erzeuger:
    def __init__(self, numberOfVertices=10):
        vertices=""
        edges=""
        for i in range(numberOfVertices):
            I=chr(i+65)
            vertices+=I+"\n"
            for j in range(i + 1, numberOfVertices):
                J=chr(j+65)
                route=int(random()*100)
                time=int(random()*600)
                if route>30 and time>200 and route+time>350:
                    edges+=I+";"+J+";"+str(route)+";"+str(time)+"\n"

        print (vertices + "--\n"+edges)
                    
                    
        
