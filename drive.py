from donkeycar.parts.actuator import PulseController
from donkeycar.parts import pins
import time
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
time.sleep(1)
while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pwm_steer.run(angle_left)
                if event.key == pygame.K_RIGHT:
                    pwm_steer.run(angle_right)
                if event.key == pygame.K_UP:
                    pwm_pin.run(speed)
                if event.key == pygame.K_DOWN:
                    print("Down down")
            if event.type == pygame.QUIT:
                running = False
                print("Exiting")
                break
            if event.type == pygame.KEYUP:
                pwm_steer.run(angle_straight)
car.run(0)
steer.run(360)

pygame.display.quit()
pygame.quit()
sys.exit()
