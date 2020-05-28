#!/usr/bin/env python

"""
    Cryptopy Version 1
    Crypte et decrypte un texte en chiffrement Cesar.
    Sait travailler avec le contenu d'un fichier texte.
"""

#### Imports
import string

#### Constantes
JEUCAR = string.printable[:-5]
CARSUBSTI = JEUCAR[-3:]+JEUCAR[:-3]
MSG_TEST = "J'adore les Monty Python. Trop cool."

#### Fonctions
def encrypter(texteclair):
    """
        Crypte le message clair avec un chiffrement Cesar (d-a) et renvoie le
        texte illisible.
    """

    return texteclair # Pas de traitement pour le moment

#### Main Section
textesecret = encrypter(MSG_TEST)
print(MSG_TEST)
print(textesecret)
