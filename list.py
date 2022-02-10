import random


"""lista = [5,3,6,2,4,1]
van = False
i = 0
while i < len(lista) and not van:
if lista[i] % 3 == 0:
van = True
i+=1
if van:
print('Van a listában 3-al
osztható szám')
else:
print('Nincs a listában 3-al
osztható szám')

lista = [5,3,6,2,4,1]
min = lista[0]
for szam in lista:
if szam<min:
min = szam
print('A legkisebb elem: ', min)

lista = [5,3,6,2,4,1]
max = lista[0]
for szam in lista:
if szam>max:
max = szam
print('A legnagyobb elem: ', max)

lista = [5,3,6,2,4,1]
van = False
i = 0
while i < len(lista) and not van:
    if lista[i] % 3 == 0:
        van = True
        i += 1
        if van:
            print("Van a listában 3-al osztható szám")
        else:
            print("nincs")"""
"""import list

nyelvek = ["Python", "Turbo Pascal", "C", "Java"]
print(nyelvek.index("C"))
print(nyelvek.count("Turbo Pascal"))
print("Java" in nyelvek)
nyelvek.append("C##")
print(nyelvek)
nyelvek.insert(1,"JavaScipt")
print(nyelvek)
tantargyak = ["prog","matek","töri","hálózat","projekt"]
nyelvek.extend(tantargyak)
print(nyelvek)
orarend = tantargyak.copy()
print(orarend)
nyelvek.remove("C")
print(nyelvek)
nyelvek.pop(1)
print(nyelvek)
orarend.clear()
print(orarend)

torpek = ["Tudor","vigor","morgó","szundi","szende","hapci","kuka"]
torpek.sort()
print(torpek)

torpek.reverse()
print(torpek[2:])

#torp = input("kérek egy törp nevet")
#if torp in torpek:
 #   print("benne van a listában")
#else:
 #   print("nincs benne")

torpek.remove("szende")
print(torpek)

szereplok = ["Hófehérke","banya","herceg"]
mese = szereplok.copy()
mese.extend(torpek)
print(mese)

colors = ["piros","kék","sárga","piros","zöld","kék","fekete"]
szin = input("kérek egy színt:")
if szin in colors:
    print("van benne")
else:
    print("nincs benne")

#x = colors.count(szin)
#print(x)
#z = colors.index(szin)
#+print(z)

colors.append(szin)
print(colors)

def rendez():
    colors.sort()

print(colors)
rendez()
print(colors)

def hossz_szerint(a):
    return len(a)

nevek = []
for x in range(5):
    nev = input("?")
    nevek.append(nev)
    nevek.sort(key=hossz_szerint)
    nevek.sort(key=str.lower)
    print(nevek)


lista=[]
összeg=0
for x in range(15):
    y=random.randint(0,10)
    lista.append(y)
    összeg+=y
    print('Indexe :',x,'Érték :',y)
print(összeg)
print(lista)"""

list = [6,4,3,6,1,7]

van = False
i = 0
while i < len(list) and not van:
    if list[i] % 3 == 0:
        van = True
    i+=1

if van:
    print("van")
else:
    print("nncs")

