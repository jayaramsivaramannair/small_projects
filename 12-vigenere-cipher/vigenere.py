import pyperclip


# Declaration of a constant to hold all possible letters in an alphabet
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
myMode = ''


def encryptMessage(message, key):
    """Encrypt the message using the key"""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):

    translated = []

    keyIndex = 0
    key = key.upper()

    # Loop through each character in the message.
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            # Add the encrypted / decrypted symbol to translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)

    # Let the user specify it they are encrypting or decrypting:
    # Repeat the prompt until the user enters the expected input
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        myMode = 'encrypt'
        break
    elif response.startswith('d'):
        myMode = 'decrypt'
        break
    print('Please enter the letter e or d.')

    # Let the user specify the key to use:
    # Keep asking until the user enters a valid key.
while True:
    print('Please specify the key to use.')
    print('It can be a word or any combination of letters: ')
    response = input('> ').upper()
    if response.isalpha():
        myKey = response
        break

# Allow the user to enter the message for encryption / decryption:
print('Enter the message to {}.'.format(myMode))
myMessage = input('> ')

# Perform the encryption / descryption:
if myMode == 'encrypt':
    translated = encryptMessage(myMessage, myKey)
elif myMode == 'decrypt':
    translated = decryptMessage(myMessage, myKey)

print("%sed message: " % (myMode.title()))
print(translated)
pyperclip.copy(translated)
print('Full %sed text copied to clipboard.' % (myMode))
