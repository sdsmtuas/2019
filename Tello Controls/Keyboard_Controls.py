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
# Note to self: pull before you push you dumb dumb

drone = tello.Tello()

def main():
    while True:
        try:
            if keyboard.is_pressed('q'):
                print("quitting program")
                break

            if keyboard.is_pressed('\\'):
                drone.takeoff()

            if keyboard.is_pressed('/'):
                drone.land()

            if keyboard.is_pressed('i'):
                drone.forward()

            if keyboard.is_pressed('j'):
                print("\n\tgoing left")
                drone.left()

            if keyboard.is_pressed('k'):
                drone.back()

            if keyboard.is_pressed('l'):
                drone.right()


if __name__ == '__main__':
    main()