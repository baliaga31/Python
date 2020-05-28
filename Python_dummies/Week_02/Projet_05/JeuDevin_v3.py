#!/usr/bin/env python

""" 
    Projet 5 JeuDevin.py Version 3
"""
import random

INVITE = 'propose un nombre:'

def jouer_tour():
    """ Choisir un nombre, demander au joueur de le trouver et 
    reboucler tant qu'il ne l'a pas """
    nbr_secret = random.randint(1,100)
    nbr_saisies = 0
    while True:
        nbr_joueur = raw_input(INVITE)
        nbr_saisies = nbr_saisies + 1
        if nbr_secret == int(nbr_joueur):
            print('Correct!')
            return nbr_saisies
        elif nbr_secret > int(nbr_joueur):
            print('Trop petit')
        else:
            print('Trop grand')

# SECTION PRINCIPALE MAIN

total_tours = 0
total_saisies = 0

while True:
    total_tours = total_tours + 1
    print("On passe au tour" + str(total_tours))
    print("En avant pour les devinettes !")

    ce_tour = jouer_tour()
    
    total_saisies = total_saisies + ce_tour
    print("Tu as fait " + str(ce_tour) + " saisies.")
    moy = str(total_saisies / float(total_tours))
    print("Ta moyenne de saisies/tour = " + moy)
    print("")