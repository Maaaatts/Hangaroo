# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:37:04 2019

@author: Matthew Rabanes
"""

def isWordGuessed(secretWord, lettersGuessed):
    
    wordGuess = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuess += 1
        else:
            return False
    return True
