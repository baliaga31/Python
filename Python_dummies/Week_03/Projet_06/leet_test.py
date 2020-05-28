#!/usr/bin/python3

"""
   Leet Speak script
   Author: Benoit Aliaga
   Version 01
"""

# Variables

Sub = [['a','4'], ['e','3'], ['l','1'], ['o','0'], ['t','7']]

# Fonction Leet converter

def leet_converter(message, Sub):
    """
       Write a message and translate it in leet speak.
    """

    for s in Sub:
        vcar = s[0]
        ncar = s[1]
        message = message.replace(vcar,ncar)
        
    message_crypt = message
    print("I leave the leet_converter function.")
    return(message_crypt)

# Fonction Leet debugger

def leet_debugger(message_crypt, Sub):
    """
       Break the leet message.
    """

    print("I will start the leet_debugger function.")
    print("Leet message:", message_crypt)
    
    for s in Sub:
        carv = s[1]
        carn = s[0]
        message_crypt = message_crypt.replace(carv, carn)

    break_message = message_crypt
    return(break_message)

# Main programm

message = input('Propose un message a crypter \n')
X = leet_converter(message, Sub)

leet_debugger(X, Sub)
