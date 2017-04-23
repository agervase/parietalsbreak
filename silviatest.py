#!/usr/bin/env python

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import os, sys
import pygame
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (206, 206, 206)
RED = (255, 0, 0)
scene1 = False
scene2 = False
scene3 = False
scene4 = False
scene5 = False
scene6 = False

## a simple class that uses the generator
# and can tell if it is done
pygame.mixer.init(44100, -16,2,2048)
pygame.init()
 
font = pygame.font.Font("Aaargh.ttf", 15)

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

background = pygame.image.load("pictures/front_layer_title.png")
background = pygame.transform.scale(background, (700, 500))

clouds = pygame.image.load("pictures/clouds.png")

title = pygame.image.load("pictures/title_text.png")

play = pygame.image.load("pictures/play.png")

def backgroundimg(bg, x,y):
	screen.blit(bg, (x,y))

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

def drawPrompt(prompt):
	numchars = len(prompt)
	counter = 0 	
	ycoord = 330
	lineLength = 70
	while counter < numchars-lineLength:
		linechars = 0
		for word in prompt[counter:numchars].split():
			linechars = linechars+len(word)+1
			if linechars > lineLength:
				break
		if counter < numchars:
			line = prompt[counter:counter+linechars].strip()
			one = font.render(line, False, (0, 0, 0))
			screen.blit(one, (50, ycoord))
			ycoord = ycoord + 25
		counter = counter + linechars
	line = prompt[counter:numchars].strip()
	one = font.render(line, False, (0, 0, 0))
	screen.blit(one, (50, ycoord))
	

# If only one person, type 'none.png' into person2.
def drawScene(person1, person2, background):
	backgroundimg(pygame.image.load(background), x, y);	
	backgroundimg(pygame.image.load(person1), x, y);
	backgroundimg(pygame.image.load(person2), x+400, y);
	backgroundimg(pygame.image.load("pictures/textBox.png"), x, y);	

# If there are less than 4 choices type " ".
def drawChoices(numchoices, name, choice1, choice2, choice3, choice4):
	#numchoices = 4
	choiceFont = pygame.font.Font(None, 30)
	name = font.render(name, False, (255, 255, 255))
	one = choiceFont.render(choice1, False, (0, 0, 0))
	two = choiceFont.render(choice2, False, (0, 0, 0))
	three = choiceFont.render(choice3, False, (0, 0, 0))
	four = choiceFont.render(choice4, False, (0, 0, 0))
	screen.blit(name, (50, 300))
	if numchoices == 1:
		pygame.draw.rect(screen,(GRAY), pygame.Rect((95, 437), (500, 25)))
		screen.blit(three, (100, 440))
	elif numchoices == 2:
		pygame.draw.rect(screen,(GRAY), pygame.Rect((95, 407), (500, 25)))
		screen.blit(one, (100, 410))
		pygame.draw.rect(screen,(GRAY), pygame.Rect((95, 437), (500, 25)))
		screen.blit(three, (100, 440))
	else:
		pygame.draw.rect(screen,(GRAY), pygame.Rect((95, 407), (240, 25)))
		screen.blit(one, (100, 410))
		pygame.draw.rect(screen,(GRAY), pygame.Rect((345, 407), (240, 25)))
		screen.blit(two, (350, 410))
		pygame.draw.rect(screen,(GRAY), pygame.Rect((95, 437), (240, 25)))
		screen.blit(three, (100, 440))
		pygame.draw.rect(screen,(GRAY), pygame.Rect((345, 437), (240, 25)))
		screen.blit(four, (350, 440))
	pygame.display.update()

def getChoice(numchoices, m, n):
	print numchoices,"choices"
	if numchoices == 1:
		if m > 95 and m < 595 and n > 437 and n < 462:
			print "\tYou chose 1"
			return 1
		else:
			return 0
	elif numchoices == 2:
		if m > 95 and m < 595 and n > 407 and n < 432:
			print "\tYou chose 1"
			return 1
		elif m > 95 and m < 595 and n > 437 and n < 462:
			print "\tYou chose 2"
			return 2
		else:
			return 0
	else:
		if m > 95 and m < 305 and n > 407 and n < 432:
			print "\tYou chose 1"
			return 1
		elif m > 345 and m < 585 and n > 407 and n < 432:
			print "\tYou chose 2"
			return 2
		if m > 95 and m < 305 and n > 437 and n < 462:
			print "\tYou chose 3"
			return 3
		elif m > 345 and m < 585 and n > 437 and n < 462:
			print "\tYou chose 4"
			return 4
		else:
			return 0

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
		cloudsimg(cx,cy)
		cloudsimg(cx2,cy2)
                backgroundimg(background,x,y)
		titleimg(x,y)
		playimg(x,y)
                pygame.display.update()
                pygame.display.flip()
 
    # --- Game logic should go here
    scene1 = True
    while scene1 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene1 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
		print m,n
#                if m > 100 and m <204 and n < 460 and n > 440:
#                     answer = "y"
#                     scene2 = True
#                     scene1 = False
#                     print answer
#                elif m > 340 and m <550 and n < 439  and n > 455:
#                     answer = "n"
#                     scene2 = True
#                     scene1 = False
#                     print answer
                answer = getChoice(numchoices, m, n)
		#print answer
		if answer > 0:
			scene2 = True
			scene1 = False
                screen.fill(WHITE)
            else:
		drawScene("pictures/Silvia - thinking.png", "pictures/none.png", "pictures/dorm_bg.png")
		drawPrompt("So you wake up one fine Friday morning in your dorm room in PE to your alarm. You have an 8:20 class, but aren't sure if you want to go. Do you go?")
		drawChoices(numchoices, "Silvia", "Of Course!", " ", "Nah ma, stay in bed.", " ")
		pygame.display.update()
                pygame.display.flip()
        	scene2 = True
    
    while scene2 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene2 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
		print m,n
                answer = getChoice(numchoices, m, n)
		#print answer
		if answer > 0:
			scene3 = True
			scene2 = False
                screen.fill(WHITE)
                #scene2 = False
            else:
		drawScene("pictures/Silvia - sigh.png", "pictures/none.png", "pictures/dorm_bg.png")
		drawPrompt("That's a good idea. You've already paid an arm and a leg for it, anyways. You might as well go.")
		drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ")
		pygame.display.update()
                pygame.display.flip()
		scene3 = True 

    while scene3 and not done:
        for event in pygame.event.get():
	    numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene3 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
		print m,n
                answer = getChoice(numchoices, m, n)
		#print answer
		if answer > 0:
			scene4 = True
			scene3 = False
                screen.fill(WHITE)
                #scene3 = False
            else:
		drawScene("pictures/Silvia - neutral.png", "pictures/Abby - Sad.png", "pictures/hallway_bg.png")
		drawPrompt("It's 8:10 AM.  Parietals are still in effect but you notice your RA trying to sneak out a member of the opposite sex. She asks you if you're willing to keep it between the both of you.")
		drawChoices(numchoices, "Silvia", "..For a price", "Scream and Faint", "Look the other way", "Speedial #2 for the Rector")
		pygame.display.update()
                pygame.display.flip()
    		scene4 = True

    while scene4 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene4 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
		print m,n
                answer = getChoice(numchoices, m, n)
		#print answer
		if answer > 0:
			scene5 = True
			scene4 = False
                screen.fill(WHITE)
                #scene4 = False
            else:
		drawScene("pictures/Silvia - neutral.png", "pictures/Abby - Smiling.png", "pictures/hallway_bg.png")
		drawPrompt("They thank you for turning a blind eye and head out unnoticed. You walk to your first class.")
		drawChoices(numchoices, "Silvia", " ", " ",  "This might help you later...", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene5 = True
    
    while scene5 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene5 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
		print m,n
                answer = getChoice(numchoices, m, n)
		#print answer
		if answer > 0:
			scene6 = True
			scene5 = False
                screen.fill(WHITE)
                #scene5 = False
            else:
		drawScene("pictures/Silvia - smiling.png", "pictures/none.png", "pictures/hallway_bg.png")
		drawPrompt("After your last class of the day your friends invite you to a late lunch. Do you want to go?")
		drawChoices(numchoices, "Silvia", "Yes, I have a craving for cheese right now.", " ",  "No, I have a date wth Jay Brockman", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene6 = True

    while scene6 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene6 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
		print m,n
                answer = getChoice(numchoices, m, n)
		#print answer
		if answer > 0:
			scene7 = True
			scene6 = False
                screen.fill(WHITE)
                #scene5 = False
            else:
		drawScene("pictures/Silvia - smiling.png", "pictures/none.png", "pictures/hallway_bg.png")
		drawPrompt("After your last class of the day your friends invite you to a late lunch. Do you want to go?")
		drawChoices(numchoices, "Silvia", "Yes, I have a craving for cheese right now.", " ",  "No, I have a date wth Jay Brockman", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene7 = True

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
