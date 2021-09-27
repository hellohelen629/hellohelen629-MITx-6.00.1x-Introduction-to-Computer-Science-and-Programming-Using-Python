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
    # FILL IN YOUR CODE HERE...
    boo = []
    for i in secretWord:
        if i in lettersGuessed:
            boo.append(True)
        else:
            boo.append(False)
    
    if False in boo:
        return False
    else:
        return True
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    l = []
    for i in secretWord:
        if i in lettersGuessed:
            l.append(i)
        else:
            l.append('_')
    
    str = ' '.join(l)
    return str



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    l = []
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            l.append(i)
    str = ''.join(l)    
    return str
               

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
    # FILL IN YOUR CODE HERE...
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord) ,'letters long')
    print('-----------')
    mistakesMade = 0
    guessDict = {}
    import string
    availableLetters = string.ascii_lowercase
    wrongL = []
    while mistakesMade <= 8:
      if mistakesMade == 8:
          print('Sorry, you ran out of guesses. The word was'+ ' '+ secretWord +'.')
          break
      elif isWordGuessed(secretWord, list(guessDict.values())):
          print('Congratulations, you won!')
          break      
      else:
          print('You have', 8 - mistakesMade, 'guesses left')
          
          availableLetters = getAvailableLetters(list(guessDict.values())+wrongL)
          print('Available Letters:', availableLetters)    
          
          guess = input('Please guess a letter: ')         
             
          
          if guess in secretWord and guess not in guessDict: #right guess
             
             guessDict[guess] = guess
             guess_ = getGuessedWord(secretWord, list(guessDict.values()))  
             print('Good guess:', guess_)
             print('-----------')
          elif guess in secretWord and guess in guessDict: #repeat right 
             guess_ = getGuessedWord(secretWord, list(guessDict.values()))
             print("Oops! You've already guessed that letter:", guess_)
             print('-----------')
          elif guess not in secretWord and guess in wrongL: #repeat right 
             guess_ = getGuessedWord(secretWord, list(guessDict.values()))
             print("Oops! You've already guessed that letter:", guess_)
             print('-----------')
          elif guess not in secretWord and guess not in guessDict: # wrong guess
              guess_ = getGuessedWord(secretWord, list(guessDict.values()))
              
              wrongL.append(guess)
              print('Oops! That letter is not in my word:', guess_)
              print('-----------')
              mistakesMade += 1
              
              
          
          
 


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
