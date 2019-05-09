# Parietals Break

Literally the best game you will ever play. Parietals Break is a story line, text-based game created on Pygame based on the entirely fictional university named Dotre Name. It's a half-mandatory-project, half-jab-at-sexist-double-standards-at-a-totally-fictional-school-that-isn't-in-Indiana. Have fun!

# Installation
To play, download the .zip and extract the contents or clone the repository with the link
```
https://github.com/agervase/parietalsbreak.git
```
The necessary files to download for gameplay are `parietalsbreak.py` and the `girlpictures/` and `boypictures` directories.  

The game requires Pygame installed locally which, if you do not already have, can be downloaded at:
```
https://www.pygame.org/wiki/GettingStarted
```
or through terminal with
```
pip install Pygame
```

# How to Play

Parietals Break is a mouse-based game. Click the options to make the best decisions to try to get your boy (or girl) to freedom or risk getting a stern talking to at the Office of Community Standards. 

# Developers
## Dependencies

Main Gameplay:
Python 3
Pygame 1.9.6
```
pip install Pygame
```

## Game Functions
```
displayImg(img, x, y)
```
Displays image given the image and the dimensions.

```
drawPrompt(prompt)
```
Displays the question to the player given the string prompt containing the question.

```
drawScene(person1, person2, background)
```
Draws the scene on screen given the image paths for person1, person2, and background.
Dependent on displayImg().

```
drawChoices(numchoices, name, choice1, choice2, choice3, choice4)
```
Displays the choices on screen given the number of choices, name of the character, and the string for each choice.

```
getChoice(numchoices, m, n)
```
Gets the user's choice given the number of choices and the coordinates of the user's mouse when it clicks.

```
rot_center(image, angle)
```
Rotates an image while maintaining the position

```
makedict(gender)
```
Given the gender the user chooses to play as, return a dictionary of all images used for that gender

# Other Fun Stuff

We made this game in about 40 hours. If there's stuff broken, hmu. Also, feel free to use this to up your Pygame/Python game. 
Verilog is a hardware description language.   

Love,  

Silvia Camara [@silvercam15](https://github.com/silvercam15)
      &
Abby Gervase [@agervase](https://github.com/agervase)



