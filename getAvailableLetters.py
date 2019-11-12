# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:32:15 2019

@author: aleah cute
"""

import string

def getAvailableLetters(lettersGuessed) :
    alphabet = string.ascii_lowercase
    for char in lettersGuessed :
        if char in alphabet :
            alphabet = alphabet.translate({ord(char): None})
    return alphabet 
