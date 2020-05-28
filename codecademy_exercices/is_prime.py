#!/usr/bin/python

def is_prime(x):
	if x < 2:
		return false
	else:
		for n in range(2, x - 1):
			if x % n == 0:
       				return False
		return True
    
x = raw_input()
print x
print is_prime(x)