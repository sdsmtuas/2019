"""
Authors: Romain Caille
         Justin Lewis
Date: 11 / 19 / 2020
"""
# Control drone with keyboard commands
# Possibly implement joystick commands
from easytello import tello
import keyboard

msg = """
Program used to control Tello drone using keyboard bindings.
---------------------------------------
|            Tello Drone              |
---------------------------------------
    i   ----> pitchForward
    k   ----> pitchBack
    j   ----> rollLeft
    l   ----> rollRight
    ----------------------
    w   ----> goUp
    s   ----> goDown
    d   ----> yawCW
    a   ----> yawCCW
---------------------------------------
Press Escape to quit.

"""

def main():
    while True:
        try:
            if keyboard.is_pressed('q'):
                print("quitting program")
                break
        except (BaseException, Exception):
            break


if __name__ == '__main__':
    main()