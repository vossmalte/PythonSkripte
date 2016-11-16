#zeilen Lesen
all_erg=[]      #für Liste der Teilnehmer
f=open('ergebnisse.txt', 'r')
for line in f:
    st_erg=line.split("\t")[0].split(" ")   #Spieltagsergebnisse
    all_erg.append(st_erg)
    print(st_erg)

#print("\n\n\n")
#print(all_erg[1:])

teilnehmer=[]
for i in all_erg[1:]:
    for j in i:
        if j not in teilnehmer:
            teilnehmer.append(j)
print("\n\n\n\t Teilnehmende Teams:")
teilnehmer.sort()
for i in teilnehmer:
    print("'" + i + "' => 0,")
    
