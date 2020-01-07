#!/usr/bin/python3

# Exercice 3.2: Poly-A

a = "A" * 20

print(a)

# Exercice 3.3: Poly-A et poly-GC

b = "A" * 20 + "GC" * 20

print(b)

# Exercice 3.4: Ecriture formatee

a = "Salut"
b = 102
c = 10.318

print("{:s}, {:d}, {:.2f}".format(a, b, c))

# Exercice 3.5: Ecriture formatee 2

perc_GC = ((4500 + 2575)/14800)*100

print("Le pourcentage de GC est {:<6.0f} %".format(perc_GC))
print("Le pourcentage de GC est {:<6.1f} %".format(perc_GC))
print("Le pourcentage de GC est {:<6.2f} %".format(perc_GC))
print("Le pourcentage de GC est {:<6.3f} %".format(perc_GC))
