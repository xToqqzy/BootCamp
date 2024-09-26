states = [(True, True), (True, False),  (False,True), (False, False)]

print("AND")
for a, b in states:
    result = a and b
    print (f"{a} + {b} = {result}")

print()


print("OR")
for a, b in states:
    result = a or b
    print(f"{a} + {b} = {result}")