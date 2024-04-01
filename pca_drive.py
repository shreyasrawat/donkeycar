from donkeycar.parts.actuator import PCA9685
from time import sleep
import pygame
import sys
  
# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((300, 300)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Window') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
running = True




'''
    -
    -
    - 
'''
throttle = PCA9685(0, address=64, frequency=60)
steering = PCA9685(1, address=64, frequency=60)
speed = 400
angle_straight = 360
angle_left = 90
angle_right = 450

while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    steering.run(angle_left)
                if event.key == pygame.K_RIGHT:
                    steering.run(angle_right)
                if event.key == pygame.K_UP:
                    throttle.run(speed)
                if event.key == pygame.K_DOWN:
                    print("Down down")
            if event.type == pygame.QUIT:
                running = False
                print("Exiting")
                break
            if event.type == pygame.KEYUP:
                steering.run(angle_straight)

   