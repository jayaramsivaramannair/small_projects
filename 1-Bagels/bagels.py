import random


print("Bagels, a deductive logic game.")
print("\n")
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say:        That means:")
print(" Pico              One digit is correct but in the wrong position.")
print(" Fermi             One digit is correct and in the right position.")
print(" Bagels            No digit is correct.")
print("I have thought up a number.")
print(" You have 10 guesses to get it.")
print("\n")

# Variable to stop the game if the game is correct
correct_guess = False

# Variable to track the number of guesses as the number of guesses cannot exceed 10
guesses = 1
computer_number = str(random.randint(100, 999))
user_number = ""
result = ""

# Dictionary to track the number guessed by the computer
computer_dict = {}

# Ask the user if he / she wants to continue or not
play_again = True
response = ""

# Dictionary to track the number input by the user
user_dict = {}

# Iterate over each character in the string representing computer's name
for element in range(0, len(computer_number)):
    computer_dict[element] = computer_number[element]

while play_again:
    while not correct_guess:
        if (guesses > 10):
            print("You ran out of guesses. Better luck next time!")
            break

        print("Guess #" + str(guesses) + ":")
        user_number = input("")

        # make a dictionary of the number entered by the user
        for element in range(0, len(user_number)):
            user_dict[element] = user_number[element]

        # Check if each digit is correct and in the correct position
        if user_dict[0] == computer_dict[0] and user_dict[1] == computer_dict[1] and user_dict[2] == computer_dict[2]:
            correct_guess = True

        if(correct_guess):
            print("You got it!")
            # if the number if guessed right then break out of the loop
            break

        # Check if each digit is present in the computer's number and if it is in the correct position or not
        for element in range(0, len(user_number)):
            if user_dict[element] in computer_dict.values():
                if user_dict[element] == computer_dict[element]:
                    if result == "":
                        result += "Fermi"
                    else:
                        result += " Fermi"
                else:
                    if result == "":
                        result += "Pico"
                    else:
                        result += " Pico"
            else:
                continue

        if(result == ""):
            print("Bagels")
        else:
            print(result)
            result = ""

        guesses += 1

    # Ask the user if he/she wants to play another round of the guessing game or not
    response = input("Do you want to play again? (yes or no)")
    if(response == "no"):
        print("Thanks for playing!")
        play_again = False
    elif(response == "yes"):
        result = ""
        guesses = 1
        correct_guess = False
