# function which takes a number and the number of digits required in the displayed string
def getSevSegStr(number, minWidth=0):
    # zFill is used to pre-fill a string with zeros until it is of the desired length
    number = str(number).zfill(minWidth)

    # Rows keeps tracks of each distinct component of a number represented using seven-segments
    rows = ['', '', '']
    for i in range(len(number)):
        if number[i] == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
        elif number[i] == '-':
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif number[i] == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif number[i] == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif number[i] == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif number[i] == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif number[i] == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif number[i] == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif number[i] == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif number[i] == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif number[i] == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif number[i] == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add a space between numbers if it is not the last digit
        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)


choice = ''
print('Enter a Number to display using seven segments: ')
choice = input('> ')
choice = int(choice)
print()
print(getSevSegStr(choice, 2))
