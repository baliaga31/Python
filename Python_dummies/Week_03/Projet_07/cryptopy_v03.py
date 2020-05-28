#!/usr/bin/env python

"""
    Cryptopy Version 2
    Crypte et decrypte un texte en chiffrement Cesar.
    Sait travailler avec le contenu d'un fichier texte.
"""

#### Imports
import string

#### Constantes
JEUCAR = string.printable[:-5]
CARSUBSTI = JEUCAR[-3:]+JEUCAR[:-3]
MSG_TEST = "J'adore les Monty Python. Trop cool."

# Generation du dictionnaire avec le jeu de caracteres
# (en clair)
DICO_ENCRYP = {}
for i,k in enumerate(JEUCAR):
    v = CARSUBSTI[i]
    DICO_ENCRYP[k] = v
# Les autres \t, \n etc. restent tels quels
for c in string.printable[-5:]:
    DICO_ENCRYP[c] = c

### Fonctions
def encrypter(texteclair, vardico_cryp):
    """
        Crypte le message texteclair avec le dictionnaire fourni et renvoie le 
        texte une fois rendu illisible.
    """
    textesecret = []
    for k in texteclair:
        v = vardico_cryp[k]
        textesecret.append(v)
    return ''.join(textesecret)

def decrypter(textesecret, vardico_decryp):
    """
        Decrypte le message avec le dictionnaire fourni et renvoie le 
        texte une fois rendu lisible.
    """
    texteclair = []
    for k in textesecret:
        v = vardico_decryp[k]
        texteclair.append(v)
    return ''.join(texteclair)

### Main Section
textesecret = encrypter(MSG_TEST, DICO_ENCRYP)
print(MSG_TEST)
print(textesecret)