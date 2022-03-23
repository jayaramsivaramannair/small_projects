"""
This program hacks messages encrypted with the Caesar Cipher by doing a brute force attack against every possible key

"""

# Let the user specify the message to hack:
print("Enter the encrypted Caesar Cipher message to hack.")
message = input('> ')


# Every possible symbol that can be encrypted / decrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            # Returns index of each character in 'SYMBOLS' string
            num = SYMBOLS.find(symbol)
            # Decrypt the number.
            num = num - key

            # Wrap-around if the num is less than 0
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # If the character is not present in 'SYMBOLS' string then simply add it
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print('Key #{}:{}'.format(key, translated))
