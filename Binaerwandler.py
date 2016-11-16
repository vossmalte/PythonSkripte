# tool translating str to binary and reverse
# MV 20140927
def inttobyte(z:int=0):
    "returns a list representing a byte"
    byte=[]
    for i in range(7,-1,-1):
        pot=2**i
        if z>=pot:
            z-=pot        # zahl verringern
            #print(str(pot)+" "+str(i)+" "+str(z))
            byte.append(1)
        else:
            byte.append(0)
    return byte

def bytetoint(byte):
    "returns unicode number of a binary code - accepting str and list"
    if type(byte)==str:
        string=byte
        byte=[]
        for i in string:
            byte.append(int(i))  
    z=0
    #byte.reverse
    exp=7
    for i in byte:
        z+=i*(2**exp)
        exp-=1
    return z

def strtobinlist(s:str="Message"):
    "returns 2-dimensional list of a string in bin code"
    liste=[]
    for i in s:
        liste.append(inttobyte(ord(i)))
    return liste

def listtostr(l:list=[[0,0,0,0,0,0,0,0]]):
    "returns binary code as string - better for copy and paste"
    s=""
    for i in l:
        for j in i:
            s+=str(j)
    return s
            
def readMSG(code:str="01000001"):
    "returns readable msg"
    code=code.replace(" ","")   # leerzeichen löschen
    runs=int(len(code)/8)        # anzahl der Bytes in der Kette (=Stringlänge)
    msg=""
    for i in range(0,runs):
        s=""
        for j in range(0,8):
            s+=code[i*8+j]    
        msg+=chr(bytetoint(s))
    return msg

def sendMSG(msg:str="Merry Christmas"):
    "returns bin-code"
    return listtostr(strtobinlist(msg))

if __name__=="__main__":
    #inttobin()
    #print(bytetoint(inttobyte(int(input()))))
    #print(listtostr(strtobinlist()))
    
    pass
