#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

def nombre_lettre(message):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nb = 0
    for n in message:
        if n in alphabet:
          nb += 1
    return nb

print(nombre_lettre("ESPRIT ES TU LA"))
