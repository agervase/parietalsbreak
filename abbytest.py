#!/usr/bin/env python

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import time
 
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

image = pygame.image.load("parietals.png")
image = pygame.transform.scale(image, (700, 500))
def img(x,y):
	screen.blit(image, (x,y))

x = 0
y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    #MENU
    homescreen = True
    while homescreen:
        for event in pygame.event.get():
        #print type(event)
            if event.type == pygame.QUIT:
                done = True
                homescreen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                if m > 335 and m < 390 and n > 155 and n < 185:
                   screen.fill(WHITE)
                   homescreen = False
            else:
                screen.fill(WHITE)
                img(x,y)
                pygame.display.update()
                pygame.display.flip()
 
    # --- Game logic should go here
    scene1 = True
    while scene1 and not done:
        for event in pygame.event.get():
        #print type(event)
            if event.type == pygame.QUIT:
                done = True
                scene1 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene1 = False
            else:
                screen.fill(BLACK)
                screen.blit(pygame.font.SysFont('Arial',25).render('Scene 1',True,(255,0,0)),(200,100))
                pygame.display.update()
                pygame.display.flip()
        
    scene2 = True
    while scene2 and not done:
        for event in pygame.event.get():
        #print type(event)
            if event.type == pygame.QUIT:
                done = True
                scene2 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene2 = False
            else:
                screen.fill(BLACK)
                screen.blit(pygame.font.SysFont('Arial',25).render('Scene 2',True,(255,0,0)),(200,100))
                pygame.display.update()
                pygame.display.flip()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
    # --- Go ahead and update the screen with what we've drawn.
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
