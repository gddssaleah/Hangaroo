# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:21:48 2019

@author: aleah cute
"""

def getGuessedWord(secretWord,lettersGuessed):
    letter = ' ' 
    for char in secretWord:
        if char in lettersGuessed:
            letter +=char
        else:
            letter += ('_')
    return letter