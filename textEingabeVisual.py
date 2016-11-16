# Skript zur visuellen Texteingabe
from visual import *

def textEingabe(prompt="Please insert username here:"):
    "Returns a string input by the user in the visual window"
    scene.range=8
    f=label(pos=(0,2,0),text=prompt)
    i=label(pos=(0,0,0))
    string=""
    while True:
        if scene.kb:
            k=scene.kb.getkey()
            if k=="backspace":
                string=string[0:len(string)-1]          # String verkürzen
            elif k=="\n":
                i.visible=False;f.visible=False
                del(i);del(f)
                return string
            else:   # keine Sondertaste
                if len(string)<15:
                    string+=k
            i.text=string
            
            


if __name__=="__main__":
    print(textEingabe())
    exit(0)
