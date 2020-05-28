#!/usr/bin/python

def anti_vowel(text):
    vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
    for n in text:
        for n in vowel_list:
            text = text.replace(n,"")
    return text

print anti_vowel("Hey you")
