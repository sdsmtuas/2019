"""
Author: Conrad Selig
Date: 11 / 12 / 2019
"""


def dd_get_height(drone):
    height = drone.get_height()
    return [height, "Current Drone Height: " + str(height)]


def dd_get_battery(drone):
    bat = drone.get_battery()
    return [bat, "Current Drone Battery: " + str(bat) + "%"]


def dd_get_speed(drone):
    speed = drone.get_speed()
    return [speed, "Current Drone Speed: " + str(speed)]
