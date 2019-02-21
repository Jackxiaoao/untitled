import random
a = []
c = []
for i in range(50):
    b = random.randint(-10, 10)
    if b > 0 :
        a.append(b)
    elif b < 0 :
        c.append(b)
print("是正数的为:",a)
print("是负数的为:",c)



