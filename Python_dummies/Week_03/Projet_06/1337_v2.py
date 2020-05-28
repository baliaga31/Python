#!/usr/bin/env python

"""
    Codage d'un message en langue Leet Speak (1337 Sp34k)
    Version 2 (amorce de fonction)
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
txt_converti = coder_message(TEST_MESSAGE, TEST_SUBSTITUTIONS)
print(TEST_MESSAGE)
print(txt_converti)