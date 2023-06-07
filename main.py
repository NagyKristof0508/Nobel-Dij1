class Dijazottak:
    def __init__(self, adatsor):
        reszletek=adatsor.split(';')
        self.ev=int(reszletek[0])
        self.nev=reszletek[1]
        self.SzuletesHalalozas=reszletek[2]
        self.orszagkod=reszletek[3]

    def __str__(self):
        return f"Év: {self.ev}, Díjazott: {self.nev}"

    

finp=open("orvosi_nobeldijak.txt", mode="rt", encoding="utf-8")
adatsorok=finp.read().split("\n")
finp.close()

dijazottemberek=[]
for i in range(1, len(adatsorok), 1):
    if adatsorok[i] != "":
        dijazott=Dijazottak(adatsorok[i])
        dijazottemberek.append(dijazott)

#hány ember él
elember=0
for item in dijazottemberek:
    if item.SzuletesHalalozas[1]=="":
        elember+=1

print(f"Összesen {elember}db ember él a díjazottak közül")

#hány díjazott van

db=len(dijazottemberek)
print(f"Összesen {db}db ember van")

#melyik volt az utolsó év

maxev=dijazottemberek[0]
for item in dijazottemberek:
    if item.ev > maxev.ev:
        maxev=item

print(f"Az utolsó év: {maxev}")

#melyik országból hány ember volt

GB=0
CH=0
USA=0
S=0
D=0
F=0
masorszag=0

for item in dijazottemberek:
    if item.orszagkod== "GB":
        GB+=1
    elif item.orszagkod == "CH":
        CH+=1
    elif item.orszagkod == "USA":
        USA+=1
    elif item.orszagkod == "S":
        S+=1
    elif item.orszagkod == "D":
        D+=1
    elif   item.orszagkod == "F":
        F+=1
    else:
        masorszag+=1

print(f"Statisztika:\n GB={GB}\n CH={CH}\n USA={USA}\n S={S}\n D={D}\n F={F}\n Más országok: {masorszag} ")