"""
Author: Conrad Selig
Date: 11 / 12 / 2019
"""

from easytello import tello
from . import drone_diag


def main():
    drone = tello.Tello()
    print(drone_diag.dd_get_battery(drone)[1])

    drone.streamon()

    drone.takeoff()

    drone.curve(75, -75, 0, 0, -150, 100, 60)
    drone.curve(-75, 75, 0, 0, 150, -100, 60)

    drone.land()

    drone.streamoff()

    return


if __name__ == '__main__':
    main()
