#!/usr/bin/env python

"""
    Codage d'un message en langue Leet Speak (1337 Sp34k)
    Version 6 Finale (on traite le message original)
"""

TEST_MESSAGE = "Bienvenue dans le monde de 1337 !"
SUBSTITUTIONS = [['a','4'], ['e','3'], ['l','1'], ['o','0'], ['t','7']]

### Section des fonctions
def coder_message(message, substitutions):
    """
        Traite d'une chaine transmise et applique des substitutions de lettres
        d'apres une liste d'elements. Chaque element est une liste de longueur 2 (ancien, nouveau)
    """

    for s in substitutions:
        vcar = s[0]
        ncar = s[1]
        message = message.replace(vcar, ncar)
        print("Texte converti = " + message)
    print("Je sors de coder_message()")
    return message

### Section de test dans main
message = raw_input("Message que je doit crypter : ")
txt_converti = coder_message(message, SUBSTITUTIONS)
print("Tu avais saisi ceci :  " + message)
print("Le codage donne ceci : " + txt_converti)