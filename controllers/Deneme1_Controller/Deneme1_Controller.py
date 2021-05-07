from controller import Robot
from controller import Keyboard
import pygame
CRUISING_SPEED = 10.0
TURN_SPEED = CRUISING_SPEED/2.0
TIME_STEP = 64

robot =Robot()

left_wheel = robot.getDevice('left wheel')
right_wheel = robot.getDevice('right wheel')

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
right_wheel.setVelocity(0.0)
left_wheel.setVelocity(0.0)


keyboard = Keyboard()
keyboard.enable(TIME_STEP)

motor_cmd = {
    ord('W'): (CRUISING_SPEED, CRUISING_SPEED),
    ord('S'): (-CRUISING_SPEED, -CRUISING_SPEED),
    ord('A'): (-TURN_SPEED, TURN_SPEED),
    ord('D'): (TURN_SPEED, -TURN_SPEED),
    ord('E'): (0.0, 0.0)
}

def command_Motors(cmd):
    left_wheel.setVelocity(cmd[0])
    right_wheel.setVelocity(cmd[1])
    
while robot.step(TIME_STEP) != -1:
    key = keyboard.getKey()
    if key in motor_cmd.keys():
        command_Motors(motor_cmd[key])