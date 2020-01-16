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


# Exercice 5.2: Boucle et jours de la semaine

jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

print("Solution 1")

for day in jours[0:5]:
    print("Les jours de la semaine sont {}.".format(day))

print("Solution 2")

for day in jours[5:7]:
    print("Les jours du week-end sont {}.".format(day))

print("Solution 3")

i = 5
while i <= 6:
    print("les jours du week-end sont {}.".format(jours[i]))
    i = i +1

# Exercice 5.3: Nombres de 1 a 10 sur une ligne

for n in range(1, 11):
    print(n, end=" ")


# Exercice 5.4: Nombres pairs et impairs

impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17]
pair = []
for z in impairs:
    p = z + 1
    print(p)
    pair.append(p) # Alternative: pair.append(n+1)


# Exercice 5.5: Calcul de la moyenne

notes = [14, 9, 6, 8, 12]
somme = 0

for y in notes:
    somme = somme + y

moyenne = somme/len(notes)
print("Cet etudiant a une moyenne de {:.2f}.".format(moyenne))
