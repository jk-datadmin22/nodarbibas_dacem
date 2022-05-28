"""
if <boolean loģika>: 
    komandas, 
    kas jāveic, 
    ja loģika ir True
else:
    komandas, kas
    jāveic, ja loģika
    ir False


if <boolean loģika>: 
    komandas, 
    kas jāveic, 
    ja loģika ir True


if <boolean loģika>: 
    komandas, 
    kas jāveic, 
    ja loģika ir True
elif <boolean loģika>:   #elif var būt vairāki
    komandas, kas
    jāveic, ja loģika
    ir True
else:  #nav obligāts
    komandas, kas
    jāveic, ja 
    viss iepriekšējais ir False

"""

vecums = int(input("Cik Tev gadu?"))

if vecums >= 18:
    print("Apsveicu, Tu esi pilngadīgs!")
else:
    print("Tev vēl jāpaaugas!")

if vecums >= 65:
    print("Tev laiks doties pensijā!")

# if vecums < 10:
#     print("Pirmā desmitgade!")
# else:
#     if vecums < 20:
#         print("Otrā desmitgade!")
#     else:
#         if vecums < 30:
#             print("Trešā demitgade!")
#         else:
#             .............        

if vecums < 10:
    print("Pirmā desmitgade!")
elif vecums < 20:
    print("Otrā desmitgade!")
elif vecums < 30:
    print("Trešā desmitgade!")
elif vecums < 40:
    print("Ceturtā desmitgade!")
else:
    print("Nevaru noteikt desmitgadi!")

# Saīsinātais pieraksts
print("Pilgadīgs") if vecums >= 18 else print("Paaudzies!")

