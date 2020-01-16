#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# Exercice 5.1: Boucles de base

x = ['vache', 'souris', 'levure', 'bacterie']

print("Solution 1")

for i in x:
    print(i)


print("Solution 2")

for i in range(len(x)):
    print(x[i])


print("Solution 3")

i = 0
while i < len(x):
    print(x[i])
    i = i + 1
