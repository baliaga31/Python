#import random module

import random

# Make sure that the_flying_circus() returns True
def the_flying_circus():
    i = random.randint(5,100)
    print i
    if 5 > i:    # Start coding here!
        return i
    elif i == 4 and i > 5:
        return i
    else:
        return True
