# print 1 tm 10 printten
# aanoassen zodat je alleen de even getallen krijgt
# nu deze getallen in een nieuwe variabele erbij tellen
getal = 0

for i in range(1,11):
    if (i % 2 == 0):
        getal += i
print(f"{getal}")

