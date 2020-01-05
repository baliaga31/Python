#!/usr/bin/env python

"""
    Script Exercice 2 
"""

#import module
import math

print("Programme de conversion HT à TTC.")
#Declaration de la variable HT
HT = float(input("Prix HT: "))

while HT > 0:
    #Calcul HT -> TVA 20%
    TVA = (HT * 20) / 100
    #Prix final
    TTC = HT + TVA
    print("Le prix final avec les taxes est de :", TTC)
    HT = float(input("Prix HT: "))

print("Au revoir !") 