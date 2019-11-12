# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:51:38 2019

@author: aleah cute
"""

def Hangaroo (secretWord):
    print("Welcome to Hangaroo") 
    letters = input("Enter guessed letter: ")
    lives = 5
    while lives > 0:
        failed = 0
        for char in secretWord:
            if char in letters:
                print (char)
            else: 
                print (" _ ")
                failed +=1            
        if failed == 0:
                print ("Congratulations! You saved Hangaroo.")
                break
        print
        letter = input("Enter guessed letter: ")
        letters += letter
        if letter not in secretWord:
            lives -=1
            print ("Incorrect")
            print ("You have", +lives, "lives left")
        if lives == 0:
            print ("You killed Hangaroo.")
            print ("The word is", secretWord)
        
                