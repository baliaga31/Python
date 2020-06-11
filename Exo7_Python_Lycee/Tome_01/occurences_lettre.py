#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3


def occurences_lettre(phrase):
    nb = 0
    for n in phrase:
        if n == "E":
            nb += 1
    return(nb)

print(occurences_lettre("ESPRIT ES TU LA"))
