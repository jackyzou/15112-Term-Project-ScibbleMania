# Scribble Mania: drawing game based on PyGame modules.

###Why I adopted pygame###
Pygame is a cross-platfrom library designed to make it easy to write multimedia software, such as games, in Python. Pygame requires the Python language and SDL multimedia library. It can also make use of several other popular libraries.

## Step by Step Guide

0. Installing the required module PyGame:
	1. Open Terminal on your computer (MacOX)
	2. pip install pygame (note: pip3 install pygame, if installing in python3 directory)
	3. Installing from source is fairly automated. The most work will involve compiling and installing all the pygame dependencies. Once that is done run the "setup.py" script which will attempt to auto-configure, build, and install pygame.
	4. If you have further concerns, go to http://www.pygame.org and http://www.pygame.org/download.shtml for detailed instructions.

1.  Open your IDE, I used Sublime Text 2

2.  Click `File > New Window` or hit `Ctrl + N`

3.  Import the `pygame`, `sys`, `os` and `time` modules and be sure it's properly installed

    ```python
    import pygame
    from pygame.locals import *
    import sys, os
    import time
    ```
4. Run the ScribbleMania.py file to start the game

5. During the game, files, for example, screenshots and play data will be stored in the folder called: "/completeScreenshots"

6. All the supporting images and background music used in the program are stored in the folder called "/image"

Hope you have fun playing this game!