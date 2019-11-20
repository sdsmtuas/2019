#Control Drone with keyboard keys
#Extra points if you write a teleop program a joystick


#!/usr/bin/python
import sys, termios, tty, os, time, rospy
from std_msgs.msg import Empty,UInt8,Bool
from geometry_msgs.msg import Twist
from random import *

msg = """
Program is used control a rover and a parrot drone using keyboard bindings.
---------------------------
           Rover
---------------------------
   i    ----> Forward
   k    ----> Backward
   j    ----> Pivot Left
   l    ----> Pivot Right
   u    ----> Slow Down
   o    ----> Speed Up
   ;    ----> Disable
   p    ----> Motors Re-enable
   [/]  ----> Control camera tilt angle
   c    ----> Start/Stop recording
---------------------------
       Parrot Drone
---------------------------
   w/s  ----> Pitch
   a/d  ----> Roll
   q/e  ----> Yaw
   </>  ----> Altitude
   [/]  ----> Control camera tilt angle
   c    ----> Start/Stop recording
   f    ----> (Make sure there are no immediate obstructions)
---------------------------
All other keys will reset everything to 0
Wait for the program to tell you to start sending commands
CTRL-C to quit
"""

#Get commands from Keyboard
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#Writes values in the form of Twist() message
def move(motion,x_vel,y_vel,z_vel,yaw):
    motion.linear.x = x_vel
    motion.linear.y = y_vel
    motion.linear.z = z_vel
    motion.angular.z = yaw
    return motion

#reset all velocities
def reset():
    lin_x = 0
    lin_y = 0
    lin_z = 0
    ang_z = 0
    return (lin_x,lin_y,lin_z,ang_z,ch)

#move camera up and down
def camera_control(ch,camera,virtual_camera):
    if ch == '[':
        camera.angular.y = camera.angular.y - 0.2
    elif ch == ']':
        camera.angular.y = camera.angular.y + 0.2
    virtual_camera.publish(camera)
    return camera

#map keys to different actions
def key_map(ch,lin_x,lin_y,lin_z,ang_z,camera,virtual_camera):
    w_pressed=0  #Keagan--This isnt used anywhere?
    a_pressed=0  #Keagan--This isnt used anywhere?
    print(ch)
    while ch:
        print ch
        #Pitch
        if ch ==  "w":
            if lin_x<0:
                lin_x = 0
            lin_x = lin_x + 0.2  #Keagan--should 0.2 be a 'constant' variable?
            lin_y,lin_z,ang_z = (0,0,0)  # yes I know there are no true constants in Python
        elif ch == 's':
            if lin_x > 0:
                lin_x = 0
            lin_x = lin_x - 0.2
            lin_y,lin_z,ang_z = (0,0,0)
        #Roll
        elif ch == "a":
            if lin_y<0:
                lin_y = 0
            lin_y = lin_y + 0.2
            lin_x,lin_z,ang_z = (0,0,0)
        elif ch == "d":
            if lin_y>0:
                lin_y = 0
            lin_y = lin_y - 0.2
            lin_x,lin_z,ang_z = (0,0,0)
        #yaw
        elif ch == "e":
            if ang_z < 0:
                ang_z = 0
            ang_z = ang_z + 0.2
            lin_y,lin_z,lin_x = (0,0,0)
        elif ch == "q":
            if ang_z>0:
                ang_z = 0
            ang_z = ang_z - 0.2
            lin_y,lin_z,lin_x = (0,0,0)
        #Altitude
        elif ch == ">":
            lin_z = 1
            lin_y,lin_x,ang_z = (0,0,0)
        elif ch =="<":
            lin_z = -1
            lin_y,lin_x,ang_z = (0,0,0)
        #Flip
        elif ch == 'f':
            flip = randint(0,3)
            rospy.loginfo('Flipping')
            flip_off.publish(flip)
            time.sleep(2)
        #Move camera
        elif (ch == '[' or ch == ']'):
            camera = camera_control(ch,camera,virtual_camera)
        #Reset drone's everything if anything else is pressed
        else:
            lin_x,lin_y,lin_z,ang_z,ch = reset()
        return (lin_x,lin_y,lin_z,ang_z,ch)

#Keagan -- Check if the key is being held
def key_held(ch,prev_ch):
    if ch == prev_ch:
        return True
    else:
        return False
   

##############################################################################
################ End of Definitions, beginning code execution ################
##############################################################################

#Keagan's hideous global variables
SPEED_INTERVAL = 5

first_execute = True
prev_ch = 'placeholder'
   
flag,ch= (0,0)
lin_x,lin_y,lin_z,ang_z,ch = reset()

print msg

#Set up messages and Publishers
motion = Twist()
camera = Twist()
take_off = rospy.Publisher('/ardrone/takeoff',Empty,queue_size=2)
land = rospy.Publisher('/ardrone/land',Empty,queue_size=2)
record = rospy.Publisher('/ardrone/record',Bool,queue_size=2)
motion_command = rospy.Publisher('/ardrone/cmd_vel',Twist,queue_size=1)
flip_off = rospy.Publisher('/ardrone/flip',UInt8,queue_size=1)
virtual_camera = rospy.Publisher('/ardrone/camera_control',Twist,queue_size=2)

#initialize ROS node
rospy.init_node('teleop_node',anonymous=True)
#Wait for initialization to finish
time.sleep(5)

#Keagan -- should you have a prompt here so that the drone doesn't
#          automatically take off?
rospy.loginfo('Taking off.....')
print("Taking off")
take_off.publish(Empty())
time.sleep(5)

#Tell user to start sending commands
rospy.loginfo('Send Commands now..')
while True:  
    ch = getch()               
    #Map pressed keys
    lin_x,lin_y,lin_z,ang_z,ch=key_map(ch,lin_x,lin_y,lin_z,ang_z,camera,virtual_camera)
    move(motion,lin_x,lin_y,lin_z,ang_z)
    motion_command.publish(motion)
    ##lin_x,lin_y,lin_z,ang_z,ch=reset()
    #Start/Stop recording
    if ch == "c":

        if flag == 0:
            rospy.loginfo('Turning on recording...')
            flag = 1
        elif flag == 1:
            rospy.loginfo('Turning off recording...')
            flag = 0
        record.publish(flag)

#land on exit
land.publish(Empty())
