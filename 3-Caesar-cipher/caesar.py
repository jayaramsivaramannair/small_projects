import pyperclip as pc

print('Welcome to Caesar Cipher Script - I will encrypt your messages so that they can be delivered without intrusion')
print('Do you want to (e)ncrypt or (d)ecrypt?')

# Variable to keep track of whether the message is being encrypted or decrypted
mode = ""
key = ""
message = ""
result = ""

while mode != "e" or mode != "d":
    mode = input("> ")
    if mode == 'e' or mode == 'd':
        break
    print("Failed to understand your request:")
    print("Please enter (e) if you want the message to be encrypted")
    print("Please enter (d) if you want the message to be decrypted")

print('Please enter the key (0 to 25) to use.')
key = input("> ")

if mode == 'e':
    print('Enter the message to encrypt.')
elif mode == 'd':
    print('Enter the message to decrypt.')

message = input("> ")

for element in message:
    # if the character is a punctuation mark and thus not aphabetic, it must be used be used directly in the result
    if(element.isalpha()):
        # Get the ASCII value for the character's upper value
        keyValue = ord(element.upper())
        if (mode == 'e'):
            # Iterate from 1 to key entered by the user for each character to translate it
            for i in range(1, int(key) + 1):
                keyValue = keyValue + 1
                # This is included to make sure that the keyValue still represents a letter from the alphabet
                if keyValue > 90:
                    keyValue = 65
            result += chr(keyValue)
        elif (mode == 'd'):
            for i in range(1, int(key) + 1):
                keyValue = keyValue - 1
                if keyValue < 65:
                    keyValue = 90
            result += chr(keyValue)
    else:
        result += element

print(result)
pc.copy(result)
if (mode == 'e'):
    print('Full encrypted text copied to clipboard.')
elif(mode == 'd'):
    print('Full decrypted text copied to clipboard.')
