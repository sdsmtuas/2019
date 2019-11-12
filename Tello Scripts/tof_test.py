"""
Author: Conrad Selig
Date: 11 / 12 / 2019
"""

from easytello import tello
from . import drone_diag


def main():
    drone = tello.Tello()
    print(drone_diag.dd_get_battery(drone)[1])

    drone.takeoff()

    while drone.get_tof() < 2000:
        drone.up(20)

    while drone.get_tof() > 500:
        drone.down(20)

    drone.land()

    return


if __name__ == '__main__':
    main()
