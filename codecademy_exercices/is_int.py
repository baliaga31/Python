#!/usr/bin/python

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(7.0)
print is_int(7.5)