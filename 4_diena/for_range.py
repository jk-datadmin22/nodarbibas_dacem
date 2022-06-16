# cikli ļauj atkārtot un atkārtoti izpildīt dažādas darbības

for i in range(5):
    print(i)

print("==================================")

for i in range(-5, 5):
    print(i)

print("==================================")

for i in range(5, -5, -1):
    print(i)

print("==================================")

for i in range(10, 30, 3):
    print(i)

print("==================================")

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")

    print()
    
print("==================================")
