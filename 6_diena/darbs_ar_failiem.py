saraksts = ["Dace", "Anna", "Krista"]

#režīmi - r - lasīšana, w - rakstīšana (izdzēš visu saturu un raksta pa jaunam), 
# a - pievienošana (pieliek jauno teksta verisiju klāt vecajai galā)
with open("dati.txt", "w", encoding="utf-8") as fails:
    fails.write("Esi sveika, Dace!\n")
    fails.write("Šodien saulains laiks.\n")
    #fails.writelines(saraksts)
    fails.write("\n".join(saraksts))
    fails.write("\n")

#nolasīt visu failu vienā simbolu virknē
with open("dati.txt", "r", encoding="utf=8") as fails:
    saturs = fails.read()
print(saturs)

# lasīt pa rindiņai
with open("dati.txt", "r", encoding="utf=8") as fails:
    teksts1 = fails.readline()
    teksts2 = fails.readline()

print(teksts1)
print(teksts2)


with open("dati.txt", "r", encoding="utf=8") as fails:
    rindina = fails.readline()
    while rindina:
        print(rindina)
        rindina = fails.readline()

with open("dati.txt", "r", encoding="utf=8") as fails:
    for rindina in fails.readlines():
        print(rindina)
     
with open("dati.txt", "r", encoding="utf=8") as fails:
    rindinas = fails.readlines()
    #print(rindinas)

    for rindina in rindinas:
        print(rindina)
