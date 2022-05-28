import random

a = int(input("Введите сколько вариантов у вас будет: "))

b = []

for i in range(a):
    u = str(input("Введите " + str(i+1) + " из " + str(a) + ": "))
    b.append(u)


answer = random.randint(0, a-1)

print("Выпало: " + b[answer])
