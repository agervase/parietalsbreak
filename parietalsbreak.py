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
name = "Silvia"
gender = "girl"
oppgender = "boy"
last = 71


## a simple class that uses the generator
# and can tell if it is done
pygame.mixer.init(44100, -16,2,2048)
pygame.init()

font = pygame.font.Font("Fonts/Aaargh.ttf", 15)

# raise the USEREVENT every 1000ms
pygame.time.set_timer(pygame.USEREVENT, 200)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Parietals Break")

# Background Music
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background = pygame.image.load(dictpics["front_layer_title"])
background = pygame.transform.scale(background, (700, 500))

clouds = pygame.image.load(dictpics["clouds"])

title = pygame.image.load(dictpics["title_text"])

play = pygame.image.load(dictpics["play"])

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
        backgroundimg(pygame.image.load(dictpics["textBox"]), x, y);

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
        if numchoices == 1:
                if m > 95 and m < 595 and n > 437 and n < 462:
                        return 1
                else:
                        return 0
        elif numchoices == 2:
                if m > 95 and m < 595 and n > 407 and n < 432:
                        return 1
                elif m > 95 and m < 595 and n > 437 and n < 462:
                        return 2
                else:
                        return 0
        else:
                if m > 95 and m < 305 and n > 407 and n < 432:
                        return 1
                elif m > 345 and m < 585 and n > 407 and n < 432:
                        return 2
                if m > 95 and m < 305 and n > 437 and n < 462:
                        return 3
                elif m > 345 and m < 585 and n > 437 and n < 462:
                        return 4
                else:
                        return 0

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def makedict(gender):
    mypath = dictpics[""
    pictures = [mypath+f for f in os.listdir(mypath) if os.path.isfile(mypath+f)]
    pickeys = [(os.path.splitext(f)[0]).replace(" ","") for f in os.listdir(mypath) if os.path.isfile(mypath+f)]
    dictpics = dict(zip(pickeys,pictures))
    return dictpics



while not done:
    dictpics = makedict(gender)
    scene = 1
    while scene==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene1 = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                if m > 335 and m < 390 and n > 155 and n < 185:
                   screen.fill(WHITE)
		   scene=2
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

    while scene==2 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene=last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                	if answer ==1:
				gender = "girl" #should be gender = "boy"
				oppgender = "girl"
				SUBPRN = "he"
				POSS = "his"
				DOP = "him"
	                scene=3
			dictpics = makedict(gender)
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"], dictpics["none"], dictpics["dorm_bg"])
                drawPrompt("First things first, do you identify more as a boy or a girl?")
                drawChoices(numchoices, " ", "Boy", " ", "Girl", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==3 and not done:
        for event in pygame.event.get():
            numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene=last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 1:
			if answer ==1:
				name = "Silvia"
			if answer ==2:
				name = "Beter Pui"
			if answer ==3:
				name = "Kreya Shumar"
			if answer ==4:
				name = "Bray Jockman"
                        scene=4
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"], dictpics["none"], dictpics["dorm_bg"])
                drawPrompt("Which name do you think best represents you as a person?")
                drawChoices(numchoices, " ", "Silvia", "Beter Pui", "Kreya Shumar", "Bray Jockman")
                pygame.display.update()
                pygame.display.flip()

    while scene==4 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene=5
                elif answer ==2:
                        scene=6
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"], dictpics["none"], dictpics["dorm_bg"])
                drawPrompt("So you wake up one fine Friday morning in your dorm room in PE to your alarm. You have an 8:20 class, but aren't sure if you want to go. Do you go?")
                drawChoices(numchoices, name, "Of Course!", " ", "Nah ma, stay in bed.", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==5 and not done:
        for event in pygame.event.get():
            numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                        scene=7
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-sigh"], dictpics["none"], dictpics["dorm_bg"])
                drawPrompt("That's a good idea. You've already paid an arm and a leg for it, anyways. You might as well go.")
                drawChoices(numchoices, name, " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==6 and not done:
        for event in pygame.event.get():
            numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                        scene = 10
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-sigh"], dictpics["none"], dictpics["dorm_bg"])
                drawPrompt("That's fair, you were up pretty late doing your Systems homework, you deserve some more sleep.")
                drawChoices(numchoices, name, " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==7 and not done:
        for event in pygame.event.get():
            numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 3:
                        scene = 8
			hallstaff=hallstaff+1
		elif answer !=3 and answer>0:
			scene = 9
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-neutral"], dictpics["RA-Sad"], dictpics["hallway_bg"])
                drawPrompt("It's 8:10 AM.  Parietals are still in effect but you notice your RA trying to sneak out a "+oppgender+", and "+SUBPRN+" asks you if you're willing to keep it between the two of you.")
                drawChoices(numchoices, name, "...For a price", "Scream and Faint", "Look the other way", "Speedial 2 for the Rector")
                pygame.display.update()
                pygame.display.flip()

    while scene==8 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                screen.fill(WHITE)
                if answer > 0:
			scene = 10
            else:
                drawScene(dictpics["main-neutral"], dictpics["RA-Smiling"], dictpics["hallway_bg"])
                drawPrompt("Your RA thanks you for turning a blind eye and head out unnoticed. You walk to your first class.")
                drawChoices(numchoices, name, " ", " ",  "This might help you later...", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==9 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                screen.fill(WHITE)
                if answer > 0:
			scene = 10
            else:
                drawScene(dictpics["main-sigh"], dictpics["RA-Suspicious"], dictpics["hallway_bg"])
                drawPrompt("Your RA and their illegal guest manage to evade capture, but "+SUBPRN+" is not happy that you didn't just look the other way, and "+SUBPRN+" vows vengence upon you and all who wronged "+DOP+"...")
                drawChoices(numchoices, name, " ", " ",  "It's too early for this...", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==10 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 11
			friendship = friendship+1
		elif answer == 2:
                        scene = 18
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-smiling"], dictpics["none"], dictpics["hallway_bg"])
                drawPrompt("After your last class of the day your friends invite you to a late lunch. Do you want to go?")
                drawChoices(numchoices, name, "Yes, I have a craving for cheese right now.", " ",  "No, I have a date wth Jay Brockman", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==11 and not done:
        for event in pygame.event.get():
	    numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer == 4:
			scene=12
			numCheese = numCheese+1
		elif answer > 0:
			scene = 14
                screen.fill(WHITE)
                scene6 = False
            else:
                drawScene(dictpics["main-neutral"], dictpics["friendDH-Smiling"], dictpics["cafeteria_bg"])
                drawPrompt("You and your friends head to NDH, the superior dining hall, and grab a seat. What kind of food are you hungry for?")
                drawChoices(numchoices, name, "Yes.", "Tacos", "Pizza", "A single slice of cheese")
                pygame.display.update()
                pygame.display.flip()

    while scene==12 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer > 0:
	                scene = 13
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"], dictpics["friendDH-Smiling"], dictpics["cafeteria_bg"])
                drawPrompt("You pick a single slice of cheese because that's just the kind of monster that you are. You try to decorate it with tiny bits of lettuce to make the dish look more appealing. You failed. You proceed to eat it with a knife and fork. You take an extra piece of cheese to go.")
                drawChoices(numchoices, name, " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    CheeseC = 0
    while scene==13 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
                        scene = 15
                screen.fill(WHITE)
            else:
                CheeseC += 5
                rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
                drawScene(dictpics["none"], dictpics["none"], dictpics["rays"])
                drawPrompt("You've acquired CHEESE!")
                drawChoices(numchoices,name, " ", " ", "Continue", " ");
                screen.blit(rotatedcheese, (200,0))
                pygame.display.update()
                pygame.display.flip()
                screen.fill(WHITE)


    while scene==14 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer > 0:
	                scene = 15
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"], dictpics["friendDH-Smiling"], dictpics["cafeteria_bg"])
                drawPrompt("That sounds delicious! Dining hall food truly is a gift to Dotre Name students everywhere.")
                drawChoices(numchoices, name, " ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==15 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
	                scene = 16
			numCheese = numCheese+1
		if answer == 2:
	                scene = 26
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"], dictpics["friendDH-Smiling"], dictpics["cafeteria_bg"])
                drawPrompt("One of your friends is disappointed with the food selection and wants to go to the grocery store. She asks if you want to join.")
                drawChoices(numchoices, name, "Yes, I enjoy mooching rides off friends."," ", "No, I don't even like you."," ")
                pygame.display.update()
                pygame.display.flip()

    while scene==16 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
		if answer > 0:
	                scene = 17
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"], dictpics["cheese"], dictpics["cafeteria_bg"])
                drawPrompt("What a good friend! She's so appreciative that she buys you some cheese! You now head back to the dorm to get some work done.")
                drawChoices(numchoices,name, " ", " ", "Continue", " ");
                pygame.display.update()
                pygame.display.flip()

    CheeseC = 0
    while scene==17 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                        scene = 26
                screen.fill(WHITE)
            else:
                CheeseC += 5
                rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
                drawScene(dictpics["none"], dictpics["none"], dictpics["rays"])
                drawPrompt("You've acquired CHEESE!")
                drawChoices(numchoices,name, " ", " ", "Continue", " ");
                screen.blit(rotatedcheese, (200,0))
                pygame.display.update()
                pygame.display.flip()
                screen.fill(WHITE)

    while scene==18 and not done:
        for event in pygame.event.get():
	    numchoices = 4
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                screen.fill(WHITE)
		if answer == 1 or answer == 4:
			scene = 19
			distraction = distraction + 1
		elif answer > 0:
			scene = 20
            else:
                drawScene(dictpics["main-Smiling"], dictpics["friendDH-Smiling"], dictpics["pasq_bg"])
                drawPrompt("Instead of going to the DH, you head back to your dorm. On the way back, you run into someone from your section.")
                drawChoices(numchoices, name, "Wave at "+DOP, "Scream and faint", "Insult "+DOP, "Profess your love to "+DOP);
                pygame.display.update()
                pygame.display.flip()

    while scene==19 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene = 21
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"], dictpics["friendDH-Smiling"], dictpics["pasq_bg"])
                drawPrompt("That was nice of you it seems to have brightened "+POSS+" day. You know those random acts of kindness can really benefit you in the long run...")
                drawChoices(numchoices, name, " ", " ", "Continue", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==20 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene14 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene = 21 
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"], dictpics["none"], dictpics["forest_bg"])
                drawPrompt("That's okay, "+SUBPRN+" probably realizes that you're too busy daydreaming about your VGA board...")
                drawChoices(numchoices, name, " ", " ", "Continue", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==21 and not done:
	numchoices = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
			scene = 22
			stamina = stamina+1
		elif answer == 2:
			scene = 26
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"], dictpics["none"], dictpics["dorm_bg"])
                drawPrompt("When you get back to your dorm you realize it's been literally 6 years since you last exercised. Do you want to go for a quick run?")
                drawChoices(numchoices, name, "Heck yeah! Do you even lift bro?", " ", "Nah, I'm healthy enough.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==22 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
			scene = 23
			friendship = friendship+1
		elif answer == 2:
			scene = 24
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"],dictpics["friendRoom-Smiling"],dictpics["pasq_bg"])
                drawPrompt("Good idea, it's always good to stay healthy! On yourway back to your room, you run into your friend and "+SUBPRN+" invites you back to "+POSS+" room. Do you want to go with "+DOP+"?")
                drawChoices(numchoices, name, "Yeah! Dude, "+SUBPRN+" have Doritos!", " ", "Sorry, cant. My life is dope and I do dope stuff", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==23 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene = 26
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"],dictpics["friendRoom-Smiling"],dictpics["dorm_bg"])
                drawPrompt("You and your friend have a great time talking about how Verilog is a hardware description language and enjoying that life-changing cool ranch flavor.")
                drawChoices(numchoices, name," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==24 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene18 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene = 26
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["friendRoom-Awe"],dictpics["forest_bg"])
                drawPrompt("Your friend understands that "+SUBPRN+" can never reach your level of dopeness and sends you on your way with a sense of awe at all the dope stuff you're gonna do. You walk away thinking about how Verilog is a hardware description language.")
                drawChoices(numchoices, name," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==26 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 27
                elif answer == 2:
                        scene = 32
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"],dictpics["roommate-Smiling"],dictpics["dorm_bg"])
                drawPrompt("Now that you're back in your room, your roomate asks if you wan to take a stroll around the dorm or just stay in your room and play Lego Star Wars on her emulator and order Knotty Knoodles.")
                drawChoices(numchoices, name, "Walk around", " ", "Stay because Knoodles, duh!", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==27 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer > 0:
			scene = 28
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-sigh"],dictpics["roommate-Suspicious"],dictpics["hallway_bg"])
                drawPrompt("As you walk around, you notice that one of the side doors is blocked for construction because of the ninth Great PE Flood of 2016. The guy who build this dorm deserves an award, really. If you need to exit, you CANNOT exit throught the WEST-FACING door.")
                drawChoices(numchoices, name," ", " ", " Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==28 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 29
			numCheese = numCheese+1
                elif answer == 2:
                        scene = 31
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"],dictpics["none"],dictpics["hallway_bg"])
                drawPrompt("As you walk, you notice some empty rooms. Do you want to peek inside?")
                drawChoices(numchoices, name,"Yeah, totally not creepy."," ", "Nah, I'm good.", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==29 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 30
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Smiling"],dictpics["none"],dictpics["dorm_bg"])
                drawPrompt("You see your neighbor has left some food out on "+POSS+" desk with a sign encouraging people to take some, so you do. "+SUBPRN+" left cheese! Your single slice of cheese now has a friend. You head back to your room.")
                drawChoices(numchoices, name," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    CheeseC = 0
    while scene==30 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer > 0:
                        scene = 32
                screen.fill(WHITE)
            else:
                CheeseC += 5
                rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
                drawScene(dictpics["none"],dictpics["none"],dictpics["rays"])
                drawPrompt("You've acquired CHEESE! You decide you're done exploring and head back to your room to play pikmin with your roommate.")
                drawChoices(numchoices,name, " ", " ", "Continue", " ");
                screen.blit(rotatedcheese, (200,0))
                pygame.display.update()
                pygame.display.flip()
                screen.fill(WHITE)

    while scene==31 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 32
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Nacho"],dictpics["none"],dictpics["hallway_bg"])
                drawPrompt("You decide to not be a creep, and you don't go into the room. You go back to your room to play Pikmin and watch Nacho Libre with your roommate.")
                drawChoices(numchoices, name," ", " ", "Continue", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==32 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 33
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"],dictpics["roommate-Smiling"],dictpics["dorm_bg"])
                drawPrompt("You literally suck at Pikmin and accidentally drown half of your Pikmin friends. It's  getting pretty late and your roommate asks the all-important question...")
                drawChoices(numchoices, name," ", " ", "I'm listening...", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==33 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 34
                elif answer == 2:
                        scene = 36
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-thinking"],dictpics["roommate-Worried"],dictpics["dorm_bg"])
                drawPrompt("Do you want to go out this lovely Friday night (to have wholesome fun drinking non-alcoholic juice-based beverages that were definitely not made in a trash can and probably play some charades?)")
                drawChoices(numchoices, name,"Hell yea, I love \"charades\"!", " ", "Nah, let's get a milkshake from Smashburger.", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==34 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 35
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-sigh"],dictpics["oppgen-Sad"],dictpics["dorm_bg"])
                drawPrompt("Due to some wild and unforseen consequences that involve a party cab, barbecue sauce, a stolen American flag, and the Polish festival of Dingus Day, you find yourself after 2am with a member of the opposite gender!")
                drawChoices(numchoices, name, " ", " ", "Oh, no", " ")
                pygame.display.update()
                pygame.display.flip()

    while scene==35 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene29 = 38
                screen.fill(WHITE)
                scene24 = False
            else:
                drawScene(dictpics["main-Sad"],dictpics["oppgen-Sad"],dictpics["dorm_bg"])
                drawPrompt("Because we're obviously not adults capable of making decisions, the RA's are patrolling, looking for any stray males in the building but your guest wants to get to bed.")
                drawChoices(numchoices, name, " ", " ", "Continue.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==36 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
		if answer == 1:
			scene = 37
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-sigh"],dictpics["oppositegender"],dictpics["dorm_bg"])
                drawPrompt("You should have foreseen this, but in your excitement you forgot the inevitable result of obtaining a milkshake. Your milkshake brought all the "+oppgender+"s to your yard! And by yard I mean extremely small dorm room!")
                drawChoices(numchoices, name, " ", " ", "Well, at least it's better than yours.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==37 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 38
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["oppgen-Sad"],dictpics["dorm_bg"])
                drawPrompt("You manage to herd them out, but as the clock strikes 2am, you realize that there is one remaining member of the opposite gender in your room!")
                drawChoices(numchoices, name, " ", " ", "Uh oh...", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==38 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			if gender[0]=='b':
				scene = 39
			else:
	                        scene = 40
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["oppgen-Sad"],dictpics["dorm_bg"])
                drawPrompt("Looks like you're gonna have to facilitate a PARIETALS BREAK!")
                drawChoices(numchoices, name, " ", " ", "Bring it.", " ");
                pygame.display.update()
                pygame.display.flip()

############# possible day to night transition scene 39 ###############
    while scene==39 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			scene = 70
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("You literally just walk the girl downstairs. She high-fives you rector on the way out. Congrats, you win Parietals Break and the gender lottery. Have fun making more money than me for the rest of your life.")
                drawChoices(numchoices, name, " ", " ", "Don't worry, I will", " ");
                pygame.display.update()
                pygame.display.flip()


    while scene==40 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 41
                if answer == 2:
                        scene = 48
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("All right, it's time to get this boy to freedom. You've got to make a run for the staircases. Your room is right in the middle, do you want to go for the main staircase or the side staircase?")
                drawChoices(numchoices, name, "Main staircase", " ", "Side staircase", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==41 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 42
                if answer == 2:
                        scene = 45
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("You hear someone jamming to country in the e-lounge. You are afraid because this person might get you in trouble for the boy and because country music is inherently terrifying. What do you do?")
                drawChoices(numchoices, name, "Make a break for the staircase", " ", "Wait it out.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==42 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1 and hallstaff > 0:
                        scene = 43
		elif answer == 1:
			scene = 44
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("The person in the e-lounge is your RA!")
                drawChoices(numchoices, name, " ", " ", "Dun dun DUUUUUUUN", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==43 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 53
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Luckily, since you looked the other way for her this morning, she's willing to look the other way for you now. You make it to the staircase and down one floor.")
                drawChoices(numchoices, name, " ", " ", "Frick yeah, this is easy.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==44 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 69
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Game Over"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("After the vengence she swore upon you this morning, she happily calls up your Rector and gets you in trouble. You and your male guest have to write letters of apology to Touchdown Jesus.")
                drawChoices(numchoices, name, " ", " ", "RIP", " ");
                pygame.display.update()
                pygame.display.flip()
	
    while scene==45 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1 and numCheese>2:
                        scene = 46
		elif answer == 1:
                        scene = 47
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("You're so distracted listening for the person in the e-lounge that you don't even notice your Rector coming up behind you!")
                drawChoices(numchoices, name, " ", " ", "Frick", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==46 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 53 ########## I think???????
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Luckily, you are able to distract her with some of her favorite food: CHEESE. You've picked up more than two slices today, just enough to distract her as the two of you slip away! You make it to the staircase and down one floor.")
                drawChoices(numchoices, name, " ", " ", "Sweeeeeeet", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==47 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 69
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Game Over"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("She says she isn't mad, just disappointed, but she definitely looks pretty mad. You and your male friend get in lots of trouble. The two of you have to write letters of apology to Erin Hoffman Harding.")
                drawChoices(numchoices, name, " ", " ", "RIP", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==48 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 51
                elif answer == 2:
			if friendship > 0:
	                        scene = 49
			else:
				scene = 50
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("You hear someone someone coming, and with your incredible hearing, you immediately determine that it's one of your dorm's ARs. What do you do?")
                drawChoices(numchoices, name, "Make a break for the staircase", " ", "Ask a friend to hide you.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==49 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 53 ########## I think???????
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Luckily, since you have such a strong bond, she's willing to hide you while you wait for the AR to pass. You make it to the staircase and down one floor.")
                drawChoices(numchoices, name, " ", " ", "Ah, the magic of friendship.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==50 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 69
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Game Over"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Uh oh, your friend is feeling petty today and doesn't let you in! She lets you get caught by your AR and you get in trouble. You and your male guest have to write letters of apology to Father John I. Jenkins, C.S.C.")
                drawChoices(numchoices, name, " ", " ", "*insert you tried star*", " ");
                pygame.display.update()
                pygame.display.flip()
                #scene25 = True

    while scene==51 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 52
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Your AR obviously sees you immediately, what did you expect yo happen???")
                drawChoices(numchoices, name, " ", " ", "... Not that?", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==52 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene42a = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene59 = 69
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Game Over"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Well thanks to your poor decision making, your AR gets youin trouble. You and your male guest have to write letters of apology to Brian Kelly since our awful football season was obviously your fault.")
                drawChoices(numchoices, name, " ", " ", "I done messed up", " ");
                pygame.display.update()
                pygame.display.flip()
	
    while scene==53 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 63
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("I don't have the story for this floor written yet...")
                drawChoices(numchoices, name, " ", " ", "Wow Abby you should get on that.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==63 and not done:
        for event in pygame.event.get():
            numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 68
                if answer == 2:
                        scene = 64
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("You just need to get down one more staircase, but the main one is blocked by a group of freshmen who had waaaaaaaay too much fun playing charades. Do you want to try to exit from the NORTH-FACING or WEST-FACING staircase?")
                drawChoices(numchoices, name, "North staircase", " ", "West staircase", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==64 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			if numCheese >= 3:
                        	scene = 65
			elif distraction > 0 and stamina > 0:
				scene = 66
			else:
				scene = 67
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Uh oh, the West staircase is underconstruction! If only they used the money for preventing flooding towards your tuition (cough, 3.7% cough)... You try to run for the north staircase, but you run into your Rector.")
                drawChoices(numchoices, name, " ", " ", "Why does the universe hate me?", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==65 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			scene = 70
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Luckily, you have so much cheese on your person, that you are able to convince her to look the other way. You and your male friend ESCAPE.")
                drawChoices(numchoices, name, " ", " ", "ALL HAIL THE CHEESE", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==66 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			scene = 70
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("Lucky for you, the girl from your section that you were nice to earlier distracts your rector for a few seconds. Thanks to your run, your legs are energized enough to make a mad dash for the north staircase. You make it in the nick of time, and you and your male friend ESCAPE.")
                drawChoices(numchoices, name, " ", " ", "Wow, I've learned a valuable lesson about random acts of kindness.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==67 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
                        scene = 69
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-Game Over"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("She tells you that she expected better of you, and you not only get in trouble, but also feel guilty, so that sucks. You and your male guest have to write letters of apology to the societal expectations of womanhood that force Catholics to try to preserve female innocence.")
                drawChoices(numchoices, name, " ", " ", "Darn societal expectations.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==68 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			scene = 70
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("You and your male friend manage to slip out the NORTH door into the dead of night. You share a firm handshake and go your separate ways...")
                drawChoices(numchoices, name, " ", " ", "My life is basically Shawshank Redemption.", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==70 and not done:
        for event in pygame.event.get():
	    numchoices = 1
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			scene = 69
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("CONGRATULATIONS, YOU HAVE SUCCESSFULLY BROKEN PARIETALS!!")
                drawChoices(numchoices, name, " ", " ", "Continue...", " ");
                pygame.display.update()
                pygame.display.flip()

    while scene==69 and not done:
        for event in pygame.event.get():
	    numchoices = 2
            if event.type == pygame.QUIT:
                done = True
                scene = last
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
		answer = getChoice(numchoices, m, n)
                if answer == 1:
			scene = 1
		if answer == 2:
			done = True
                screen.fill(WHITE)
            else:
                drawScene(dictpics["main-GTFO"],dictpics["none"],dictpics["forest_bg"])
                drawPrompt("This game was brought to you by PE Room 616 (#squadhouse). We'd like to thank all the h8rs for inspiring us. Silvia would also like everyone to know that she hates all the orphans in the whole world.")
                drawChoices(numchoices, " ", "This game was amazing and I want to play again!", " ", "This was the worst experience of my whole life", " ");
                pygame.display.update()
                pygame.display.flip()



sys.exit(0)
