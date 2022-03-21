import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print('Enter the message to be reproduced using an image of world map')
message = input('> ')
if message == "":
    sys.exit()


# Loop over each line in the bitmap
for line in bitmap.splitlines():
    # Loop over each character in each line of the bitmap
    # enumerate() can be used to keep track of index and value at the same time
    for i, bit in enumerate(line):
        if bit == " ":
            # By default print message ends with a new line, end parameter helps us override the default and replace it with non-empty character
            print(" ", end="")
        else:
            print(message[i % len(message)], end="")
    # Print a new line after each line in the pattern
    print()
