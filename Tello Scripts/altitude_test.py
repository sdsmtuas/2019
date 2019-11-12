"""
Author: Conrad Selig
Date: 11 / 12 / 2019
"""

from easytello import tello
from . import drone_diag


def main():
    drone = tello.Tello()
    drone.set_speed(100)
    print(drone_diag.dd_get_battery(drone)[1])
    # drone.streamon()
    drone.takeoff()

    height = drone.get_height()

    while height < 18:
        d_height = drone_diag.dd_get_height(drone)
        height = d_height[0]
        print(d_height[1])
        drone.up(20)

    while height > 3:

        d_height = drone_diag.dd_get_height(drone)
        height = d_height[0]
        print(d_height[1])
        drone.down(20)

    drone.land()
    # drone.streamoff()
    return


if __name__ == '__main__':
    main()
