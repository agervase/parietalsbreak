#!/usr/bin/env python
import string
import sys
import os
import pygame
import time

#globals
DORM = 'PE'
SUBPRN = 'she'
POSS = 'her'
DOP = 'her'
EIGHTWENTY = False
hallstaff = 0
numCheese = 0
distraction = 0
stamina = 0
ID = True
friendship = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (206, 206, 206)
RED = (255, 0, 0)
done = False # Loop until the user clicks the close button.


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

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite


while not done:
    homescreen = True
    scene4 = False
    scene4a = False
    scene5 = False
    scene6 = False
    scene6a = False
    scene6b = False
    scene7 = False
    scene8 = False
    scene8a = False
    scene8a2 = False
    scene8b = False
    scene9 = False
    scene10 = False
    scene11 = False
    scene12 = False
    scene13 = False
    scene14 = False
    scene15 = False
    scene16 = False
    scene17 = False
    scene18 = False
    scene19 = False
    scene20 = False
    scene21 = False
    scene22 = False
    scene23 = False
    scene23a = False
    scene24 = False
    scene25 = False
    scene26 = False
    scene27 = False
    scene27a = False
    scene28 = False
    scene28a = False
    scene29 = False
    scene30 = False
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

    scene4 = True
    while scene4 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene4 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                #print m,n
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene4a = True
                        scene4 = False
                elif answer ==2:
                        scene5 = True
                        scene4 = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - thinking.png", "pictures/none.png", "pictures/dorm_bg.png")
                drawPrompt("So you wake up one fine Friday morning in your dorm room in PE to your alarm. You have an 8:20 class, but aren't sure if you want to go. Do you go?")
                drawChoices(numchoices, "Silvia", "Of Course!", " ", "Nah ma, stay in bed.", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene4a = False
                #scene5 = False

    while scene4a and not done:
        for event in pygame.event.get():
            numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene4a = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                #print m,n
                answer = getChoice(numchoices, m, n)
                #print answer
                if answer > 0:
                        scene6 = True
                        scene4a = False
                screen.fill(WHITE)
                #scene2 = False
            else:
                drawScene("pictures/Silvia - sigh.png", "pictures/none.png", "pictures/dorm_bg.png")
                drawPrompt("That's a good idea. You've already paid an arm and a leg for it, anyways. You might as well go.")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene5 = False
                #scene6 = False

    while scene5 and not done:
        for event in pygame.event.get():
            numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene5 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                #print m,n
                answer = getChoice(numchoices, m, n)
                #print answer
                if answer > 0:
                        scene7 = True
                        scene5 = False
                screen.fill(WHITE)
                #scene2 = False
            else:
                drawScene("pictures/Silvia - sigh.png", "pictures/none.png", "pictures/dorm_bg.png")
                drawPrompt("That's fair, you were up pretty late doing your Systems homework, you deserve some more sleep.")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene7 = False
                #scene6 = False

    while scene6 and not done:
        for event in pygame.event.get():
            numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene6 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                #print m,n
                answer = getChoice(numchoices, m, n)
                #print answer
                if answer == 3:
                        scene6a = True
                        scene6 = False
		elif answer !=3 and answer>0:
			scene6b = True
			scene6 = False
                screen.fill(WHITE)
                #scene3 = False
            else:
                drawScene("pictures/Silvia - neutral.png", "pictures/Abby - Sad.png", "pictures/hallway_bg.png")
                drawPrompt("It's 8:10 AM.  Parietals are still in effect but you notice your RA trying to sneak out a member of the opposite sex. She asks you if you're willing to keep it between the both of you.")
                drawChoices(numchoices, "Silvia", "...For a price", "Scream and Faint", "Look the other way", "Speedial 2 for the Rector")
                pygame.display.update()
                pygame.display.flip()
                #scene6a = False
                #scene6b = False

    while scene6a and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene6a = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                #print pygame.mouse.get_pos()
                screen.fill(WHITE)
                if answer > 0:
			scene6a = False
			scene7 = True
            else:
                drawScene("pictures/Silvia - neutral.png", "pictures/Abby - Smiling.png", "pictures/hallway_bg.png")
                drawPrompt("They thank you for turning a blind eye and head out unnoticed. You walk to your first class.")
                drawChoices(numchoices, "Silvia", " ", " ",  "This might help you later...", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene7 = False

    while scene6b and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene6b = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                screen.fill(WHITE)
                if answer > 0:
			scene6b = False
			scene7 = True
            else:
                drawScene("pictures/Silvia - sigh.png", "pictures/Abby - Suspicious.png", "pictures/hallway_bg.png")
                drawPrompt("Your RA and their illegal guest manage to evade capture, but they're not happy that you didn't just look the other way, and they vow vengence upon you and all who wronged them...")
                drawChoices(numchoices, "Silvia", " ", " ",  "It's too early for this...", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene7 = False

    while scene7 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene7 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                #print m,n
                answer = getChoice(numchoices, m, n)
                #print answer
                if answer == 1:
                        scene8 = True
                        scene7 = False
		elif answer == 2:
                        scene12 = True
                        scene7 = False
                screen.fill(WHITE)
                #scene5 = False
            else:
                drawScene("pictures/Silvia - smiling.png", "pictures/none.png", "pictures/hallway_bg.png")
                drawPrompt("After your last class of the day your friends invite you to a late lunch. Do you want to go?")
                drawChoices(numchoices, "Silvia", "Yes, I have a craving for cheese right now.", " ",  "No, I have a date wth Jay Brockman", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene8 = False
                #scene12 = False

    while scene8 and not done:
        for event in pygame.event.get():
	    numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene8 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer == 4:
			scene8a = True
			scene8 = False
		elif answer > 0:
			scene8b = True
			scene8 = False
                screen.fill(WHITE)
                scene6 = False
            else:
                drawScene("pictures/Silvia - neutral.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
                drawPrompt("You and your friends head to NDH, the superior dining hall, and grab a seat. What kind of food are you hungry for?")
                drawChoices(numchoices, "Silvia", "Yes.", "Tacos", "Pizza", "A single slice of cheese")
                pygame.display.update()
                pygame.display.flip()
                #scene7 = True

    while scene8a and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene8a = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer > 0:
	                scene8a2 = True
	                scene8a = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
                drawPrompt("You pick a single slice of cheese because that's just the kind of monster that you are. You try to decorate it with tiny bits of lettuce to make the dish look more appealing. You failed. You proceed to eat it with a knife and fork. You take an extra piece of cheese to go.")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene8 = True

    CheeseC = 0
    while scene8a2 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene8a2 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
                        scene9 = True
                        scene8a2 = False
                screen.fill(WHITE)
            else:
                CheeseC += 5
                rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
                drawScene("pictures/none.png", "pictures/none.png", "pictures/rays.png")
                drawPrompt("You've acquired CHEESE!")
                drawChoices(numchoices,"Silvia", " ", " ", "Continue", " ");
                screen.blit(rotatedcheese, (200,0))
                pygame.display.update()
                pygame.display.flip()
                screen.fill(WHITE)
                #scene10 = True


    while scene8b and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene8b = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer > 0:
	                scene9 = True
	                scene8b = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
                drawPrompt("That sounds delicious! Dining hall food truly is a gift to Notre Dame students everywhere.")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene8 = True

    while scene9 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene9 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
	                scene10 = True
	                scene9 = False
		if answer == 2:
	                scene20 = True
	                scene9 = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
                drawPrompt("One of your friends is disappointed with the food selection and wants to go to the grocery store. She asks if you want to join.")
                drawChoices(numchoices, "Silvia", "Yes, I enjoy mooching rides off friends."," ", "No, I don't even like you."," ")
                pygame.display.update()
                pygame.display.flip()
                #scene9 = True

    while scene10 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene10 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer > 0:
	                scene11 = True
	                scene10 = False
                screen.fill(WHITE)
                #scene9 = False
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/cheese.png", "pictures/cafeteria_bg.png")
                drawPrompt("What a good friend! She's so appreciative that she buys you some cheese! You now head back to the dorm to get some work done.")
                drawChoices(numchoices,"Silvia", " ", " ", "Continue", " ");
                pygame.display.update()
                pygame.display.flip()
                #sceneCheese = True

    CheeseC = 0
    while scene11 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene11 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                        scene20 = True
                        scene11 = False
                screen.fill(WHITE)
            else:
                CheeseC += 5
                rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
                drawScene("pictures/none.png", "pictures/none.png", "pictures/rays.png")
                drawPrompt("You've acquired CHEESE!")
                drawChoices(numchoices,"Silvia", " ", " ", "Continue", " ");
                screen.blit(rotatedcheese, (200,0))
                pygame.display.update()
                pygame.display.flip()
                screen.fill(WHITE)
                #scene10 = True

    while scene12 and not done:
        for event in pygame.event.get():
	    numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene12 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                screen.fill(WHITE)
                #scene10 = False
		if answer == 1 or answer ==4:
			scene13 = True
			scene12 = False
		elif answer > 0:
			scene14 = True
			scene12 = False
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
                drawPrompt("Instead of going to the Dh, you head back to your dorm. On the way back, you run into someone from your section.")
                drawChoices(numchoices, "Silvia", "Wave at them", "Scream and faint", "Insult them", "Profess your love to them");
                pygame.display.update()
                pygame.display.flip()
                #scene11 = True

    while scene13 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene13 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene15 = True
			scene13 = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("That was nice of you it seems to have brightened their day. You know those random acts of kindness can really benefit you in the long run...")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene12 = True

    while scene14 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene14 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene15 = True
			scene14 = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - thinking.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("That's okay, they probably realize that you're too busy daydreaming about your VGA board...")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene12 = True

    while scene15 and not done:
	numchoices = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene15 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
			scene16 = True
			scene15 = False
		elif answer == 2:
			scene20 = True
			scene15 = False
                screen.fill(WHITE)
                #scene12 = False
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
                drawPrompt("When you get back to your dorm you realize it's been literally 6 years since you last exercised. Do you want to go for a quick run?")
                drawChoices(numchoices, "Silvia", "Heck yeah! Do you even lift bro?", " ", "Nah, I'm healthy enough.", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene13 = True

    while scene16 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene16 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
			scene17 = True
			scene16 = False
		elif answer == 2:
			scene18 = True
			scene16 = False
                #print pygame.mouse.get_pos()
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - Smiling.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Good idea, it's always good to stay healthy! On yourway back to your room, you run into your friend and they invite you back to their room. Do you want to go with them?")
                drawChoices(numchoices, "Silvia", "Yeah! Dude, they have Doritos!", " ", "Sorry, cant. My life is dope and I do dope stuff", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene14 = True

    while scene17 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene17 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene20 = True
			scene17 = False
                screen.fill(WHITE)
                #scene14 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("You and your friend have a great time talking about how Verilog is a hardware description language and enjoying that life-changing cool ranch flavor.")
                drawChoices(numchoices, "Silvia"," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene15 = True

    while scene18 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene18 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene20 = True
			scene18 = False
                screen.fill(WHITE)
                #scene14 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Your friend understands they can never reach your level of dopeness and sends you on your way with a sense of awe at all the dope stuff you're gonna do. You walk away thinking about how Verilog is a hardware description language.")
                drawChoices(numchoices, "Silvia"," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene15 = True

    while scene20 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene20 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene21 = True
                        scene20 = False
                elif answer == 2:
                        scene25 = True
                        scene20 = False
                screen.fill(WHITE)
                #scene16 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Now that you're back in your room, your roomate asks if you wan to take a stroll around the dorm or just stay in your room and play Lego Star Wars on her emulator and order Knotty Knoodles.")
                drawChoices(numchoices, "Silvia", "Walk around", " ", "Stay because Knoodles, duh!", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene17 = True

    while scene21 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene17 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene22 = True
			scene21 = False
                screen.fill(WHITE)
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("As you walk around, you notice that one of the side doors is blocked for construction because of the Great PE Flood of 2016. The guy who build this dorm deserves an award, really. If you need to exit, you CANNOT exit throught the WEST-FACING door.")
                drawChoices(numchoices, "Silvia"," ", " ", " Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                scene18 = True

    while scene22 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene22 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene23 = True
                        scene22 = False
                elif answer == 2:
                        scene24 = True
                        scene22 = False
                screen.fill(WHITE)
                #scene16 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("As you walk, you notice some empty rooms. Do you want to peek inside?")
                drawChoices(numchoices, "Silvia","Yeah, totally not creepy."," ", "Nah, I'm good.", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene17 = True

    while scene23 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene23 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene23a = True
                        scene23 = False
                screen.fill(WHITE)
                #scene19 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("You see your neighbor has left some food out on their desk with a sign encouraging people to take some, so you do. They left cheese! Your single slice of cheese now has a friend. You head back to your room.")
                drawChoices(numchoices, "Silvia"," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene20 = True

    CheeseC = 0
    while scene23a and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene23a = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                        scene25 = True
                        scene23a = False
                screen.fill(WHITE)
            else:
                CheeseC += 5
                rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
                drawScene("pictures/none.png", "pictures/none.png", "pictures/rays.png")
                drawPrompt("You've acquired CHEESE! You decide you're done exploring and head back to your room to play pikmin with your roommate.")
                drawChoices(numchoices,"Silvia", " ", " ", "Continue", " ");
                screen.blit(rotatedcheese, (200,0))
                pygame.display.update()
                pygame.display.flip()
                screen.fill(WHITE)
                #scene10 = True

    while scene24 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene24 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene25 = True
                        scene24 = False
                screen.fill(WHITE)
                #scene19 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("You decide to not be a creep, and you don't go into the room. You go back to your room to play Pikmin and watch Nacho Libre with your roommate.")
                drawChoices(numchoices, "Silvia"," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene20 = True

    while scene25 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene25 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene26 = True
                        scene25 = False
                screen.fill(WHITE)
                #scene21 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("You literally suck at Pikmin and accidentally drown half of your Pikmin friends. It's  getting pretty late and your roommate asks the all-important question...")
                drawChoices(numchoices, "Silvia"," ", " ", "I'm listening...", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene22 = True

    while scene26 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene26 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene27 = True
                        scene26 = False
                elif answer == 2:
                        scene28 = True
                        scene26 = False
                screen.fill(WHITE)
                #scene22 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Do you want to go out this lovely Friday night (to have wholesome fun drinking non-alcoholic juice-based beverages that were definitely not made in a trash can and probably play some charades?)")
                drawChoices(numchoices, "Silvia","Hell yea, I love \"charades\"!", " ", "Nah, let's get a milkshake from Smashburger.", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene23 = True

    while scene27 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene27 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene27a = True
                        scene27 = False
                screen.fill(WHITE)
                #scene23 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Due to some wild and unforseen consequences that involve a party cab, barbecue sauce, a stolen American flag, and the Polish festival of Dingus Day, you find yourself after 2am with a member of the opposite gender!")
                drawChoices(numchoices, "Silvia", " ", " ", "Oh, no", " ")
                pygame.display.update()
                pygame.display.flip()
                #scene24 = True

    while scene27a and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene27a = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene29 = True
                        scene27a = False
                screen.fill(WHITE)
                scene24 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Because we're obviously not adults capable of making decisions, the RA's are patrolling, looking for any stray males in the building but your guest wants to get to bed.")
                drawChoices(numchoices, "Silvia", " ", " ", "Continue.", " ");
                pygame.display.update()
                pygame.display.flip()
                scene25 = True

    while scene28 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene28 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
			scene28a = True
			scene28 = False
                screen.fill(WHITE)
                #scene26 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("You should have foreseen this, but in your excitement you forgot the inevitable result of obtaining a milkshake. Your milkshake brought all the boys to your yard! And by yard I mean extremely small dorm room!")
                drawChoices(numchoices, "Silvia", " ", " ", "Well, at least it's better than yours.", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene27 = True

    while scene28a and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene28 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                #print pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene29 = True
                        scene28a = False
                screen.fill(WHITE)
                #scene27 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("You manage to herd them out, but as the clock strikes 2am, you realize that there is one remaining member of the opposite gender!")
                drawChoices(numchoices, "Silvia", " ", " ", "Uh oh...", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene28 = True

    while scene29 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene29 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                #print pygame.mouse.get_pos()
                if answer == 1:
                        scene30 = True
                        scene29 = False
                screen.fill(WHITE)
                #scene25 = False
            else:
                drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
                drawPrompt("Looks like you're gonna have to facilitate a PARIETALS BREAK!")
                drawChoices(numchoices, "Silvia", " ", " ", "Bring it.", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene26 = True


