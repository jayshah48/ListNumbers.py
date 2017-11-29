import random

def ListNumbers():
    abc = random.sample(range(1,20),10)
    print(abc)
    n = int(input("Enter value of n: "))
    xyz = [];
    for i in abc:
        if i < n:
            xyz.append(i)
    print(xyz);

ListNumbers()