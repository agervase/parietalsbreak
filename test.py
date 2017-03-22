import pygame, sys 
import time
from pygame.locals import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.mixer.init(44100, -16,2,2048)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Background Music

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background = pygame.image.load("parietals.png")
background = pygame.transform.scale(background, (700, 500))

play = pygame.image.load("play.png")

clouds = pygame.image.load("clouds.png")

def backgroundimg(x,y):
	screen.blit(background, (x,y))

def playimg(x,y):
	screen.blit(play, (x,y))

def cloudsimg(x,y):
	screen.blit(clouds, (x,y))

x = 0
y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Gets mouse position
    mouse = pygame.mouse.get_pos() 
	
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    backgroundimg(x,y)
    playimg(x,y)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
