# 1. uzdevums
# Izveidot programmu, kas prasa lietotājam ievadīt vairākus skaitļus - 
# ievade beidzas, kad lietotājs ir ievadījis 0. 
# Aprēķināt no visiem ievadītajiem pāra skaitļiem vidējo aritmētisko. (0- nav ne pāra, ne nepāra)
saraksts = []
# # len(saraksts) !=0
skaitli = int(input("Ievadi skaitli:"))

while skaitli !=0:
    skaitli = int(input("Ievadi skaitli:"))
    if skaitli == 0:
        break

    if skaitli %2 == 0:
        saraksts.append(skaitli)
        print(saraksts)
    
    print(skaitli)

print("===================================================")

summa = 0
skaits = 0

while True:
    skaitlis = int(input("Ievadi skaitli:"))
    if skaitlis == 0:
        break

    if skaitlis % 2 == 0:
        summa = summa + skaitlis
        skaits = skaits + 1

if skaits != 0:
    print("Vidējais ir", summa / skaits)
else:
    print("Netika ievadīts neviens pāra skaitlis!")

print("===================================================")

saraksts = []
while True:
    skaitlis = int(input("Ievadi skaitli: "))
    if skaitlis == 0:
        break
    if skaitlis %2 ==0:
        saraksts.append(skaitlis)

summa = sum(saraksts)
if len(saraksts) != 0:
    average = summa / len(saraksts)
    print(average)
else:
    print("Tukšums")

print("===================================================")

# 2. uzdevums
# Izveidot programmu, kas prasa lietotājam ievadīt vairākus unikālus skaitļus 
# (ja skaitlis jau ir iepriekš ievadīts, tad to neiekļauj) - 
# ievade beidzas, kad lietotājs ir ievadījis 0. 
# Izvadīt visus skaitļus un tad lielāko ievadīto skaitli un mazāko ievadīto skaitli.

saraksts = []
while True:
    skaitli = int(input("Ievadi skaitli:"))
    if skaitli == 0:
        break

    if skaitli not in saraksts:
        saraksts.append(skaitli)
    
print(saraksts)

sort = sorted(saraksts, reverse=True)
print(sort)
print("Lielākais skaitlis: ", sort[0])
print("Mazākais skaitlis: ", sort[len(sort) - 1])

mazakais = saraksts[0]
for i in saraksts:
	if i<mazakais:
		mazakais=i
print("Mazākais skaitlis: ", mazakais)

lielakais = saraksts[0]
for i in saraksts:
	if i>lielakais:
		lielakais=i
print("Lielākais skaitlis: ", lielakais)

# 3. uzdevums
# Izveido programmu, kur lietotājam ir jāuzmin datora iedomātais skaitlis 
# (no 1 līdz 20). Lietotājs min tik ilgi, kamēr ir atminējis skaitli, 
# beigās parāda tekstu "Apsveicam ar uzvaru!" un rezultātu (minējuma skaitu).

import random

skaitlis = random.randint(1, 20) #datora iedomātais skaitlis
meginajumi = 0

while True:
    try:
        minejums = int(input("Ievadi skaitli, kuru gribi uzminēt (0 - iziet):"))
    except:
        print("Ievade ir nepareiza...")
        continue

    meginajumi = meginajumi + 1

    if minejums == 0:
        print("Man žēl, ka Tu padevies!")
        break

    if minejums == skaitlis:
        print("Apsveicam ar uzvaru!")
        print("Lai uzvarētu, Tev tas prasīja ", meginajumi, "mēģinājumus.")
        break
    else:
        if minejums > skaitlis:
            print("Tavs minējums ir par augstu!")
        else:
            print("Tavs minējums ir par zemu!")
        print("Mēģini vēlreiz...")








