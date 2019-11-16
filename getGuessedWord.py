# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:05:39 2019

@author: Matthew Rabanes
"""

def getGuessedWord(secretWord, lettersGuessed):
    
    guessedWord = ""
        
    for letter in secretWord:
        
        if letter in lettersGuessed:
            guessedWord = guessedWord + letter
        else:
            guessedWord = guessedWord + "_ "

    return guessedWord