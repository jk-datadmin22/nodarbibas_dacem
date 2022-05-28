# 1.uzdevums
# Uzrakstiet programmu, kas prasa lietotājam ievadīt savu vārdu, 
# ja tas ievada vārdu, Bond, tad izdrukājiet uz ekrāna "Esi sveicināts 007", 
# ja cits tad "Esi sveicināts, VARDS", kur VARDS ir lietotāja ievadītais vārds.

vards = str(input("Kāds ir Tavs vārds? "))

if vards == "Bond":
    print("Esi sveicināts 007")
else:
    print("Esi sveicināts,", vards)


print("==================================")
# 2.uzdevums
# Izveido programmu, kas nosaka vai lietotāja ievadītais skaitlis ir pāra vai nepāra.

skaitlis = int(input("Lūdzu ievadi skaitli: "))

if (skaitlis % 2) == 0:
    print("Šis ir pāra skaitlis!")
else:
    print("Šis ir nepāra skaitlis!")


print("==================================")
# 3.uzdevums
# Lietotājs ievada savu vērtējumu programmēšanā izvadīt vārdisko vērtējumu (izcili, teicami utt.)

atzime = int(input("Kāda ir Tava atzīme? "))

if atzime == 10:
    print("izcili")
elif atzime == 9:
    print("teicami")
elif atzime == 8:
    print("ļoti labi")
elif atzime == 7:
    print("labi")
elif atzime == 6:
    print("gandrīz labi")
elif atzime == 5:
    print("viduvēji")
elif atzime == 4:
    print("gandrīz viduvēji")
elif atzime == 3:
    print("vāji")
elif atzime == 2:
    print("ļoti vāji")
elif atzime == 1:
    print("ļoti, ļoti vāji")
else:
    print("Šādas atzīmes nav!")

print("==================================")
# 4.uzdevums
# Izveido gāzes kalkulatoru. 
# Lietotājs ievada pateriņu (kWh) programma izvada cik ir jāmaksā. 
# Jāizmanto Latvijas gāzes cenu tabula

# ja tavs patēriņš ir tik līdz tik, tev ir jāmaksā tik reiz tavs patēriņš

paterins = float(input("Lūdzu ievadi savu dabasgāzes gada patēriņu kWh:"))

if paterins <= 2635:
    print("Gāzes cena par gadu ir EUR", round(paterins * 0.1045819, 4))
elif paterins >= 2635.1 and paterins <= 5269:
    print("Gāzes cena par gadu ir EUR", round(paterins * 0.0917141, 4))
elif paterins >= 5269.1 and paterins <= 63227.9:
    print("Gāzes cena par gadu ir EUR", round(paterins * 0.0762993, 4))
elif paterins >= 63228 and paterins <= 263450:
    print("Gāzes cena par gadu ir EUR", round(paterins * 0.0762993, 4))

