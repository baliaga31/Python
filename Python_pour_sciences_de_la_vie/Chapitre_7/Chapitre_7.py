#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# Exercice 7.1: Moyenne des notes


#filin = open("notes.txt", "r")

#lines = filin.readlines()
#for line in lines:
#    print(line)

#filin.close()

notes = []

with open("notes.txt", "r") as filin:
    for line in filin:
        notes.append(float(line))

somme = 0.0
for note in notes:
    somme = somme + note

print("Moyenne : {:.2f}".format(somme/len(notes)))


# Exercice 7.2: Admis ou recale

notes = []

with open("notes.txt", "r") as filin:
    for line in filin:
        notes.append(float(line))

with open("notes2.txt", "w") as filout:
    for note in notes:
        if note > 10:
            mention = "Admis"
        else:
            mention = "Recale"
        filout.write("{:.1f} {}\n".format(note, mention))
