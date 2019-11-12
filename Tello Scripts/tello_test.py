"""
Author: Conrad Selig
Date: 11 / 12 / 2019
"""

from easytello import tello
from . import drone_diag
import time


def main():

    drone = tello.Tello()
    print(drone_diag.dd_get_battery(drone)[1])

    drone.streamon()
    drone.takeoff()
    time.sleep(5)


    '''
    user_i = input("Check Altitude: ")
    while user_i != "exit":
        print(drone.get_attitude())
        user_i = input("Check Altitude: ")
    '''

    for i in range(4):
        drone.forward(100)
        drone.cw(92)

    drone.land()
    drone.streamoff()
    return


if __name__ == '__main__':
    main()
