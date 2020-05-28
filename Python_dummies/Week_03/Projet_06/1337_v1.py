#!/usr/bin/env python

"""
    Codage d'un message en langue Leet Speak (1337 Sp34k)
    Version 1 (amorce de fonction)
"""

### Section des fonctions
def coder_message(message, substitutions):
    """
        Traite d'une chaine transmise et applique des substitutions de lettres
        d'apres une liste d'elements. Chaque element est une liste de longueur 2 (ancien, nouveau)
    """

### Section de test dans main
txt_converti = coder_message(TEST_MESSAGE, TEST_SUBSTITUTIONS)
print(txt_converti)