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
    print(i, end = " ")
print()
print("==================================")

#3. uzdevums
#Saskaiti visus skaitļus intervālā no 10 - 29, kas dalās ar 3.
summa = 0
for i in range(10, 29):
    if i % 3 == 0:
        print(i, end = "\t")
        summa = summa + i
        print(summa)
print()        
print("==================================")

#4. uzdevums
#Izveido programmu, kas izdrukā skaitļus no 1 līdz 100, bet skaitļu vietās, kas dalās ar:
# 3 tiek izdrukāts vārds "Bum",
# 5 tiek izdrukāts vārds "Rum",
# 3 un 5 tiek izdrukāts vārds "BumRum"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("BumRum", end = " ")
    elif i % 3 == 0:
        print("Bum", end = " ")
    elif i % 5 == 0:
        print("Rum", end = " ")
    else: 
        print(i, end = " ")

print()        
print("==================================")

# 6. uzdevums
# Izveido programmu, kas izdrukā zemāk esošo piemēru. Jāizmanto cikls-ciklā.

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(1, 10):
    for j in range(i):
        print(i, end="")
    print()
print("==================================")


# 7. uzdevums
# Izveido programmu, kas izdrukā zemāk esošo piemēru. Jāizmanto cikls-ciklā.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

rows = 4
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

print("==================================")

# number of rows
# rows = 5
# for i in range(0, rows):
    # nested loop for each column
    # for j in range(0, i + 1):
        # print star
        # print("*", end=' ')
    # new line after each row
#     print("\r")
# rows = 4
# for i in range(rows + 1, 0, -1):
    # nested reverse loop
    # for j in range(0, i - 1):
        # display star
    #     print("*", end=' ')
    # print("\r")

for i in range(5):
    for j in range(i + 1):
        print("*", end=' ')
    print()

for i in range(5, 0, -1):
    for j in range(i - 1):
        print("*", end=' ')
    print()

print("==================================")

