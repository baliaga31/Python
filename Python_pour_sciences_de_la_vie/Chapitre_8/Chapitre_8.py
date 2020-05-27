#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import math
import random
import os
import time

# Exercice 8.1:

for number in range(10,21):
    racine = math.sqrt(number)
    print("{:d} {:.3f}".format(number, racine))

# Exercice 8.2:

print("\n Valeur de cos(pi/2)")
print(math.cos(math.pi/2))


# Exercice 8.3:

print(os.getcwd())
print(os.listdir())
print(len(os.listdir()))

# Exercice 8.4:

for number in range(0,11):
    print(number)
    time.sleep(1)

# Exercice 8.5:

