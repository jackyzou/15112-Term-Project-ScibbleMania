import sys, pygame
from pygame.locals import *
import os, math, random

#This is the intro screen
class splashScreen:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Scribble Mania!') #Title
        
        #bg music
        self.musicOn = True
        if(self.musicOn == True):
            pygame.mixer.music.load('image/bgmusic.mp3')
            pygame.mixer.music.play(-1)

        #program color panel
        self.BLACK = 0,0,0
        self.WHITE = 255,255,255
        self.RED = (200,0,0)
        self.light_red = (255,0,0)
        self.YELLOW = (200,200,0)
        self.light_yellow = (255,255,0)
        self.GREEN = (34,177,76)
        self.light_green = (22,222,105)
        self.BLUE = (67,94,132)
        self.light_blue = (114,203,255)

        #program font panel
        self.font = pygame.font.SysFont("Impact", 20)
        self.smallfont = pygame.font.SysFont("Impact", 25)
        self.medfont = pygame.font.SysFont("Impact", 50)
        self.largefont = pygame.font.SysFont("Impact", 85)

        #program mouse control panel
        self.QUIT = False
        self.mousebutton = None
        self.mousedown = False
        self.mouse_buttons = ["Left Button","Middle Button","Right Button","Wheel Up","Wheel Down"]

        #clock declaration
        self.clock = pygame.time.Clock()

        #initialize system
        self.initialize()

       
    def initialize(self):

        #Setup the pygame screen
        self.screen_width = 1300
        self.screen_height = 700
        self.screen_size = (self.screen_width, self.screen_height)    
        self.screen = pygame.display.set_mode(self.screen_size)
        
        #setup a generic drawing surface/canvas
        self.canvas = pygame.Surface((self.screen_width, self.screen_height))
        
        #load all the images
        self.bg = pygame.image.load("image/parallaxbg.jpg")
        self.playIcon = pygame.image.load("image/playbutton.png")
        self.vsIcon = pygame.image.load("image/draw.png")
        self.settingIcon = pygame.image.load("image/settingButton.png")
        self.downloadIcon = pygame.image.load("image/DLbutton.png")
        self.titleIcon = pygame.image.load("image/title.png")
        self.quitIcon = pygame.image.load("image/exit.png")
        self.backIcon = pygame.image.load("image/back.png")
        self.levelSelect = pygame.image.load("image/levelSelect.png")
        self.level123 = pygame.image.load("image/levels123.png")
        self.timeIcon = pygame.image.load("image/time.png")
        self.shapeIcon = pygame.image.load("image/shapes.png")
        self.leftMouse = pygame.image.load("image/leftmouse.png")
        self.wheelMouse = pygame.image.load("image/wheelmouse.png")
        self.mute = pygame.image.load("image/mute.png")


        #create Buttons 
        self.play_button = pygame.transform.scale(self.playIcon, (180,180))
        self.vs_button = pygame.transform.scale(self.vsIcon, (215, 215))
        self.setting_button = pygame.transform.scale(self.settingIcon, (80, 80))
        self.download_button = pygame.transform.scale(self.downloadIcon, (80, 80))
        self.quit_button = pygame.transform.scale(self.quitIcon,(80,80))
        self.back_button = pygame.transform.scale(self.backIcon,(80,80))




        
    
    #mouse handler takes care of all the mouse events 
    def mouse_handler(self,event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mousedown = True
            self.mousebutton = event.button  
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mousedown = False
            self.mousebutton = event.button

        self.mouseX, self.mouseY = pygame.mouse.get_pos()
 
        self.show_mousestate()

    #shows the position of the mouse and it's press state
    def show_mousestate(self):
        """Show the mouse position and button press on the screen"""
        if self.mousebutton and self.mousedown:
            info = "Mouse: "+str(self.mouse_buttons[self.mousebutton-1])
        else:
            info = "Mouse: "
        info += "X= "+str(self.mouseX)+" Y: "+str(self.mouseY)

        #NB: for now we clear the canvas with black
        self.canvas.fill(self.BLACK)

        #load font and blit to canvas
        font = pygame.font.Font(None, 20)        
        textimg = font.render(info, 1, self.WHITE)
        self.canvas.blit(textimg, (10, 10))

    # draw general stuff the doesn't need to repaint 
    def draw(self):
        """We use a generic surface / Canvas onto which we draw anything
           Then we blit this canvas onto the display screen"""
        self.screen.blit(self.bg, (0, 0))

        #buttons are here
        self.button("play", 490,590,100,100, self.GREEN, self.light_green, action="play")
        self.button("drawSandbox", 818,588,103,103, self.YELLOW, self.light_yellow, action="drawSandbox")
        self.button("s", 65,560,45,45, self.YELLOW, self.light_yellow, action="setting")
        self.button("d", 65,460,45,45, self.YELLOW, self.light_yellow, action="download")
        self.button("quit", 1240,540,45,45, self.RED, self.light_red, action ="quit")

        
        #display on the screen
        self.screen.blit(self.play_button, (400, 500))
        self.screen.blit(self.vs_button, (710, 480))
        self.screen.blit(self.setting_button, (25, 520))
        self.screen.blit(self.download_button, (25, 420))
        self.screen.blit(self.titleIcon, (120,-80))
        self.screen.blit(self.quit_button, (1200,500))
        
        
    #customized button class (the main splashscreen and levelSelect all share 
    # one button class to maximize code reuse)
    def button(self, text, x, y, width, height, inactive_color, active_color, action = None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #if the button is a level select button
        if(text == "level"):
            if(abs(cur[0]-(x + width/2) ) < width/2 and abs(cur[1]- (y + height /2 ) ) < height/2):
                #the button is now active when mouse hovers on it
                pygame.draw.rect(self.screen, active_color, (x,y,width,height))
                
                if click[0] == 1 and action != None:
                    if action == "quit":
                        pygame.quit()
                        quit()

                    if action == "level1":
                        level1 = gameMode(action)
                        level1.run()
                        print("This is level1")

                    if action == "level2":
                        level2 = gameMode(action)
                        level2.run()
                        print("This is level2")
                    
                    if action == "level3":
                        level3 = gameMode(action)
                        level3.run()
                        print("This is level3")
                
            else:
                # the button returns to the unselected state
                pygame.draw.rect(self.screen, inactive_color, (x,y,width,height))
        else:

            if(abs(cur[0]-x)<width and abs(cur[1]-y)<height):
                
                pygame.draw.circle(self.screen, active_color, (x,y), width)
                if click[0] == 1 and action != None:
                    if action == "quit":
                        pygame.quit()
                        quit()

                    if action == "drawSandbox":
                        drawSandbox = gameMode(action)
                        drawSandbox.run()
                        print("This is drawSandbox")

                    if action == "play":
                        self.level_select()
                        print("This is play")
                    
                    if action == "setting":
                        self.game_setting()
                        print("This setting")

                    if action == "download":
                        self.downloadScreen()
                        print("This is download")

                    if action == "backFromSetting":
                        print("This is back")
                        myWelcomScreen = splashScreen()
                        myWelcomScreen.run()
                    
                    if action == "mute":
                        pygame.mixer.music.stop()
                        self.musicOn = False
            else:
                # the button returns to the unselected state
                pygame.draw.circle(self.screen, inactive_color, (x,y), width)

    # helper function to format text objects 
    def text_objects(self, text, color,size = "small"):

        if size == "small":
            textSurface = self.smallfont.render(text, True, color)
        if size == "medium":
            textSurface = self.medfont.render(text, True, color)
        if size == "large":
            textSurface = self.largefont.render(text, True, color)

        return textSurface, textSurface.get_rect()

    # helper function to fomat button 
    def text_to_button(self, msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
        textSurf, textRect = self.text_objects(msg,color,size)
        textRect.center = (buttonx, buttony)
        self.screen.blit(textSurf, textRect)

    # helper function to format text
    def message_to_screen(self,msg,color, y_displace = 0, size = "small"):
        textSurf, textRect = self.text_objects(msg,color,size)
        textRect.center = (int(1300 / 2), int(700 / 2)+y_displace)
        self.screen.blit(textSurf, textRect)
    
    # this screen displays solved levels that are stored locally
    def downloadScreen(self):
        gcont = True
        dataList = []
        level1time = ""
        level1shape = ""
        level2time = ""
        level2shape = ""
        level3time = ""
        level3shape = ""
        while gcont:
            for event in pygame.event.get():
                    #print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
        
            with open("completeScreenshot/playData.txt") as f:
                dataList = f.readlines()
            
            for data in range(len(dataList)):
                if(dataList[data] == "level1\n"):
                    level1time = dataList[data+1].strip()
                    level1shape = str(dataList[data+2]).strip()

                if(dataList[data] == "level2\n"):
                    level2time = dataList[data+1].strip()
                    level2shape = str(dataList[data+2]).strip()

                if(dataList[data] == "level3\n"):   
                    level3time = dataList[data+1].strip()
                    level3shape = str(dataList[data+2]).strip()

            self.screen.blit(self.bg, (0,0))
            self.message_to_screen("See solved levels",(243,161,141),-275,size="large")
            self.screen.blit(self.levelSelect, (150,100))
            try:
                screenShot1 = pygame.image.load("completeScreenshot/level1.jpeg")
                screenShot2 = pygame.image.load("completeScreenshot/level2.jpeg")
                screenShot3 = pygame.image.load("completeScreenshot/level3.jpeg")
            except:
                print("No image")

 
            level1Text = self.medfont.render("Level 1",True, self.BLACK)
            level2Text = self.medfont.render("Level 2",True, self.BLACK)
            level3Text = self.medfont.render("Level 3",True, self.BLACK)
            winTime1Text = self.medfont.render(level1time, True, self.BLACK)
            winTime2Text = self.medfont.render(level2time, True, self.BLACK)
            winTime3Text = self.medfont.render(level3time, True, self.BLACK)
            shapeUsed1Text = self.medfont.render(str(level1shape), True, self.BLACK)
            shapeUsed2Text = self.medfont.render(str(level2shape), True, self.BLACK)
            shapeUsed3Text = self.medfont.render(str(level3shape), True, self.BLACK)
            
            self.screen.blit(level1Text, [330,250])
            self.screen.blit(level2Text, [570,250])
            self.screen.blit(level3Text, [800,250])
            self.screen.blit(winTime1Text, [330,480])
            self.screen.blit(winTime2Text, [570,480])
            self.screen.blit(winTime3Text, [800,480])
            self.screen.blit(shapeUsed1Text, [330,530])
            self.screen.blit(shapeUsed2Text, [570,530])
            self.screen.blit(shapeUsed3Text, [800,530])

            self.screen.blit(pygame.transform.scale(self.timeIcon, (50,50)), (430,480))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (50,50)), (430,530))
            self.screen.blit(pygame.transform.scale(self.timeIcon, (50,50)), (670,480))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (50,50)), (670,530))
            self.screen.blit(pygame.transform.scale(self.timeIcon, (50,50)), (910,480))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (50,50)), (910,530))

            self.screen.blit(pygame.transform.scale(screenShot1,(200,160)),[300,320])
            self.screen.blit(pygame.transform.scale(screenShot2,(200,160)),[530,320])
            self.screen.blit(pygame.transform.scale(screenShot3,(200,160)),[760,320])
            
            self.button("back", 65,650,46,46, self.BLUE, self.light_blue, action="backFromSetting")
            self.screen.blit(self.back_button, (25, 610))

            pygame.display.update()

    # this is the screen that shows user how to play the game 
    def game_setting(self):
        gcont = True

        while gcont:
            for event in pygame.event.get():
                    #print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()


            self.screen.blit(self.bg, (0,0))
            self.message_to_screen("Controls",self.GREEN,-300,size="large")
            self.message_to_screen("Drag mouse to draw curves",self.BLACK,-170,size= "small")
            self.message_to_screen("Click or wheel mouse to create particles",self.BLACK,-120,size="small")
            self.message_to_screen("Draw Anything on Canvas to Finish the Task",self.BLACK,-40,size= "medium")
            self.message_to_screen("Goal 1: Find a solution using less time",self.BLACK,40)
            self.message_to_screen("Goal 2: Find a solution using less shapes",self.BLACK,150)
            self.message_to_screen("                    →  - ∞",self.BLACK,90,size= "medium")
            self.message_to_screen("                    →  - ∞",self.BLACK,200,size= "medium")

            self.screen.blit(pygame.transform.scale(self.timeIcon, (50,50)), (610,420))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (50,50)), (610,530))
            self.screen.blit(pygame.transform.scale(self.leftMouse, (100,100)),(300,150))
            self.screen.blit(pygame.transform.scale(self.wheelMouse, (100,100)),(900,150))
            
            
            self.button("back", 65,650,46,46, self.BLUE, self.light_blue, action="backFromSetting")
            self.button("", 1250,650,46,46, self.BLUE, self.light_blue, action="mute")
            self.screen.blit(self.back_button, (25, 610))
            self.screen.blit(pygame.transform.scale(self.mute,(60,60)),(1220,620))

            pygame.display.update()

            self.clock.tick(15)
    
    # this is the screen that allows user to select which level they want to play
    def level_select(self):

        gcont = True

        while gcont:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()


            self.screen.blit(self.bg, (0,0))
            self.message_to_screen("Choose Level",(243,161,141),-275,size="large")
            self.screen.blit(self.levelSelect, (150,100))

            self.button("level", 235,260,250,240,self.GREEN,self.light_green,action= "level1")
            self.button("level", 517,260,250,240,self.GREEN,self.light_green,action= "level2")
            self.button("level", 800,260,250,240,self.GREEN,self.light_green,action= "level3")
            self.screen.blit(self.level123, (240,265))
                        
            self.button("back", 75,588,46,46, self.BLUE, self.light_blue, action="backFromSetting")
            self.screen.blit(self.back_button, (35, 548))

            pygame.display.update()

            self.clock.tick(15)

    # This is the main run function of the splashscreen
    def run(self):
        """This method provides the main application loop.
           It continues to run until either the ESC key is pressed
           or the window is closed
        """
        while True:
            
            events = pygame.event.get()
            for e in events:
                #pass event onto mouse handler only if something happens
                self.mouse_handler(e)
                
                #Set quit state when window is closed
                if e.type == pygame.QUIT :
                    self.QUIT = True
                if e.type == KEYDOWN:
                    #Set quit state on Esc key press
                    if e.key == K_ESCAPE:
                        self.QUIT = True
                                    
            if self.QUIT:
                #Exit pygame gracefully
                pygame.quit()
                sys.exit(0)

            #Process any drawing that needs to be done
            self.draw()

            #flip the display
            pygame.display.flip()



# this is the gameMode class that creates the main gaming view
class gameMode:
    def __init__(self,level):
        pygame.init()
        pygame.display.set_caption(level)
        
        #fundamental varibles
        self.level = level
        self.isWin = False
        self.undoPressed = False
        self.hasDrawnConstraint = False

        #color panel
        self.BLACK = 0,0,0
        self.WHITE = 255,255,255
        self.RED = (200,0,0)
        self.light_red = (255,0,0)
        self.YELLOW = (200,200,0)
        self.light_yellow = (255,255,0)
        self.GREEN = (34,177,76)
        self.light_green = (0,255,0)
        self.BLUE = (67,94,132)
        self.light_blue = (114,203,255)
        self.GRAY = (127,127,127)
        self.light_gray = (200,200,200)

        # varibles crucial to drawing 
        self.draw_on = False
        self.last_pos = (0, 0)
        self.color = (255, 128, 0)
        self.radius = 10          #The brush size is defined here
        self.speed = 10
        self.gravity = 0.3
        self.linePosList = dict() #this is list of all shapes
        self.my_particles = []
        self.shapeKey = -2 

        #clock declaration
        self.clock = pygame.time.Clock()
        self.frame_count = 0
        self.frame_rate = 60
        self.start_time = 90
        self.total_seconds = 0

        #font panel for the class
        self.font = pygame.font.SysFont("Impact", 20)
        self.smallfont = pygame.font.SysFont("Impact", 25)
        self.medfont = pygame.font.SysFont("Impact", 50)
        self.largefont = pygame.font.SysFont("Impact", 85)

        #initialize the program
        self.initialize()


    # initializing files and variables
    def initialize(self):
        #Setup the pygame screen
        self.screen_width = 1300
        self.screen_height = 700
        self.screen_size = (self.screen_width, self.screen_height)    
        self.screen = pygame.display.set_mode(self.screen_size)

        #load all the images
        self.paperbg = pygame.image.load("image/paperbg.jpg")
        self.timeIcon = pygame.image.load("image/time.png")
        self.shapeIcon = pygame.image.load("image/shapes.png")
        self.restartIcon = pygame.image.load("image/restart.png")
        self.settingIcon = pygame.image.load("image/question.gif")
        self.undoIcon = pygame.image.load("image/undo.png")
        self.backIcon = pygame.image.load("image/back.png") 
        self.starIcon = pygame.image.load("image/star.png")
        self.bg = pygame.image.load("image/parallaxbg.jpg")
        self.levelSelect = pygame.image.load("image/levelSelect.png")
        self.next = pygame.image.load("image/next.png")
        self.leftMouse = pygame.image.load("image/leftmouse.png")
        self.wheelMouse = pygame.image.load("image/wheelmouse.png")

        #create Buttons 
        self.restart_Button = pygame.transform.scale(self.restartIcon, (80,80))
        self.setting_Button = pygame.transform.scale(self.settingIcon, (120, 120))
        self.undo_Button = pygame.transform.scale(self.undoIcon,(70,70))
        self.back_Button = pygame.transform.scale(self.backIcon,(80,80))
        self.next_Button = pygame.transform.scale(self.next, (83,83))
        
        #setup a generic drawing surface/canvas
        self.canvas = pygame.Surface((self.screen_width, self.screen_height))

        self.draw()


    # customized button class
    def button(self, text, x, y, width, height, inactive_color, active_color, action = None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if(abs(cur[0]-x)<width and abs(cur[1]-y)<height):
            #this is when mouse is hover over the button
            pygame.draw.circle(self.screen, active_color, (x,y), width)
            
            if click[0] == 1 and action != None:
                if action == "quit":
                    pygame.quit()
                    quit()

                if action == "restart":
                    level = self.level
                    mygame = gameMode(level)
                    mygame.shapeKey += 2
                    mygame.run()

                    print("this is restart")

                if action == "undo":
                    self.undoPressed = True
                    print("This is undo")
                
                if action == "settingFromGame":
                    self.game_setting()
                    print("This setting")

                if action == "levelSelect":
                    myWelcomScreen = splashScreen()
                    myWelcomScreen.level_select()

                if action == "nextLevel":
                    currentLevel = self.level
                    nextLevel = str(currentLevel[:5]+str(int(currentLevel[-1])+1))
                    mygame = gameMode(nextLevel)
                    mygame.run()

                if action == "backFromSetting":

                    self.initialize()
                    self.run()                    
                    

                if action == "backToLevelSelect":
                    print("This is back")
                    myWelcomScreen = splashScreen()
                    myWelcomScreen.level_select()

        else:
            #mouse is not hovering over the button
            pygame.draw.circle(self.screen, inactive_color, (x,y), width)


    #game control screen to tell user how to play
    def game_setting(self):
        gcont = True
        while gcont:
            for event in pygame.event.get():
                    #print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            self.screen.blit(self.bg, (0,0))
            self.message_to_screen("Controls",self.GREEN,-300,size="large")
            self.message_to_screen("Drag mouse to draw curves",self.BLACK,-170,size= "small")
            self.message_to_screen("Click or wheel mouse to create particles",self.BLACK,-120,size="small")
            self.message_to_screen("Draw Anything on Canvas to Finish the Task",self.BLACK,-40,size= "medium")
            self.message_to_screen("Goal 1: Find a solution using less time",self.BLACK,40)
            self.message_to_screen("Goal 2: Find a solution using less shapes",self.BLACK,150)
            self.message_to_screen("                    →  - ∞",self.BLACK,90,size= "medium")
            self.message_to_screen("                    →  - ∞",self.BLACK,200,size= "medium")

            self.screen.blit(pygame.transform.scale(self.timeIcon, (50,50)), (610,420))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (50,50)), (610,530))
            self.screen.blit(pygame.transform.scale(self.leftMouse, (100,100)),(300,150))
            self.screen.blit(pygame.transform.scale(self.wheelMouse, (100,100)),(900,150))
            self.screen.blit(pygame.transform.scale(self.timeIcon, (50,50)), (610,420))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (50,50)), (610,530))
            
            self.button("back", 65,650,46,46, self.BLUE, self.light_blue, action="backFromSetting")
            self.screen.blit(self.back_Button, (25, 610))

            pygame.display.update()  


    # this screen shows up if the user has completed a level
    def levelCompleteScreen(self):
        gcont  = True
        
        while gcont:
            for event in pygame.event.get():
                    #print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            self.screen.blit(self.bg, (0,0))
            self.message_to_screen("Level Complete", self.GREEN,-275,size="large")
            self.screen.blit(self.levelSelect, (150,100))
            
            levelText1 = self.font.render(str("LV"+self.level[5:]),True, self.GRAY)
            levelText2 = self.medfont.render(str(self.level),True, self.BLACK)
            winTimeText = self.medfont.render(str("%s''"%self.winTime), True, self.BLACK)
            shapeUsedText = self.medfont.render(str(self.shapeUsed), True, self.BLACK)

            screenShot = pygame.image.load("completeScreenshot/%s.jpeg"%str(self.level))

            self.screen.blit(levelText1, [270,240])
            self.screen.blit(levelText2, [225,350])
            self.screen.blit(winTimeText, [395,350])
            self.screen.blit(shapeUsedText, [535,350])
            self.screen.blit(pygame.transform.scale(screenShot,(400,400)),[650,210])
            
            self.button("restart", 285,550,46,46, self.BLUE, self.light_blue, action="backToLevelSelect")
            self.button("level", 415,550,46,46, self.BLUE, self.light_blue, action="restart")
            self.button("next", 545,550,46,46, self.BLUE, self.light_blue, action="nextLevel")

            self.screen.blit(self.starIcon, (230,200))
            self.screen.blit(pygame.transform.scale(self.timeIcon, (80,80)), (365,210))
            self.screen.blit(pygame.transform.scale(self.shapeIcon, (80,80)), (520,210))
            
            self.screen.blit(self.back_Button, (245, 510))
            self.screen.blit(self.restart_Button, (375,510))
            self.screen.blit(self.next_Button, (503,508))

            pygame.display.update()  


    # formating text objects for the class
    def text_objects(self, text, color,size = "small"):

        if size == "small":
            textSurface = self.smallfont.render(text, True, color)
        if size == "medium":
            textSurface = self.medfont.render(text, True, color)
        if size == "large":
            textSurface = self.largefont.render(text, True, color)

        return textSurface, textSurface.get_rect()
    
    # displaying formatted text to screen
    def message_to_screen(self,msg,color, y_displace = 0, size = "small"):
        textSurf, textRect = self.text_objects(msg,color,size)
        textRect.center = (int(1300 / 2), int(700 / 2)+y_displace)
        self.screen.blit(textSurf, textRect)
    
    # draw the general back ground and buttons that doesn't need to repaint a lot 
    def draw(self):

        #self.screen.blit(self.paperbg, (160,75))
        self.screen.fill(self.BLACK)
        #buttons are here
        self.button("restart", 75,460,45,45, self.GRAY, self.light_gray, action="restart")
        self.button("back", 75,588,45,45, self.YELLOW, self.light_yellow, action="backToLevelSelect")
        
        self.button("setting", 1250,460,45,45, self.YELLOW, self.light_yellow, action="settingFromGame")
        self.button("undo", 1250,588,45,45, (40,40,40), (80,80,80), action="undo")


        self.screen.blit(self.restart_Button, (35, 420))
        self.screen.blit(self.back_Button, (35, 548))
        self.screen.blit(self.setting_Button, (1190, 400))
        self.screen.blit(self.undo_Button, (1210, 548))


        self.screen.blit(self.starIcon, (20,25))
        self.screen.blit(self.timeIcon, (45,135))
        self.screen.blit(self.shapeIcon, (47,260))


        #Timer counter on the screen 
        self.total_seconds = self.frame_count // self.frame_rate
        minutes = self.total_seconds // 60
        seconds = self.total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        text = self.font.render(output_string, True, self.WHITE)
        self.screen.blit(text, [27, 190])

        self.total_seconds = self.start_time - (self.frame_count // self.frame_rate)
        if self.total_seconds < 0:
            self.total_seconds = 0
        # Divide by 60 to get total minutes
        minutes = self.total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = self.total_seconds % 60
     
        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
     
        # Blit to the screen
        clockText = self.font.render(output_string, True, self.WHITE) #this is the clock text

        #this is the amount of shapes
        shapeText = pygame.font.SysFont("Impact", 30).render(str(self.shapeKey), True, self.WHITE) 
     
        if(self.level == "drawSandbox"):
            levelText = self.medfont.render("∞",True, self.WHITE)
            self.screen.blit(levelText, [52,45])

        else:
            levelText = self.font.render(str("LV"+self.level[5:]),True, self.WHITE)
            self.screen.blit(levelText, [58,65])
            self.screen.blit(clockText, [20, 222])


        self.screen.blit(shapeText, [60,320])
     
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        self.frame_count += 1
     
        # Limit frames per second
        self.clock.tick(self.frame_rate)

    # this is a main algorithm for creating a smooth curve out of circles 
    def roundline(self,srf, color, start, end, radius=1):
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = int(max(abs(dx), abs(dy)))
        for i in range(distance):
            x = int(start[0]+float(i)/distance*dx)
            y = int(start[1]+float(i)/distance*dy)
            pygame.draw.circle(srf, color, (x, y), radius)

    # draws the shape with give shape keys and dictionary
    def drawCurveWithDict (self, screen, color, lineList, radius):
        for coord in range(0,len(lineList),4):
            self.roundline( screen, color, [lineList[coord],lineList[coord+1]], 
                                [lineList[coord+2],lineList[coord+3]], radius)


    # This is the main run function of the gameMode: most important driver of the game
    def run(self):
        """This method provides the main application loop."""

        #create a physics enviornment
        env = Environment(1195,675)
        try:
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:  
                        raise StopIteration
                    
                    #drawing area boundry [(171, 109), (1183, 112), (168, 661), (1182, 661)]                    
                    # if (e.pos[0]> 170 and e.pos[0] < 1180) and (e.pos[1] > 110 and e.pos[1] < 660):
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        if (e.pos[0]> 150 and e.pos[0] < 1195) and (e.pos[1] > 50 and e.pos[1] < 675):
                            pygame.draw.circle(self.screen, color, e.pos, self.radius)
                            self.linePosList[self.shapeKey] = list(e.pos)
                            selected_particle = env.findParticle(e.pos[0], e.pos[1])
                            draw_on = True
                        else:
                            draw_on = False
                    if e.type == pygame.MOUSEBUTTONUP:#finished drawing one shape
                        selected_particle = None
                        if (e.pos[0]> 150 and e.pos[0] < 1195) and (e.pos[1] > 50 and e.pos[1] < 675):
                            if(len(self.linePosList)!=0):
                                if(len(self.linePosList[self.shapeKey])==2): #when it's a dot
                                    #create a particle object here
                                    #addParticles(self, x, y, size, color):
                                    env.addParticles(self.linePosList[self.shapeKey][0],
                                        self.linePosList[self.shapeKey][1], self.radius, color)
                                    selected_particle = None
                                    running = True

                                elif(len(self.linePosList[self.shapeKey])>2): #when it's a shape
                                    #create a curve object here
                                    #addCurves(self, listOfParticles, size, color)
                                    env.addCurves(self.linePosList[self.shapeKey],self.radius, color)
                                    selected_particle = None
                                    running = True
                                
                            self.shapeKey += 1
                        draw_on = False
                        print(self.linePosList) #checking if all the shapes are stored properly
                        
                        if(self.undoPressed == True):
                            if(len(self.linePosList)!=0):
                                if(len(self.linePosList[self.shapeKey-1])==2): #when it's a dot
                                    if(self.shapeKey > 0):
                                        self.shapeKey -= 1
                                        env.particles.pop()
                                        self.undoPressed = False
                                else:
                                    if(self.shapeKey > 0):
                                        self.shapeKey -= 1
                                        env.curves.pop()
                                        self.undoPressed = False
                            else:
                                pass

                    if e.type == pygame.MOUSEMOTION:
                        if draw_on:
                            if (e.pos[0]> 150 and e.pos[0] < 1195) and (e.pos[1] > 50 and e.pos[1] < 675):
                                self.linePosList[self.shapeKey] += list(e.pos)
                                pygame.draw.circle(self.screen, color, e.pos, self.radius)
                                self.roundline(self.screen, color, e.pos, last_pos, self.radius)
                        last_pos = e.pos

                if selected_particle:
                    draw_on = False
                    selected_particle.mouseMove(e.pos[0], e.pos[1])
                self.draw()
                env.update()
                #self.screen.blit(self.paperbg, (160,75))



                ####Quadtree Created Here#####

                tree = Quadtree(0, pygame.Rect(150,50,1050,630), env.particles)#creates trunk of quadtree
                
                tree.update(self.screen)#updates trunk and begins recursive process for collision testing
                
                #self.screen.fill(env.colour)

                for p in env.particles:
                    pygame.draw.circle(self.screen, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)
                    #self.clock.tick(5)
                
                for c in env.curves:
                    for i in range(1,len(c.x)):
                        self.roundline(self.screen, c.colour, (c.x[i],c.y[i]),(c.x[i-1],c.y[i-1]), self.radius)
                
                if self.level == "drawSandbox":
                    myfont = pygame.font.SysFont("Impact", 75)
                    label = myfont.render("SandBox Mode: Draw anything!", 1, (255,255,255))
                    self.screen.blit(label, (200, -1))

                if self.level == "level1":
                    myfont = pygame.font.SysFont("Impact", 75)
                    label = myfont.render("Draw a Shape!", 1, (255,255,255))
                    self.screen.blit(label, (480, -1))

                if self.level == "level2":
                    myfont = pygame.font.SysFont("Impact", 55)
                    label = myfont.render("Make the ball hit the right wall!", 1, (255,255,255))
                    self.screen.blit(label, (300, -1))

                if self.level == "level3":
                    myfont = pygame.font.SysFont("Impact", 55)
                    label = myfont.render("Fill the cup with particles!", 1, (255,255,255))
                    self.screen.blit(label, (350, -1))

                if(self.level == "level1"):
                    # here's definition of winning level1
                    self.isWin = False
                    if(self.shapeKey != 0):
                        if(self.total_seconds<=0):
                            myfont = pygame.font.SysFont("Impact", 200)
                            label = myfont.render("Try Again :(", 1, (255,255,255))
                            self.screen.blit(label, (350, 250))
                        else:
                            if(env.touchedGround == True):
                                myfont = pygame.font.SysFont("Impact", 200)
                                label = myfont.render("Solved!!!", 1, (255,255,255))
                                self.screen.blit(label, (350, 250))
                                pygame.draw.line(self.screen, self.RED, (150, 675), (1195, 675),5)
                                self.isWin = True
                                self.winTime = 90 - self.total_seconds
                                self.shapeUsed = self.shapeKey
                                pygame.image.save(self.screen, "completeScreenshot/level1.jpeg")
                                #print(winTime,shapeUsed)
                                #break

                if(self.level == "level2"):
                    # here's definition of winning level2
                    self.isWin = False
                    
                    if(self.total_seconds<=0):
                        myfont = pygame.font.SysFont("Impact", 200)
                        label = myfont.render("Try Again :(", 1, (255,255,255))
                        self.screen.blit(label, (350, 250))
                    else:
                        if(env.touchedRightWall == True):
                            myfont = pygame.font.SysFont("Impact", 200)
                            label = myfont.render("Solved!!!", 1, (255,255,255))
                            self.screen.blit(label, (350, 250))
                            pygame.draw.line(self.screen, self.RED, (1195, 50), (1195, 675),5)
                            self.isWin = True
                            self.winTime = 90 - self.total_seconds
                            self.shapeUsed = self.shapeKey
                            pygame.image.save(self.screen, "completeScreenshot/level2.jpeg")
                            #print(winTime,shapeUsed)
                            #pygame.time.wait(5000)
                            #break

                if(self.level == "level3"):
                    # here's definition of winning level3
                    self.isWin = False
                    cup =  [540, 425, 540, 426, 540, 427, 540, 428, 540, 431, 540, 433, 542, 
                            436, 544, 444, 545, 450, 547, 455, 548, 461, 553, 474, 553, 479, 
                            555, 486, 561, 499, 563, 504, 565, 509, 568, 519, 571, 524, 577, 
                            535, 578, 540, 581, 545, 586, 557, 588, 562, 590, 567, 592, 571, 
                            595, 579, 596, 583, 598, 588, 600, 592, 602, 599, 604, 603, 604, 
                            607, 607, 615, 608, 619, 610, 623, 612, 626, 613, 633, 614, 638, 
                            615, 640, 616, 641, 617, 644, 617, 645, 618, 647, 619, 650, 620, 
                            653, 620, 655, 621, 656, 623, 660, 624, 661, 625, 663, 626, 664, 
                            626, 665, 627, 667, 627, 668, 627, 669, 628, 669, 629, 669, 633, 
                            669, 635, 669, 638, 669, 648, 670, 654, 670, 659, 671, 669, 671, 
                            674, 671, 682, 671, 688, 671, 697, 671, 701, 671, 706, 671, 716, 
                            671, 723, 671, 731, 671, 743, 670, 750, 670, 754, 669, 759, 669, 
                            773, 668, 780, 667, 785, 666, 793, 666, 797, 666, 801, 666, 812, 
                            665, 816, 665, 819, 665, 828, 664, 831, 664, 834, 664, 838, 664, 
                            845, 664, 848, 664, 849, 664, 851, 664, 853, 661, 855, 656, 858, 
                            649, 861, 643, 866, 631, 869, 625, 871, 619, 875, 608, 876, 603, 
                            878, 598, 881, 586, 883, 581, 885, 576, 888, 570, 891, 559, 892, 
                            555, 894, 550, 896, 546, 898, 537, 899, 533, 901, 529, 902, 524, 
                            905, 514, 906, 509, 907, 504, 909, 496, 910, 492, 910, 488, 911, 
                            483, 913, 477, 914, 474, 915, 472, 916, 466, 917, 464, 918, 461, 
                            918, 459, 919, 457, 919, 455, 920, 454, 920, 451, 921, 450, 921, 
                            449, 921, 447, 921, 446, 921, 445, 921, 444, 922, 444, 922, 443, 
                            922, 442, 922, 441, 923, 441]
                    env.constraints = cup
                    self.drawCurveWithDict(self.screen,self.WHITE,cup,self.radius)
                    if(self.hasDrawnConstraint == False):
                        env.addConstraints()
                        self.hasDrawnConstraint = True

                    if(self.total_seconds<=0):
                            myfont = pygame.font.SysFont("Impact", 200)
                            label = myfont.render("Try Again :(", 1, (255,255,255))
                            self.screen.blit(label, (350, 250))
                    else:
                        if(self.shapeKey >= random.randint(170,200)):
                            myfont = pygame.font.SysFont("Impact", 200)
                            label = myfont.render("Solved!!!", 1, (255,255,255))
                            self.screen.blit(label, (350, 250))
                            pygame.draw.line(self.screen, self.RED, (1195, 50), (1195, 675),5)
                            pygame.draw.line(self.screen, self.RED, (150, 50), (150, 675),5)
                            pygame.draw.line(self.screen, self.RED, (150, 50), (1195, 50),5)
                            pygame.draw.line(self.screen, self.RED, (1195, 50), (1195, 50),5)
                            self.isWin = True
                            self.winTime = 90 - self.total_seconds
                            self.shapeUsed = self.shapeKey
                            pygame.image.save(self.screen, "completeScreenshot/level3.jpeg")


                pygame.draw.line(self.screen, (108,108,108), (150, 675), (1195, 675),1)
                #pygame.draw.aaline(self.screen, self.GRAY, (150, 50), (1195, 50))
                pygame.draw.line(self.screen, (108,108,108), (150, 50), (150, 675),1)
                pygame.draw.line(self.screen, (108,108,108), (1195, 50), (1195, 675),1)    
                                  

                pygame.display.flip()
                if(self.isWin == True):
                    playData = open("completeScreenshot/playData.txt","a")
                    playData.write(str(self.level)+"\n")
                    playData.write("%s''"%str(self.winTime)+"\n")
                    playData.write(str(self.shapeUsed)+"\n"+"\n")
                    playData.close()

                    pygame.time.wait(2000)
                    self.levelCompleteScreen()




        except StopIteration:
            pass

#####################################################################################
########### Following is some math physics code for the enviornment class ###########
#####################################################################################

#mathematically adding two vectors 
def addVectors(angle1, length1, angle2, length2):
    """ Returns the sum of two vectors """
    
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle  = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

# effects when two particles collide
def collide(p1, p2):
    """ Tests whether two particles overlap
        If they do, make them bounce
        i.e. update their angle, speed and position """
    
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    
    if dist < p1.size + p2.size:

        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass, angle, 
                                                            2*p2.speed*p2.mass/total_mass)
        (p2.angle, p2.speed) = addVectors(p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass, 
                                            angle+math.pi, 2*p1.speed*p1.mass/total_mass)
        elasticity = p1.elasticity * p2.elasticity
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5*(p1.size + p2.size - dist+1)
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap


# effects when two curves collide
def collideCurve(c1 , c2):
    """ Tests whether two curves overlap
        If they do, make them bounce
        i.e. update their angle, speed and position """
    xShapeLength = max(len(c1.x),len(c2.x))
    yShapeLength = max(len(c1.y),len(c2.y))
    dx = [0.0] * xShapeLength
    dy = [0.0] * yShapeLength
    
    if(len(c1.x) > len(c2.x)):
        for i in range(len(c1.x)):
            if(i >= len(c2.x)):
                dx[i] = 0
            else:
                dx[i] = c1.x[i] - c2.x[i] #long and short crash
                
    elif(len(c1.x)< len(c2.x)):
        for i in range(len(c2.x)):
            if(i >= len(c1.x)):
                dx[i] = 0 
            else:
                dx[i] = c1.x[i] - c2.x[i] #short and long crash
                
    if(len(c1.y) > len(c2.y)):
        for i in range(len(c1.y)):
            if(i < len(c2.y)):
                dy[i] = c1.y[i] - c2.y[i]
            else:
                dy[i] =0

    elif(len(c1.y)< len(c2.y)):
        for i in range(len(c2.y)):
            if(i < len(c1.y)):
                dy[i] = c1.y[i] - c2.y[i]
            else:
                dy[i] = 0
    
    dist = [0.0] * len(dx)  
    
    for j in range(len(dx)):
        
        dist[j] = math.hypot(float(dx[j]), float(dy[j]))


# effects when a particle collide with a curve
def PcollideC(p,c):
    """ Tests whether a particle and a curve overlap
        If they do, make them bounce
        i.e. update their angle, speed and position """
    xShapeLength = len(c.x)
    yShapeLength = len(c.y)
    dx = [0.0] * xShapeLength
    dy = [0.0] * yShapeLength

    for i in range(xShapeLength):
        dx[i] = p.x - c.x[i] # x difference

    for j in range(yShapeLength):
        dy[j] = p.y - c.y[j] # y difference

    dist = [0.0] * xShapeLength

    for k in range(xShapeLength):
        dist[k] = math.hypot(float(dx[k]), float(dy[k])) # distance list

    for l in range(len(dist)):
        if(dist[l] < p.size + p.size):
            
            angle = math.atan2(dy[l], dx[l]) + 0.5 * math.pi 
            total_mass = p.mass + c.mass
            (p.angle, p.speed) = addVectors(p.angle, p.speed*(p.mass-c.mass)/total_mass, angle, 
                                                                    2*c.speed*c.mass/total_mass)
            
            elasticity = p.elasticity * c.elasticity
            p.speed *= elasticity
            

            overlap = 0.5*(p.size + p.size - dist[l]+1)
            p.x += math.sin(angle)*overlap
            p.y -= math.cos(angle)*overlap
            
            break


# Particle class defines the attributes for a particle
class Particle:
    """ A circular object with a velocity, size and mass """
    
    def __init__(self, x, y, size, mass=1):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.mass = mass
        self.drag = 1
        self.elasticity = 0.7

    # this is for the quadtree to display
    def get_rect(self):
        '''Returns quadtree rect object'''
        return self.rect

    #moving the particle
    def move(self):
        """ Update position based on speed, angle
            Update speed based on drag """

        (self.angle, self.speed) = addVectors(self.angle, self.speed, math.pi, 0.05)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= self.drag
        
    def mouseMove(self, x, y):
        """ Change angle and speed to move towards a given point """

        dx = x - self.x
        dy = y - self.y
        self.angle = 0.5*math.pi + math.atan2(dy, dx)
        self.speed = math.hypot(dx, dy) * 0.1

# Curve class defines the attributes for a curve
class Curve:
    """ A unregular shape defined by the user's brush with a velocity, size and mass """

    # remember Curve is basically a list of particles 
    def __init__(self, listOfParticles, size, mass = 2):
        self.x = []
        self.y = []
        for i in range(0,len(listOfParticles),2):
            self.x.append(listOfParticles[i])
        for j in range(1,len(listOfParticles),2):
            self.y.append(listOfParticles[j])
            
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 10
        self.speed = 0
        self.angle = 0
        self.mass = mass
        self.drag = 1
        self.elasticity = 0.75
        self.listOfParticles = listOfParticles

    def get_rect(self):
        '''Returns quadtree rect object'''
        return self.rect

    def move(self):
        """ Update position based on speed, angle
            Update speed based on drag """

        (self.angle, self.speed) = addVectors(self.angle, self.speed, math.pi, 0.05)

        for i in range(len(self.x)):
            self.x[i] += math.sin(self.angle) * self.speed
        for j in range(len(self.y)):
            self.y[j] -= math.cos(self.angle) * self.speed

        self.speed *= self.drag
        
    def mouseMove(self, x, y):
        """ Change angle and speed to move towards a given point """
        
        xShapeLength = max(len(c1.x),len(c2.x))
        yShapeLength = max(len(c1.y),len(c2.y))
        dx = [0.0] * xShapeLength
        dy = [0.0] * yShapeLength

        for i in range(len(self.x)):
            dx[i] = (x - self.x[i])
        
        for j in range(len(self.y)):
            dy[j] = (y - self.y[j])

        for k in range(len(dy)):
            self.angle = 0.5*math.pi + math.atan2(dy[k], dx[k])
            self.speed = math.hypot(dy[k], dx[k]) * 0.1


# here is how we define the physicall world 
class Environment:
    """ Defines the boundary of a simulation and its properties """
    
    def __init__(self, width, height):
        self.xoffset = 150
        self.yoffset = 50
        self.width = width
        self.height = height
        self.particles = []    #list of particles 
        self.curves = []       #lsit of curves
        self.constraints = []  #obstacles 
        
        self.colour = (255,255,255)
        self.mass_of_air = 0.2
        self.elasticity = 0.4
        self.acceleration = None

        #three fundamental boolean to see if a level is solved
        self.touchedGround = False
        self.touchedLeftWall = False
        self.touchedRightWall = False

        self.curveTouchedGround = False
        
    # adding a particle to the enviornment
    def addParticles(self, x, y, size, color):
        """ Add n particles with properties given by keyword arguments """
        #should be number of self.shapeKey * (size**2 * math.pi) / (1300*700)
        #mass = random.randint(100, 10000) 
        mass = 10000
        particle = Particle(x, y, size, mass)
        particle.speed = random.random()
        particle.angle = 0
        particle.colour = color
        particle.drag = (particle.mass/(particle.mass + self.mass_of_air)) ** particle.size

        self.particles.append(particle)
    
    # adding a curve to the enviornment
    def addCurves(self, listOfParticles, size, color):
        """ Add a curved unregular shape with properties given by the user's brush """
        mass = len(listOfParticles) * 10000

        curve = Curve(listOfParticles,size,mass)
        curve.speed = random.random()
        curve.angle = 0
        curve.colour = color
        curve.drag = (curve.mass/(curve.mass+ self.mass_of_air)) ** curve.size

        self.curves.append(curve)


    # rotating the shape
    def rotatePolygon(polygon,theta):
        """Rotates the given polygon which consists of corners represented as (x,y),
        around the ORIGIN, clock-wise, theta degrees"""
        theta = math.radians(theta)
        rotatedPolygon = []
        for corner in polygon :
            rotatedPolygon.append(( corner[0]*math.cos(theta)-corner[1]*math.sin(theta),
             corner[0]*math.sin(theta)+corner[1]*math.cos(theta)) )
        return rotatedPolygon

    def get_rect(self):
        '''Returns particle rect object'''
        return self.rect

    def set_rect(self,particle):
        '''Sets particle rect object at current coordinates with side length 2*radius'''
        particle.rect = pygame.Rect(particle.x - particle.size, particle.y - particle.size, particle.size*2, particle.size*2)

    def set_rect_curve(self,curve):

        curve.rect = pygame.Rect(curve.x[0] - curve.size, curve.y[0] - curve.size, len(curve.listOfParticles)*2 , len(curve.listOfParticles)*2)


    # updates the positions of each object in the environment
    def update(self):
        """  Moves particles and tests for collisions with the walls and each other """
        
        for i, particle in enumerate(self.particles):
            particle.move()
            if self.acceleration:
                particle.accelerate(self.acceleration)
            self.bounce(particle)

            for particle2 in self.particles[i+1:]:
                collide(particle, particle2)
            self.set_rect(particle)
            for j, curve in enumerate(self.curves):
                PcollideC(particle, curve)

        for i, curve in enumerate(self.curves):
            if(self.curveTouchedGround):
                pass
            else:
                curve.move()
                if self.acceleration:
                    curve.accelerate(self.acceleration)
                self.interact(curve)
                for curve2 in self.curves[i+1:]:
                    collideCurve(curve, curve2)
                self.set_rect_curve(curve)

#attempt to check a particle against a particle in the curve
        
        # listOfTempParticles = []
        # for i, particle in enumerate(self.particles):
        #     for j, curve in enumerate(self.curves):
        #         for a in range(len(curve.x)):
        #             tempParticle = Particle(curve.x[a], curve.y[a], curve.size, curve.mass)
        #             listOfTempParticles.append(tempParticle) 
        # for p in listOfTempParticles:
        #     PcollideC(particle, p)
    
    # this is where we add the obstacles 
    def addConstraints(self):
        """ Modify the boundary of the environment according to level """
        mass = len(self.constraints) * 10000

        curve = Curve(self.constraints,10,mass)
        curve.speed = random.random()
        curve.angle = 0
        curve.colour = (0,0,0)
        curve.drag = (curve.mass/(curve.mass+ self.mass_of_air)) ** curve.size

        self.curves.append(curve)

           

    def bounce(self, particle):
        """ Tests whether a particle has hit the boundary of the environment """
        
        if particle.x > self.width - particle.size:
            
            particle.x = 2*(self.width - particle.size) - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
            self.touchedRightWall = True
        
        elif particle.x < 150: # offset from the left edge
            particle.x = 2*(160-particle.size) - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
            self.touchedLeftWall = True

        elif particle.x < particle.size:
            particle.x = 2*particle.size - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
            print("two particle touches")

        if particle.y > self.height - particle.size:
            particle.y = 2*(self.height - particle.size) - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity
            self.touchedGround = True

        
        elif particle.y < 50: # offset from the upper edge
            particle.y = 2*(60-particle.size) - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity


        elif particle.y < particle.size:
            particle.y = 2*particle.size - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity

    def interact(self, curve):
        """ Tests whether a curve has hit the boundary of the environment """
        for i in range(len(curve.x)):
            if curve.x[i] > self.width - curve.size:
                curve.x[i] = 2*(self.width - curve.size) - curve.x[i]
                curve.angle = - curve.angle
                curve.speed *= self.elasticity
                self.touchedRightWall = True

            elif curve.x[i] < 150: # offset from the left edge
                curve.x[i] = 2*(160-curve.size) - curve.x[i]
                curve.angle = - curve.angle
                curve.speed *= self.elasticity
                self.touchedLeftWall = True

            elif curve.x[i] < curve.size:
                curve.x[i] = 2*curve.size - curve.x[i]
                curve.angle = - curve.angle
                curve.speed *= self.elasticity
                break

        for j in range(len(curve.y)):
            if curve.y[j] > self.height - curve.size:
                curve.y[j] = 2*(self.height - curve.size) - curve.y[j]
                curve.angle = math.pi - curve.angle
                curve.speed *= self.elasticity
                self.touchedGround = True
                self.curveTouchedGround = True
                
            elif curve.y[j] < 50: # offset from the upper edge
                curve.y[j] = 2*(60-curve.size) - curve.y[j]
                curve.angle = math.pi - curve.angle
                curve.speed *= self.elasticity

            elif curve.y[j] < curve.size:
                curve.y[j] = 2*curve.size - curve.y[j]
                curve.angle = math.pi - curve.angle
                curve.speed *= self.elasticity
                break

    def findParticle(self, x, y):
        """ Returns any particle that occupies position x, y """
        
        for particle in self.particles:
            if math.hypot(particle.x - x, particle.y - y) <= particle.size:
                return particle
        return None


class Quadtree(object):
    def __init__(self, level, rect, particles=[], color = (0,0,0)):
        '''Quadtree box at with a current level, rect, list of particles, and color(if displayed)
        level: set to zero for "trunk" of quadtree
        rect: should be entire display for "trunk" of quadtree
        particles: list of all particles for collision testing'''
        self.maxlevel = 5#max number of subdivisions
        self.level = level#current level of subdivision
        self.maxparticles = 3#max number of particles without subdivision
        self.rect = rect#pygame rect object
        self.particles = particles#list of particles
        self.color = color#color of box if displayed
        self.branches = []#empty list that is filled with four branches if subdivided
        self.displayTree = True#boolean to display quadtree boxes behind particles

    def rect_quad_split(self,rect):
        '''Splits rect object into four smaller rect objects'''
        w=rect.width/2.0
        h=rect.height/2.0
        rl=[]
        rl.append(pygame.Rect(rect.left, rect.top, w, h))
        rl.append(pygame.Rect(rect.left+w, rect.top, w, h))
        rl.append(pygame.Rect(rect.left, rect.top+h, w, h))
        rl.append(pygame.Rect(rect.left+w, rect.top+h, w, h))
        return rl

    def get_rect(self):
        '''Returns quadtree rect object'''
        return self.rect

    def subdivide(self):
        '''Subdivides quadtree into four branches'''
        for rect in self.rect_quad_split(self.rect):
            branch = Quadtree(self.level+1, rect, [], (self.color[0]+30,self.color[1],self.color[2]))
            self.branches.append(branch)

    def add_particle(self, particle):
        '''Adds a particle to the list of particles inside quadtree box'''
        self.particles.append(particle)

    def subdivide_particles(self):
        '''Subdivides list of particles in current box to four branch boxes'''
        for particle in self.particles:
            for branch in self.branches:
                if branch.get_rect().colliderect(particle.get_rect()):
                    branch.add_particle(particle)

    def render(self, display):
        '''Displays quadtree box on the display surface given'''
        pygame.draw.rect(display, self.color, self.rect)

    def test_collisions(self):
        '''Tests for collisions between all particles in the particle list'''
        for i, particle in enumerate(self.particles):
            for particle2 in self.particles[i+1:]:
                collide(particle, particle2)
            
    def update(self, display):
        '''Updates the quadtree and begins recursive process of subdividing or collision testing'''
        if len(self.particles) > self.maxparticles and self.level <= self.maxlevel:
            self.subdivide()
            self.subdivide_particles()
            for branch in self.branches:
                branch.update(display)
        else:
            self.test_collisions()
            if self.displayTree:
                self.render(display)


if __name__ == "__main__":
    myWelcomScreen = splashScreen()
    myWelcomScreen.run()
