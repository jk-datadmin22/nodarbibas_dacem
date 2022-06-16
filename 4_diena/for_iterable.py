iepirkumi = ["sviests", "krējums", "piens", "biezpiens", "olas"]

print("Saraksta garums ir", len(iepirkumi))

for i in range(len(iepirkumi)):
    print(iepirkumi[i])
print("==================================")

for produkts in iepirkumi:
    print(produkts)
print("==================================")

vards = "Brīnumzeme"
for burts in vards:
    print(burts, end = "-")
print()
print("==================================")

vards = "Brīnumzeme"
for burts in vards:
    if burts == "e":
        print("Atradu e")
    print(burts, end = "-")
print()
print("==================================")


