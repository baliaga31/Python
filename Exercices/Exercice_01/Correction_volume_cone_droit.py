# coding=utf-8
#!usr/bin/env python

"""
    Correction volume cone droit
"""

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from math import pi

# Programme principal =========================================================
rayon = float(input("Rayon du cône (m) :"))
hauteur = float(input("Hauteur du cône (m) :"))

volume = (pi*rayon*rayon*hauteur)/3.0
print("Volume du cône =", volume, "m3")