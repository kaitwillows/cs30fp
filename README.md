# untitled shooter game (prototype???)
> an "enter the gungeon" like shooter game in pygame

i made this as a final project for grade 12 computer science. currently, it allows you to play a 1v1 match against an ai opponent. your only goal is to kill it before it kills you.

it's similar to enter the gungeon, as when you move the mouse, your screen pans to frame more of what you're aiming at, like so,

[gameplay gif](./readme%20assets/gameplay.gif)

go to [setup](#setup) to setup the game and play, or go to [tour of the game](#tour-of-the-game) to learn more about it

# setup
to play this game, you'll need to download the source code, install python and install pygame.

## download the game
you can download the release version from the [releases](https://github.com/kaitwillows/cs30fp/releases) page in this repository. be sure to download the `untitled-shoot-game` zip file and extract it

alternatively, download the source code from [this repository](https://github.com/kaitwillows/cs30fp), click on the green `<> Code` button at the top, then click `Download ZIP` to download the source code. extract the zip file to somewhere on your computer.

## install python
if you haven't allready, you're going to need to download the python programming language from [python.org](https://www.python.org/downloads/). navigate to the download section and install the latest version

## install pygame
if you have python, you can install pygame by running `pip install pygame` in a terminal window. 

## run the game
you can run the game by double clicking the `run.bat` file. (this works on windows and it *should* also work on macos)

alternatively, you can open a terminal window, and navigate it to the directory where the source code is stored, then enter `python main.py` to run the game


# tour of the game

## menu
![text-based menu options](./readme%20assets/menu.png)

look at how charming it is! (i promise the game looks cooler than this)

the menu is pretty basic, but it gives you a couple of options:
- play game - this is where the magic happens
- set screen resolution - setting this to your monitors resolution will let the game run in fullscreen. this preference is stored in `scores.json`
- reset scores - also stored in `scores.json`, the number of times you've won and lost is shown at the top. you can reset these scores if you ever feel ashamed of them.
- quit game - i don't know why you would ever want to leave, but the option is there reguardless

## game window
![game window](./readme%20assets/game%20window.png)

(maybe its not that cool, but i promise the game is slightly more fun than it looks)

either way, theres a couple important things going on here:
- you
    - the kind of hard to see green text that says `you` is you believe it or not.
    - you have one hit point, and will die if you get shot. spend it wisely.
- bad guy (`bad g` in this case)
    - this isn't a mistake, each letter in `bad guy` counts as one hit point. so each time you shoot the bad guy, it will lose one of its letters, until its hp hits 0
    - the bad guy has some ai that will hunt and track you down until you're dead, so watch out.
- your crosshair
    - just below the bad guy, you'll see your crosshair. it will show you where your aiming, and moving it will also show you more of what you're aiming at (just play the game and you'll see what i mean.)
- walls
    - the black stuff on the map represent walls, you cannot shoot nor move through these. try to use them to your advantage.
- minimap
    - the minimap provides a better overview of the environment around you for when you get lost.
    - two tiny litle pixels (one green and one red) represent your location on the map, and the enemy's.


# code overview (technical details)
*i mean like, you could also look at the code itself to get a sense of what it does*

## main.py
- displays the main menu
- runs `game_loop.py` as a subprocess when the user selects `start game`
    - running as a subprocess allows the exit codes to be used (whether the game was won/lost/exited) 
    - it also allows the game to be re-run at the users request
- uses the `json` library to read and write variables (scores, and screen resolution) to `scores.json`
- uses `try` blocks to handle invalid user inputs

## game_loop.py
- initializes pygame, as well as every game object from `game_objects.py`
- runs the game loop for each frame

## game_objects.py
classes:
- `Screen`
- `Camera`
- `Map`
- `MiniMap`
- `Mouse`
- `Player`
- `Gun`
- `Bullet`
- enemy versions of `player`, `gun`, and `bullet` also exist
