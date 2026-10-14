print("A B ORIGINAL REDUCIDA IGUALES")
for A in (False, True):
    for B in (False, True):
        original = (A and B) or (A and (not B)) or ((not A) and B)
        reducida = A or B
        print(int(A), int(B), int(original), int(reducida), int(original == reducida))

print("A B C ORIGINAL REDUCIDA IGUALES")
for A in (False, True):
    for B in (False, True):
        for C in (False, True):
            original = (not ((A or B) and (A or (not B)))) or ((not A) and C)
            reducida = not A
            print(int(A), int(B), int(C), int(original), int(reducida), int(original == reducida))
