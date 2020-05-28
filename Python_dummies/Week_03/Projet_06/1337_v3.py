#!/usr/bin/env python

"""
    Codage d'un message en langue Leet Speak (1337 Sp34k)
    Version 3 (Pour faire saisir le message pour 1 seule lettre)
"""

TEST_MESSAGE = "Bienvenue dans le monde de 1337 !"
TEST_SUBSTITUTIONS = [['e','3']]

### Section des fonctions
def coder_message(message, substitutions):
    """
        Traite d'une chaine transmise et applique des substitutions de lettres
        d'apres une liste d'elements. Chaque element est une liste de longueur 2 (ancien, nouveau)
    """

    for s in substitutions:
        vcar = s[0]
        ncar = s[1]
        converti = message.replace(vcar, ncar)
    return converti

### Section de test dans main
message = raw_input("Message que je doit crypter : ")
txt_converti = coder_message(message, TEST_SUBSTITUTIONS)
print(message)
print(txt_converti)