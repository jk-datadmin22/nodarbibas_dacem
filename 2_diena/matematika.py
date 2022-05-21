import math

# + saskaitīt
# - atņemt
# * reizināt
# / dalīt
# // dalīt bez atlikuma
# % modulis = atlikums pēc dalīšanas
# ** kāpināšana


print(5 + 3)
print(7 - 4)
print("=================")

sk1 = 13
sk2 = 5

print("sk1 =", sk1, "sk2 =", sk2)
print("Summa ir", sk1 + sk2)
print("Starpība ir", sk1 - sk2)
print("Reizināšana ir", sk1 * sk2)
print("Dalīšana ir", sk1 / sk2)
print("Dalīšana bez atlikuma ir", sk1 // sk2)
print("Modulis ir", sk1 % sk2)
# 13 // 5 => 2
# 2 * 5 = 10
# 13 - 10 ==> 3 <==

print("Kāpināšana ir", sk1 ** 2)

rezultats = 9 / 7
print("Rezultāts", rezultats)
print("Rezultāts", round(rezultats, 4))

sk3 = 225
print("Kvadrātsakne", math.sqrt(sk3))

print("Pi skaitlis", math.pi)
print("Pi skaitlis", round(math.pi, 2))

print()
# Uzdevums 1
# Dotas divas taisnstūra malas 4, 7 aprēķināt taisnstūra laukumu.
mala1 = 4
mala2 = 7
print("Taisnstūra laukums ir", mala1 * mala2)

# Uzdevums 2
# Dota temperatūra Celsija grādos 21, cik tas būs Fārenheiti?
Celsius = 21
Fahrenheit = 9.0/5.0 * Celsius + 32
print("Temperatūra Farenheitos ir", round(Fahrenheit, 4))

# Uzdevums 3
# Dots riņķa līnijas diametrs 7, aprēķināt riņķa līnijas garumu.
# C = pi * diametrs
diametrs = 7
print("Riņķa līnijas garums ir", round(math.pi * diametrs, 4))

