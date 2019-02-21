import random
b = []
c = []
d = 0
for i in range(20):
    a = random.randint(0, 100)
    b.append(a)

print(b)
for i in range(20):

    if (b[(i-1) % 2 == 0]):
        c.append(b)
print(c)
