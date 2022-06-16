#1. uzdevums
#Izdrukāt visas valstis vienā rindiņā. valstis = ['Latvija','Lietuva','Igaunija']

valstis = ["Latvija", "Lietuva", "Igaunija"]
print(valstis)

for i in range(len(valstis)):
    print(valstis[i])
print("==================================")

#2. uzdevums
#Izdrukāt skaitļus no 50 līdz 25. (ievēro secību!)

for i in range(50, 24, -1):
    print(i)

print("==================================")

#3. uzdevums
#Saskaiti visus skaitļus intervālā no 10 - 29, kas dalās ar 3.

for i in range(10, 29):
    if i % 3 == 0:
        print(i)
    
print("==================================")

#4. uzdevums
#Izveido programmu, kas izdrukā skaitļus no 1 līdz 100, bet skaitļu vietās, kas dalās ar:
# 3 tiek izdrukāts vārds "Bum",
# 5 tiek izdrukāts vārds "Rum",
# 3 un 5 tiek izdrukāts vārds "BumRum"

for i in range(1, 101):
    
     if i % 3 == 0:
        print("Bum", end = " ")

        if i % 5 == 0:
            print("Rum", end = " ")

            if i % 3 == 0 & i % 5 == 0:
                print("BumRum", end = " ")

        print(i, end = " ")
