import random
import time

# Character used for representing progress of task
BAR = chr(9608)

bytesDownloaded = 0
downloadSize = 4096

"""
# Explaining use of flush
# Since flush is not used Hello World plus Bye String will be printed after 5 seconds
print("Hello World!!!", end="")
time.sleep(5)
print("Bye!!!")


# Since flush is used, Hello World will print first then Bye string will be
# added to end of Hello World string after 5 seconds
print("Hello World!!!", end="", flush=True)
time.sleep(5)
print("Bye!!!")
"""


def getProgressBar(progress, total, barWidth=40):
    """
    Function returns a string which represents a progress bar that has bars 
    equal to barWidth and has progressed progress amount of a total amount.
    """

    progressBar = ''
    progressBar += '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Determine the number of bars to display
    # Multiplying it by barWidth to ensure that the length does not exceed barWidth
    numberOfBars = int((progress / total) * barWidth)

    # Determines the progress so far
    progressBar += BAR * numberOfBars
    # Determines the progress yet to be achieved
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'

    # Calculate the percentage completed:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'

    # Add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar


while bytesDownloaded < downloadSize:
    # Download a random amount of bytes
    bytesDownloaded += random.randint(0, 100)

    # Get the progress bar string for the corresponding fraction:
    barStr = getProgressBar(bytesDownloaded, downloadSize)

    # Don't print a newline at the end, and immediately flush the
    # printed string to the screen:
    print(barStr, end="", flush=True)
    time.sleep(0.2)

    # Print the backspaces to move the cursor to the line' start:
    print('\b' * len(barStr), end="", flush=True)
