#!/usr/bin/python3

# Exercice 4.1: Jours de la semaine

Jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print(Jours[0:5])
print(Jours[6:7])
print(Jours[-7:-2])
print(Jours[-2:])

# Exercice 4.2: Saisons

Hivers = ["Janvier", "Fevrier", "Mars"]
Printemps = ["Avril", "Mai", "Juin"]
Ete = ["Juillet", "Aout", "Septembre"]
Automne = ["Octobre", "Novembre", "Decembre"]

saisons = [Hivers, Printemps, Ete, Automne]

print(saisons[2])
print(saisons[1][0])
print(saisons[1:2])
print(saisons[:][1])

# Exercice 4.3: Table de multiplication par 9

table = list(range(0,91, 9))
print(table)

# Exercice 4.4: Nombres pairs

Pair = len(range(2, 10001, 2))
print(Pair)
