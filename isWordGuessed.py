def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:
        if char in lettersGuessed:
            return True
        return False