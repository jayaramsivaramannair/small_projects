import time
import sys
import display


while True:
    # prints 60 new lines
    print('\n' * 25)

    # Get the curren time
    currentTime = time.localtime()

    # Format it so we a 12-hour clock and not a 24 hour one
    hours = str(currentTime.tm_hour % 12)
    if hours == '0':
        hours = '12'
    minutes = str(currentTime.tm_min)
    seconds = str(currentTime.tm_sec)

    # Get the digit strings (seven-segments) by using the function from display module
    hDigits = display.getSevSegStr(hours, 2)
    hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

    mDigits = display.getSevSegStr(minutes, 2)
    mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

    sDigits = display.getSevSegStr(seconds, 2)
    sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

    # Display the digits using seven segments
    print(hTopRow + '      ' + mTopRow + '      ' + sTopRow)
    print(hMiddleRow + '  *   ' + mMiddleRow + '  *   ' + sMiddleRow)
    print(hBottomRow + '  *   ' + mBottomRow + '  *   ' + sBottomRow)

    print()
    print('Press Ctrl + C to quit.')

    # Keep looping until the next second arrives
    while True:
        time.sleep(0.01)
        if time.localtime().tm_sec != currentTime.tm_sec:
            break
