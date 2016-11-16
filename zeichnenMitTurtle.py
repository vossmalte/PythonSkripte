from turtle import *

def farn(weg):
    "Methode"
    if weg>1:
        pencolor("green")
        fd(weg)
        lt(25)
        #linker teil
        pencolor("red")
        farn(weg*.5)
        rt(35)
        #mittlerer teil
        pencolor("blue")
        farn(weg*.7)
        rt(25)
        #rechter teil
        pencolor("orange")
        farn(weg*.4)
        lt(35)
        bk (weg)
    else:
        fd(weg)
        bk(weg)





if __name__=="__main__":
#----------Standardbedingungen------------#
    reset()         #ertmal ein neues papierle
    speed(0);delay(0);ht()  #no animation
#----------Starteinstellungen---------------#
    pu()            #no drawing
    lt(90)          #links drehen
    bk(120)         #Rückwärts
    pd()            #draw!!!
#-----------ok, let´s go-------------------#
    farn(120)
    
    
