import random
import sys

HANGMAN_PICS = [
    r"""
  +--+
  |  |
     |
     |
     |
     |
  =====""",
    r"""
  +--+
  |  |
  O  |
     |
     |
     |
  =====""",
    r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
  =====""",
    r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
  =====""",
    r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
    r"""
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
=====""",
    r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
====="""]

CATEGORY = 'Animals'
WORDS = """ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR
COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK
LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE  NEWT OTTER OWL PANDA PARROT
PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD 
TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA""".split()

# List of incorrect letter guesses.
missedLetters = []
# List of correct letter guesses.
correctLetters = []
# The word the player must guess.
secretWord = random.choice(WORDS)


def drawHangman(missedLetters, correctLetters, secretWord):
    """
    Draw the current state of the hangman, along with the missed and correctly-guessed
    letters of the secret word.
    """
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # Show the incorrectly guessed letters:
    print('Missed Letters: ', end="")
    for letter in missedLetters:
        print(letter, end='')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # Display the blanks for the secret word (one blank per letter):
    blanks = ['_'] * len(secretWord)

    # Replace blanks with correctly guessed letters:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Show the secret word with spaces in between each letter:
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """
    Returns the letter the player entered. This function makes sure the player 
    entered a single letter they haven't guessed before.
    """
    # Keep asking until the player enters a valid letter.
    while True:
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER')
        else:
            return guess


while True:
    drawHangman(missedLetters, correctLetters, secretWord)

    # Let the player enter their letter guess.
    guess = getPlayerGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters.append(guess)

        # Check if the player has won:
        foundAllLetters = True
        for secretWordLetter in secretWord:
            if secretWordLetter not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is: ', secretWord)
            print('You have won!')
            break
    else:
        # If the letter guessed is not contained in the secret word
        missedLetters.append(guess)

        # Check if player has guessed too many times and lost.
        # (The "-1" is because we don't count the empty gallows in # HANGMAN_PICS. )
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            drawHangman(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!')
            print('The word was "{}"'.format(secretWord))
            break
