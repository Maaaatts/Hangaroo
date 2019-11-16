# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:45:58 2019

@author: Matthew Rabanes
"""

def getAvailableLetters(lettersGuessed):
    
    import string
    alpha = string.ascii_lowercase
    availableLetters = ""
       
    for letter in alpha:
        if letter not in lettersGuessed:
            availableLetters = availableLetters + letter
    
    return availableLetters