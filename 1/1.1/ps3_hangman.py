# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for ch in secretWord:
        if not ch in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for ch in secretWord:
        if ch not in lettersGuessed:
            ch = '_ '
        result += ch
    return result
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ''
    from string import ascii_lowercase
    for ch in ascii_lowercase:
        if ch not in lettersGuessed:
            available += ch
    return available



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def line():
        print ("-------------")
          
    def play():
        '''
        A simple helper function that plays the game. It asks for interation and maintains the current state.
        
        Returns
        -------
        bool
            True if game the player either guesses a word already in list or if they guess a word successfully, False otherwise
        '''
        print ("Available Letters:",getAvailableLetters(lettersGuessed))
        
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        guess = input("Please guess a letter: ").lower()
        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " 
                   + guessedWord)
            return True
        lettersGuessed.append(guess)
        
        
        if guess in secretWord:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print ("Good guess: " 
                   + guessedWord)
            return True
        else:
            print ("Oops! That letter is not in my word: " 
                   + guessedWord)
            return False
        
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is", len(secretWord), 
           "letters long.")
    line ()
    
    guessLeft = 8
    lettersGuessed = []
    
    while guessLeft:
        
        print ("You have", guessLeft, "guesses left.")
        if not play():
            guessLeft -= 1
        line()
        
        if isWordGuessed(secretWord, lettersGuessed):
            break
        
    if isWordGuessed(secretWord, lettersGuessed):
        print ("Congratulations, you won!")
    else:
        print ("Sorry, you ran out of guesses. The word was "
               + secretWord)
        
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# secretWord = "hello"
hangman("c")
