#!/usr/bin/env python

# -*- coding : utf8 -*-

"""
    Script calcul volume cone droit
"""
from math import pi

print("Propose un nombre")

def volume_cone_droit():

    R = float(input("Rayon du cône (m) :"))
    h = float(input("Hauteur du cone (m)"))
    volume = (pi * R**2 * h) / 3
    return volume

# MAIN SECTION
final = volume_cone_droit()
print(final)