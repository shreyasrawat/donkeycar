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

while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left down")
                if event.key == pygame.K_RIGHT:
                    print("Right down")
                if event.key == pygame.K_UP:
                    print("Up down")
                if event.key == pygame.K_DOWN:
                    print("Down down")
            if event.type == pygame.QUIT:
                running = False
                print("Exiting")
                break
            if event.type == pygame.KEYUP:
                 print("nothing pressed")

    

pygame.display.quit()
pygame.quit()
sys.exit()