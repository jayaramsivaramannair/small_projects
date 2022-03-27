import random
import pyperclip


def makeSpongeCase(message):

    # Randomize the case to bring in some randomness
    useUpper = False
    newMessage = ''

    for character in message:
        if character.isalpha():

            # If the newMessage is empty or not
            # Start a newMessage with lowercase letter
            if not newMessage:
                newMessage += character.lower()
                continue
            # Check if the last character in newMessage is an upper case letter then make the succeeding lower case
            if newMessage[-1].isupper():
                newMessage += character.lower()
            else:
                if useUpper:
                    newMessage += character.upper()
                else:
                    newMessage += character.lower()
        else:
            newMessage += character

        # Selects a number between 1 and 100 both inclucded
        if random.randint(1, 100) <= 90:
            # Flips the case
            useUpper = not useUpper

    return newMessage


userMessage = ''
spongeText = ''

print('eNtEr YoUr MeSsAgE: ')
userMessage = input('> ')
spongeText = makeSpongeCase(userMessage)
print(spongeText)

try:
    pyperclip.copy(spongeText)
    print('cOpIed SpOnGeTexT to ClIpbOaRd.')
except:
    pass
