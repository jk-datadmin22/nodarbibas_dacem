# teksts = input()
# print(teksts)

# vards = input("Ievadi savu vārdu:")
# print(vards)

sk1 = input("Ievadi skaitli 1:")  # sk1 = "5"
sk2 = input("Ievadi skaitli 2:")  # sk2 = "7"
print("Summa ir", sk1 + sk2)
print(type(sk1))
print(type(sk2))

print("================================")
sk1 = int(input("Ievadi skaitli 1:"))  # sk1 = "5"
sk2 = int(input("Ievadi skaitli 2:"))  # sk2 = "7"
print("Summa ir", sk1 + sk2)
print(type(sk1))
print(type(sk2))

print("================================")
cena = float(input("Ievadi cenu:"))
valuta = input("Ievadi valūtu:")

print(cena, valuta)
print(type(cena), type(valuta))

print ("===============================")
precuSkaits = int(input("Ievadi preču skaitu:"))
precuVeids = (input("Ievadi preču veidu:"))

print("Noliktavā ir", precuSkaits, precuVeids, end=".\n")

print("=================================")
mala1 = int(input("Ievadi vienas malas garumu:"))
mala2 = int(input("Ievadi otras malas garumu:"))
print("Taisnstūra laukums ir", mala1 * mala2)

print("==============================")
Celsius = int(input("Ievadi temperatūru Celsija grādos: "))
Fahrenheit = 9.0/5.0 * Celsius + 32
print("Temperatūra Farenheitos ir", round(Fahrenheit, 4))

print("===============================")
diametrs = int(input("Ievadi riņķa līnijas diametru: "))
print("Riņķa līnijas garums ir", round(3.14 * diametrs))





