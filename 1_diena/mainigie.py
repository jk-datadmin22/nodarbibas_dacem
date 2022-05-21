# mainīgie
# mainīgā nosaukums
# mainīgā vērtība
# mainīgā datu tips

vards = "Dace" # mainīgā nosaukums ir vards, mainīgā nosaukums ir Dace
print(type(vards))  # mainīgā datu tips ir <class 'str'> jeb string (simbolu virkne)

# vienādības zīme = ir operators - sauc par piešķiršanas operatoru
uzvards = "Mušperte"
vertejums = 10
temperatura = 23.4
irBrilles = True

print(uzvards)
print(vertejums)
print(temperatura)
print(irBrilles)

print(type(uzvards)) # datu tips str - string, jeb simbolu virkne
print(type(vertejums)) # datu tips int - integer, jeb veseli skaitļi
print(type(temperatura)) # datu tips float - float, jeb racionāli skaitļi (ar komatiem, ko apzīmē ar punktu)
print(type(irBrilles)) # datu tips bool - boolean, vērtība ir True vai False

skaitlis = 5 # šis ir skaitlis, ko var izmantot matemātiskās darbībās
otrsSkaitlis = "7" # Šī ir simbolu virkne, ko neuztver kā skaitli

print(skaitlis)
print(otrsSkaitlis)

# Mainīgo nosaukumi (vadlīnijas)
# - mainīgo nosaukumi jāveido tādu, lai tas parādītu, ko tas satur
# - jāizvairās no mainīgo nosaukumiem, kas satur tikai vienu burtu, piem., x, y, z.....
# - mainīgo nosaukumā var būt cipars, bet mainīgā nosaukums nevar sākties ar cipru
vards1 = "Dace"
vards2 = "Māris"
# 1vards = "Pēteris" - šādi nevar

# mainīgo nosaukumus jāsāk ar mazo burtu, ja tas satur vairākus vārdus izmanto camelCase
# camelCaseStyle = "stils"
# snake_case_style - "stils"
# izmanto vienu vai otru, bet tos nekombinēt

# - ja veidojam konstantes vai mainīgos, kas satur vienu vērtību, tad lieto visus lielos burtus un atstarpē apakšsvītru
GRAVITACIJAS_PAATRINAJUMS = 9.8

# - mainīgo nosaukumu veidošanā neizmanto mīkstinājuma zīmes un garumzīmes un atstarpes
# vārds = "123" - šādi nedarīt!!!

mansVards = "Pēteris"
mansVards = "Juris"

print(mansVards)

print(vards, uzvards, vertejums, irBrilles)

print("Vārds:", vards)
print("Uzvārds:", uzvards)

print("Vārds:", vards, "Vērtējums:", vertejums)
print("Uzvārds:", uzvards)

print("Vārds: {vards}, Uzvārds: {uzvards}, Vērtējums: {vertejums}")
print(f"Vārds: {vards}, Uzvārds: {uzvards}, Vērtējums: {vertejums}")

print("Vārds: {}, Uzvārds: {}, Vērtējums: {}" .format(vards, uzvards, vertejums))


