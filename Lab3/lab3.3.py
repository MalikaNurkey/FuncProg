import random

num = random.randint(0, 9)
print(num)


num2 = random.randrange(1000, 10000, 2)
print(num2)

a = [10, 20, 30, 40]
for id, i in enumerate(a):
    a[id] = i + 5
print(a)