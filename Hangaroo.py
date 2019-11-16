# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:57:26 2019

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

def getGuessedWord(secretWord, lettersGuessed):
    
    guessedWord = ""
        
    for letter in secretWord:
        
        if letter in lettersGuessed:
            guessedWord = guessedWord + letter
        else:
            guessedWord = guessedWord + "_ "

    return guessedWord
    
def getAvailableLetters(lettersGuessed):
    
    import string
    alpha = string.ascii_lowercase
    availableLetters = ""
       
    for letter in alpha:
        if letter not in lettersGuessed:
            availableLetters = availableLetters + letter
    
    return availableLetters

def Hangaroo(secretWord):
    
    print("Welcome to Hangaroo!")
    print("The word is " +  str(len(secretWord))  + " letters long.")
    lettersGuessed = []
    mistakesMade = 0
    guessesLeft = 3
    
    while mistakesMade < 3:
        if isWordGuessed(secretWord, lettersGuessed):
            return print("You've guessed the word!")
        
        print("You have " +  str( guessesLeft )  + " guesses left!")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
            
        guess = input("Type a letter to guess the word: ")
        guess = str(guess)
        guess = guess.lower()
        
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            
            if guess in secretWord:
                print("Nice guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Bad guess: " + getGuessedWord(secretWord, lettersGuessed))
                mistakesMade += 1
                guessesLeft -= 1
        else:
            print("You already guessed that letter!" + getGuessedWord(secretWord, lettersGuessed))
            
    return print("You ran out of guesses. The word was " + str(secretWord))
