import sys
import time
import display


# Variable to take seconds left on the timer
secondsLeft = 120

while True:

    print('\n' * 60)

    # 3600 seconds is 1 hour
    hours = str(secondsLeft // 3600)

    minutes = str((secondsLeft % 3600) // 60)

    seconds = str(secondsLeft % 60)

    # Get the seven segment for hours, minutes and seconds
    hDigits = display.getSevSegStr(hours, 2)
    hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

    mDigits = display.getSevSegStr(minutes, 2)
    mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

    sDigits = display.getSevSegStr(seconds, 2)
    sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

    # Display the digits:
    print(hTopRow + '        ' + mTopRow + '        ' + sTopRow)
    print(hMiddleRow + '    *   ' + mMiddleRow + '    *   ' + sMiddleRow)
    print(hBottomRow + '    *   ' + mBottomRow + '    *   ' + sBottomRow)

    if secondsLeft == 0:
        print()
        print(' ****BOOM****')
        break

    print()
    time.sleep(1)
    secondsLeft -= 1
