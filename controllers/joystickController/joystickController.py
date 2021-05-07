import pygame
import math
from controller import Robot
from controller import Keyboard


robot =Robot()
pygame.init()

joysticks =[]
Joys=[0,0,0,0]

CRUISING_SPEED = 10.0
TURN_SPEED = CRUISING_SPEED/2.0
TIME_STEP = 64

left_wheel = robot.getDevice('left wheel')
right_wheel = robot.getDevice('right wheel')

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
right_wheel.setVelocity(0.0)
left_wheel.setVelocity(0.0)

def command_Motors(cmd):
    left_wheel.setVelocity(cmd[1])
    right_wheel.setVelocity(cmd[3])

k=0

for i in range(0,pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Bulunan jotstick '",joysticks[-1].get_name(),"'")

while robot.step(TIME_STEP) != -1 and k<1:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gameExit=True
        if event.type == pygame.JOYBUTTONDOWN:
            if(event.button==0):
                k=1

        axes = joysticks[-1].get_numaxes()
        for i in range(axes):
            if joysticks[-1].get_axis(i)<0.02 and joysticks[-1].get_axis(i)>-0.02:
                Joys[i]=0
            else:
                if (i==1):
                    Joys[i]=round(joysticks[-1].get_axis(i),3)*(-10)
                     
                elif(i==3):
                    Joys[i]=round(joysticks[-1].get_axis(i),3)*(-10)                  
                                       

                else:
                    Joys[i]= round(joysticks[-1].get_axis(i),3)                 

                
            
        print(Joys)
        command_Motors(Joys)





            
          

        
            
            
                
                

        
