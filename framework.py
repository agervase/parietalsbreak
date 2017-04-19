#!/usr/bin/env python
import string
import sys

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

print "Hello! Welcome fo Parietals Break!"
person = raw_input("Enter your name: ")
print "Hello", person+"!\n"

answer = raw_input("What dorm are you in, PE or Knott? ")
if answer.lower() == 'pe': 
    DORM = 'PE'
elif answer.lower() == 'knott':
    DORM = 'Knott'
    SUBPRN = 'he'
    POSS = 'his'
    DOP = 'him'

print "Great, so you're",person,"from",DORM+"!\n"

print "So you wake up one fine Friday morning in your"
print "dorm room in",DORM,"to your alarm. You have an"
print "8:20 class, but you aren't sure you want to go"
answer = raw_input("to it. Do you go? Yes or no? ")
if answer[0].lower() == 'y':
    print "\nThat's a good idea. You've already paid for it,"
    print "You might as well go\n"
    EIGHTWENTY = True
else:
    print "\nThat's fair, you were up pretty late doing your"
    print "Systems homework, you deserve some more sleep.\n"

if EIGHTWENTY:
    print "As you leave for your class, you see your RA"
    print "trying to open",POSS, "door while carrying a"
    print "heavy-looking box. You help",DOP,"open the door,"
    print "and",SUBPRN,"is very appreciative. This could help"
    print "you out later...\n"
    hallstaff = hallstaff+1

print "Okay, so after your last class of the day, your"
print "friends invite you to a late lunch. Do you want"
answer = raw_input( "to go with them? Yes or no? ")

if answer[0].lower() == 'y':
    friendship = friendship+1
    print "\nYou and your friends head to NDH, the surperior"
    print "dining hall, and grab a seat. What kind of food are"
    print "you hungry for?"
    print "\t1. Salad"
    print "\t2. Tacos"
    print "\t3. Literally just a single slice of cheese"
    print "\t4. Pizza"
    food = raw_input("Choice: ")
    if food=='3':
        numCheese = numCheese+1
    print "Good choice, that sounds delicious!\n"
    print "\nOne of your friends is disappointed with the food"
    print "selection and wants to go to the grocery store. Do"
    store = raw_input("you want to go with her? Yes or no? ")
    if store[0].lower() == 'y':
        print "\nWhat a good friend! She's so appreciative that"
        print "she buys you some cheese!"
        if food=='3':
            "\nWow, you're getting a lot of cheese today!"
        numCheese = numCheese+1
    print "\nYou now head back to",DORM,"to get some work done.\n"

else:
    print "\nInstead of going back to the DH, you head back to",DORM
    print "to get some work done. On the way back, you run into"
    print "someone from your section. Do you wave at",DOP+"?"
    wave = raw_input("Yes or no? ")
    if wave[0].lower() == 'y':
        print "\nThat was nice of you, it seems to have brightened",POSS
        print "day. You know those random acts of kindness can really"
        print "benefit you in the long run...\n"
        distraction = distraction +1
    else:
        print "\nThat's okay,",SUBPRN, "probably realizes that you're in a rush.\n"
    print "When you get back to",DORM,"you realize that it's been"
    print "literally 6 years since you last exercised. Do you want"
    run = raw_input("to go for a quick run? Yes or no? ")
    if run[0].lower() == 'y':
        print "\nGood idea, it's always good to stay healthy!\n"
        stamina = stamina+1
        print "On your way back to your room, you run into your friend and"
        print SUBPRN,"invites you back to",POSS,"room. Do you go with",DOP+"?"
        room = raw_input("Yes or no? ")
        if room[0].lower() == 'y':
            print "\nYou and your friend have a great time hanging out, but"
            print "on your way back to your room you realize you're missing"
            print "your ID! Wonder where that could be...\n"
            ID = False
        else:
            print "\nYour friend understands, you're pretty sweaty...\n"
    else:
        print "\nThat's okay, we all know exercising is literally the worst\n"


print "Now that you're back in your room, your roommate asks if"
print "you want to take a stroll around the dorm or just stay"
print "in your room and play GameCube. Which do you want to do?"
print "\t1. Walk around",DORM
print "\t2. Play GameCube"
answer = raw_input("Choice: ")
if answer=='1':
    print "\nAs you walk around, you notice that one of the side doors"
    print "blocked for construction as they try yet again to prevent"
    print "flooding in the hallway. If you need to exit, you CANNOT"
    print "exit through the WEST-FACING door.\n"
    print "As you walk, you notice some empty rooms. Do you want to peek"
    peak = raw_input("inside? Yes or no? " )
    if peak[0].lower() == 'y':
        print "\nYou see your neighbor has left some food out on their desk with"
        print "A sign encouraging people to take some, so you do.\n"
        numCheese = numCheese+1
    else:
        print "\nYeah, it's always best to respect people's privacy.\n"
else:
    print "\nYou have a blast playing Pikmin.\n"

print "Now that it's getting late, your roommate asks you the all-important"
print "question: do you want to go out on this lovely Friday night (to have"
print "wholesome fun drinking non-alcoholic juice-based beverages that were"
print "definitely not made in a trash can and probably play some charades)?"
answer = raw_input("Yes or no? ")
if answer[0].lower() == 'y':
    print "\nDue to some wild and unforseen consequences that involve a party cab,"
    print "poster theft, and the Polish festival of Dingus Day, you find yourself"
    print "in your room after 2am with a member of the opposite gender! The RAs are"
    print "patrolling, but your guest wants to get to bed. Looks like you're gonna"
    print "have to facilitate a PARIETALS BREAK!!!\n"
else:
    print "\nThat's okay, you've had a long day. Your friend asks if you want to"
    print "grab a milkshake from Smashburger before bed. Do you go with",DOP+"?"
    milkshake = raw_input("Yes or no? ")
    if milkshake[0].lower() == 'y':
        print "\nUh oh. You should have forseen this, but in your excitement to get"
        print "a milkshake, you forgot the inevitable result of obtaining one. The"
        print "boys have all come to your yard! And by yard I mean extremely small"
        print "dorm room! You manage to herd them out, but as the clock strikes 2am,"
        print "you realize that there is one remaining member of the opposite gender"
        print "in your room! The RAs are patrolling, but your guest wants to get to"
        print "bed. Looks like you're gonna have to facilitate a PARIETALS BREAK!!!\n"
    else:
        print "\nYou're lame. You don't get to play Parietals Break. Never speak to"
        print "me again."
        sys.exit(0)

if SUBPRN=='he':
    print "\nYou literally just walk the girl downstairs. She high-fives you rector"
    print "on the way out. Congrats, you win Parietals Break and the gender lottery."
    print "Have fun making more money than me for the rest of your life."
    sys.exit(0)

print "All right, it's time to get this boy to freedom. You've got to make"
print "a run for the staircases. Your room is right in the middle, do you"
print "want to go for the main staircase or the side staircase?"
print "\t1. Main staircase"
print "\t2. Side staircase"
answer = raw_input("Choice: ")
if answer=='1':
    print "\nYou hear someone in the e-lounge. Do you want to stay on this path?"
    print "or go to the other staircase?"
    print "\t1. Keep going"
    print "\t2. Turn back"
    staircase = raw_input("Choice: ")
    if staircase=='2':
        answer = '2'
else:
    print "\nYou hear an RA coming. Do you want to stay on this path?"
    print "or go to the other staircase?"
    print "\t1. Keep going"
    print "\t2. Turn back"
    staircase = raw_input("Choice: ")
    if staircase=='2':
        answer = '1'

if answer=='1':
    print "\nSo there's someone in the e-lounge. Do you go to the staircase or"
    print "wait them out?"
    print "\t1. Go to staircase"
    print "\t2. Wait them out"
    staircase = raw_input("Choice: ")
    if staircase=='1':
        print "\nThe person in the e-lounge is an RA!\n"
        if hallstaff > 0:
            print "Luckily, you befriended her this morning when you opened her"
            print "door for her, so she's willing to look the other way. You make"
            print "it down one floor."
        else:
            print "She reports you to the Rector and you and your male friend get"
            print "in lots of trouble...\n\n"
            print "GAME OVER"
            sys.exit(0)
    else:
        print "You're so distracted listening for the person in the e-lounge"
        print "that you don't even notice your Rector coming up behind you!"
        if numCheeses>2:
            print "Luckily, you are able to distract her with some of her favorite"
            print "food: CHEESE. You've picked up more than two slices today, just"
            print "enough to distract her as the two of you slip away! You make it"
            print "to the staircase and down one floor."
        else:
            print "She is not happy to see you breaking parietals, and you and your"
            print "male friend get in lots of trouble...\n\n"
            print "GAME OVER"
            sys.exit(0)
else:
    print "\nSo you hear an RA coming. Do you run for the staircase or ask your"
    print "friend to hide you?"
    print "\t1. Run for staircase"
    print "\t2. Ask friend to hide you"
    staircase = raw_input("Choice: ")
    if staircase=='2':
        if friendship > 0:
            print "\nLuckily, you have a pretty strong friendship, and you duck into"
            print "Your friend's room just in time. You wait for the RA to pass, then"
            print "run for the staircase and make it down one floor."
        else:
            print "\nUh oh, you're friend is being petty today and doesn't let you in!"
            print "Your RA sees you, and she reports you to the Rector"
            print "and you and your male friend get in lots of trouble...\n\n"
            print "GAME OVER"
            sys.exit(0)
    else:
        print "\nYour RA sees you immediately. What did you expect to happen??"
        print "She sees you, and she reports you to the Rector and you and"
        print "your male friend get in lots of trouble...\n\n"
        print "GAME OVER"
        sys.exit(0)
print "\n\nAt this point in the game there will be a minigame... effort..."
print "\n\nYou just need to get down one more staircase, but the main one is"
print "blocked. Do you want to face the NORTH-FACING or WEST-FACING staircase?"
print "\t1. NORTH staircase"
print "\t2. WEST staircase"
answer = raw_input("Choice: ")
if answer=='2':
    print "\nUh oh, the WEST staircase is under construction! You try to run"
    print "to the NORTH staircase, but you run into your Rector."
    if numCheese == 3:
        print "\nLuckily, you have so much cheese on your person, that you are"
        print "able to convince her to look the other way. You and your male"
        print "friend ESCAPE.\n\n"
        print "CONGRATULATIONS, YOU HAVE SUCCESSFULLY BROKEN PARIETALS\n\n\n"
        sys.exit(0)
    elif distraction > 0 and stamina > 0:
        print "\nLucky for you, the girl from your section that you waved at"
        print "comes out of nowhere and distracts your rector for a few seconds."
        print "Thanks to your run earlier, your legs are energized enough to make"
        print "a mad dash for the other staircase. You make it in the nick of"
        print "time, and you and your male friend ESCAPE.\n\n"
        print "CONGRATULATIONS, YOU HAVE SUCCESSFULLY BROKEN PARIETALS\n\n\n"
        sys.exit(0)
    else:
        print "She is not happy to see you breaking parietals, and you and your"
        print "male friend get in lots of trouble...\n\n"
        print "GAME OVER"
        sys.exit(0)
else:
    print "\nYou and your male friend manage to slip out the NORTH door into"
    print "the dead of night. You share a firm handshake and go your separate"
    print "ways...\n\n"
    print "CONGRATULATIONS, YOU HAVE SUCCESSFULLY BROKEN PARIETALS\n\n\n"
    sys.exit(0)
