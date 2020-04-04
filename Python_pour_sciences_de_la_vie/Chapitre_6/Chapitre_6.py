#!/usr/bin/python3

# Chapitre 6: Tests

## Exercice 6.1: Jours de la semaine

jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

for day in jours:
    if day == "Vendredi":
        print("Vendredi: C'est le week-end ce soir")
    elif day == "Samedi" or day == "Dimanche":
        print("{}: On travaille pas, sauf si on est passionne!".format(day))
    else:
        print("{}: Au boulot !".format(day))
    

## Exercice 6.2: Sequence complementaire d'un brin d'ADN

sequence = ["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
comp = []
comp2 = []

### Solution 1: use dictionary

dic = {"A": "T", "C":"G", "T":"A", "G":"C"}

for base in sequence:
    comp.append(dic[base])

print(sequence)
print(comp)

### Solution 2: use tests

for base in sequence:
    if base == 'A':
        comp2.append('T')
    if base == 'C':
        comp2.append('G')
    if base == 'T':
        comp2.append('A')
    if base == 'G':
        comp2.append('C')
        
print(comp2)


## Exercice 6.3: Minimum d'une liste

liste = [8, 4, 6, 1, 5]
mini = liste[0]

for x in liste:
    if x < mini:
        mini = x

print(liste)
print(mini)

## Exercice 6.4: Fréquence des acides aminés

prot = ["A","R","A","W","W","A","W","A","R","W","W","R","A","G"]

A_count = 0
R_count = 0
W_count = 0
G_count = 0

for aa in prot:
    print(aa)
    if aa == 'A':
        A_count += 1
    if aa == 'R':
        R_count += 1
    if aa == 'W':
        W_count += 1
    if aa == 'G':
        G_count += 1

print("Frequence A = {:.2f}".format(A_count/len(prot)))
print("Frequence W = {:.2f}".format(W_count/len(prot)))
print("Frequence R = {:.2f}".format(R_count/len(prot)))
print("Frequence G = {:.2f}".format(G_count/len(prot)))

#print(len(prot))


## Exercice 6.5: Notes et mention d'un étudiant

notes = [14, 9, 13, 15, 12]

print(max(notes))
print(min(notes))
somme = sum(notes)

moyenne = somme / 5
print(moyenne)

# la mention obtenue sachant que la mention est « passable » si la moyenne est entre 10 inclus et 12 exclus, « assez bien » entre 12 inclus et 14 exclus et « bien » au-delà de 14.


if  moyenne >= 10 and moyenne < 12:
    print("Passable")
elif moyenne >= 12 and moyenne < 14:
    print("Assez bien")
elif moyenne >= 14:
    print("Bien")
