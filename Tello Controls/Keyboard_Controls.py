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
    print(drone.get_battery())
    while True:
        try:
            if keyboard.is_pressed('q'):
                print("quitting program")
                break

            if keyboard.is_pressed('\\'):
                drone.takeoff()

            if keyboard.is_pressed('w'):
                drone.up(20)

            if keyboard.is_pressed('s'):
                drone.down(20)

            if keyboard.is_pressed('a'):
                drone.ccw(5)

            if keyboard.is_pressed('d'):
                drone.cw(5)

            if keyboard.is_pressed('/'):
                drone.land()

            if keyboard.is_pressed('i'):
                drone.forward(20)

            if keyboard.is_pressed('j'):
                print("\n\tgoing left")
                drone.left(20)

            if keyboard.is_pressed('k'):
                drone.back(20)

            if keyboard.is_pressed('l'):
                drone.right(20)

        except:
            break

if __name__ == '__main__':
    main()

