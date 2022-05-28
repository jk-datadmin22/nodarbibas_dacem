"""
== - salīdzināšanas operators, vai viens == vienāds ar otru
!= - salīdzināšanas operators vai ir nevienāds
<  - mazāks par
>  - lielāks par
<= - mazāks vai vienāds
>= - lielāks vai vienāds

"""

from lib2to3.pgen2.token import RIGHTSHIFT


sk1 = 13
sk2 = 7
sk3 = 7

print("sk1 == sk2", sk1 == sk2)
print("sk1 != sk2", sk1 != sk2)
print("sk1 < sk2", sk1 < sk2)
print("sk1 > sk2", sk1 > sk2)
print("sk1 <= sk2", sk1 <= sk2)
print("sk1 >= sk2", sk1 >= sk2)
print()
print("sk3 == sk2", sk3 == sk2)
print("sk3 != sk2", sk3 != sk2)
print("sk3 < sk2", sk3 < sk2)
print("sk3 > sk2", sk3 > sk2)
print("sk3 <= sk2", sk3 <= sk2)
print("sk3 >= sk2", sk3 >= sk2)
print()

vards1 = "Maris"
vards2 = "maris"
vards3 = "maris"

print("Maris == maris", vards1 == vards2)
print("maris == maris", vards3 == vards2)
print("visi mazie burti pārbaude", vards1.casefold() == vards2.casefold())
print("visi mazie burti pārbaude", vards1.lower() == vards2.lower())
print()

patiesiba = True
meli = False

print("patiesiba != meli", patiesiba != meli)

"""
AND - skatās vai abas puses ir True
OR  - skatās vai kāda no pusēm ir True

A      B        A and B     A or B     A == B
True   False    False       True       False
False  True     False       True       False
True   True     True        True       True
False  False    False       False      True

"""

sk4 = 1
sk5 = 2
sk6 = 3
sk7 = 3

print("Rezultāts AND", sk5 > sk4 and sk6 == sk7)
print("Rezultāts AND", sk5 < sk4 and sk6 == sk7)
print("Rezultāts OR", sk5 > sk4 or sk6 == sk7)
print("Rezultāts OR", sk5 < sk4 or sk6 == sk7)

