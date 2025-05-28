
import random

ism = input()
familiya = input()

x = random.randint(0,50)
x1 = f"{ism}.{familiya}"
x2 = f"{ism}_{familiya}"
x3 = f"{ism[0]}{familiya}{x}"
x4 = f"{ism}{familiya[0]}"

print(x1)
print(x2)
print(x3)
print(x4)
