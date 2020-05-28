#!/usr/bin/env python

""" 
    Projet 5 JeuDevin.py Version 1
"""
import random

nbr_secret = random.randint(1,100)
INVITE = 'propose un nombre:'

def jouer_tour():
    """ Choix d'un nombre, demande au joueur de le trouver et 
    reboucle tant qu'il ne l'a pas """
    while True:
        nbr_joueur = raw_input(INVITE)
        if nbr_secret == int(nbr_joueur):
            print('Correct!')
            break
        elif nbr_secret > int(nbr_joueur):
            print('Trop petit')
        else:
            print('Trop grand')

# Section MAIN

while True:
    jouer_tour()