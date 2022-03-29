import random
import pyperclip


def checkKey(key):
    """Returns True if the key is valid. Otherwise return False."""

    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    # Checks if there is a one to one match for every character in the lettersList
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False

    return True


def encryptMessage(message, key):
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        # Swap the key and LETTERS strings to decrypt
        charsA, charsB = charsB, charsA

    # Loop through each character in the message:
    for symbol in message:
        if symbol.upper() in charsA:
          # Find the index in one set of characters
            symIndex = charsA.find(symbol.upper())
            # We check the case to make sure that we preserve the case in the translated message as well
            if symbol.isupper():
               # Use the index to extract a symbol from the same position in another set of characters
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
          # The symbol is not in LETTERS, just add it unchanged.
          # This could account for non-alphabetical characters
            translated += symbol

    return translated


def generateRandomKey():
    """Genearte and return a random encryption key."""
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


# Letters in an Alphabet
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("""
A simple substitution cipher has a one-to-one translation for each symbol in the plaintext
and each symbol in the ciphertext.
""")

# Keep repeating the prompt to force the user to enter the correct option
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()

    if response.startswith('e'):
        myMode = 'encrypt'
        break
    elif response.startswith('d'):
        myMode = 'decrypt'
        break

    print('Print enter the letter e or d.')

# Keep repeating the prompt until the user enters a valid key
while True:
    print('Please specify the key to use.')
    if myMode == 'encrypt':
        print('or enter RANDOM to have one generated for you.')
    response = input('> ').upper()
    if response == 'RANDOM':
        myKey = generateRandomKey()
        print('The key is {}. KEEP THIS SECRET!'.format(myKey))
        break
    else:
        if checkKey(response):
            myKey = response
            break

# Let the user specify the message to encrypt / decrypt:
print('Enter the message to {}.'.format(myMode))
myMessage = input('> ')

# Perform the encryption/decryption:
if myMode == 'encrypt':
    translated = encryptMessage(myMessage, myKey)
elif myMode == 'decrypt':
    translated = decryptMessage(myMessage, myKey)

print('The %sed message is: ' % (myMode))
print(translated)
pyperclip.copy(translated)
print('Full %sed text copied to clipboard.' % (myMode))
