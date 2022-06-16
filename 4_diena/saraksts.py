# kā masīvs

iepirkumi = ["sviests", "krējums", "piens", "biezpiens", "olas"]
#elementi       0           1           2       3           4
#elementi = indeksi
#print(type(iepirkumi))
print(iepirkumi)
print(iepirkumi[2])

iepirkumi.append("eļļa")
# pieliek galā šādu elementu
print(iepirkumi)

iepirkumi.remove("piens")
# noņem šādu elementu
print(iepirkumi)

iepirkumi.pop()
# nodzēš pēdējo saraksta elementu
print(iepirkumi)

iepirkumi.pop(0)
# nodzēš elementu ar norādīto indexa numuru
print(iepirkumi)

index = iepirkumi.index("olas")
print(index)

if "biezpiens" in iepirkumi:
    print("Jā, biezpiens ir iepirkumos!")

if "pica" in iepirkumi:
    print("Jā, pica ir iepirkumos!")
else: 
    iepirkumi.append("pica")
    print(iepirkumi)


print("Saraksta garums ir", len(iepirkumi))
print(iepirkumi)

iepirkumi.sort()
# sakārto sarakstu alfabēta vai cipariskā secībā
print(iepirkumi)

