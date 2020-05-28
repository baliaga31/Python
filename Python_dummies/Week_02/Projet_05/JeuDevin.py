#!/usr/bin/env python

import random

nbr_secret = random.randint(1, 100)
invite = 'Propose un nombre :'

while True:
    nbr_joueur = raw_input(invite)
    if nbr_secret == int(nbr_joueur):
        print('Correct !')
        break
    elif nbr_secret > int(nbr_joueur):
        print('Trop petit')
    else:
        print('Trop grand')