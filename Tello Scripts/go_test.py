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

    drone.takeoff()

    # forward
    drone.go(40, 0, 0, 20)
    time.sleep(2)
    # up
    drone.go(0, 0, 40, 20)
    time.sleep(2)
    # left
    drone.go(0, 40, 0, 20)
    time.sleep(2)
    # back to start
    drone.go(-40, -40, -40, 20)

    drone.land()

    return


if __name__ == '__main__':
    main()
