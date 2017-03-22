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

## a simple class that uses the generator
# and can tell if it is done
pygame.mixer.init(44100, -16,2,2048)
pygame.init()
 
font = pygame.font.Font(None, 25)
# raise the USEREVENT every 1000ms
pygame.time.set_timer(pygame.USEREVENT, 200)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Parietals Break")

# Background Music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Scrolling text functions 
def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        # don't pause for spaces
        if letter != ' ':
            yield tmp

class DynamicText(object):
    def __init__(self, font, text, pos, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.pos = pos
        self.autoreset = autoreset
        self.update()

    # Reset text to loop
    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, (0, 128, 0))
            except StopIteration:
                self.done = True
                if self.autoreset: self.reset()

    # Displays text 
    def draw(self, screen):
        screen.blit(self.rendered, self.pos)

# Actual function that does the actual thing
def textBox(text):
        message = DynamicText(font, text, (200, 200), autoreset=False)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: break
                        if event.type == pygame.USEREVENT: message.update()
                else:
                        #screen.fill(pygame.color.Color('black'))
                        message.draw(screen)
                        pygame.display.flip()
                        clock.tick(3)
                        continue
                break

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background = pygame.image.load("front_layer_title.png")
background = pygame.transform.scale(background, (700, 500))

clouds = pygame.image.load("clouds.png")

title = pygame.image.load("title_text.png")

play = pygame.image.load("play.png")

def backgroundimg(x,y):
	screen.blit(background, (x,y))

def cloudsimg(x,y):
	screen.blit(clouds, (x,y))

def titleimg(x,y):
	screen.blit(title, (x,y))

def playimg(x,y):
	screen.blit(play, (x,y))
x = 0
y = 0

cx = -100
cy = 0

cx2 = -800
cy2 = 0

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
                screen.fill((252, 220, 197))
		cx = cx + 10
		cx2 = cx2 + 10
		if cx > 700:
		    cx = -700
		    print cx
		if cx2 > 700:
                    cx2 = -700
                    #print cx2
		cloudsimg(cx,cy)
		cloudsimg(cx2,cy2)
                backgroundimg(x,y)
		titleimg(x,y)
		playimg(x,y)
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
                #screen.blit(pygame.font.SysFont('Arial',25).render('Scene 1',True,(255,0,0)),(200,100)
                textBox('Scene 1')
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
                #screen.blit(pygame.font.SysFont('Arial',25).render('Scene 2',True,(255,0,0)),(200,100))
                screen.blit.render.textBox("Scene 1")
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
