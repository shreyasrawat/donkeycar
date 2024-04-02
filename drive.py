from donkeycar.parts.actuator import PulseController
from donkeycar.parts import pins
import time
from time import sleep
import pygame
import sys
import cv2
  
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

pwm_pin = 'PCA9685.1:40.0'
pwm_steer = 'PCA9685.1:40.1'
pwmFreq = 60

try:
    pwm_pin = pins.pwm_pin_by_id(pwm_pin)
    pwm_steer = pins.pwm_pin_by_id(pwm_steer)
except ValueError as e:
    print(e)
    print("See pins.py for a description of pin specification strings.")
    exit(-1)
print(f'init pin {pwm_pin}')
freq = int(pwmFreq)
print(f"Using PWM freq: {freq}")
car = PulseController(pwm_pin)
steer = PulseController(pwm_steer)

speed = 400
angle_straight = 360
angle_left = 90
angle_right = 450

car.run(10)
angle = 360
time.sleep(1)
while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle -= 10
                    if angle < 290:
                        angle = 290
                    steer.run(angle)
                    print(angle)
                if event.key == pygame.K_RIGHT:
                    angle += 10
                    if angle > 450:
                        angle = 450
                    steer.run(angle)
                    print(angle)
                if event.key == pygame.K_UP:
                    car.run(speed)
                if event.key == pygame.K_DOWN:
                    car.run(0)
                    car.run(10)
                   
            if event.type == pygame.QUIT:
                running = False
                print("Exiting")
                break
car.run(0)


pygame.display.quit()
pygame.quit()
sys.exit()
