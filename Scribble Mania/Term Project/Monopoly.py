from tkinter import *
from PIL import ImageTk, Image
import copy
import random
####################################
# customize these functions
####################################

class Monopoly(object):
    def __init__(self):
        self.roadD = {1:("Mediterranean Avenue",60),2:("Community Chest",0),
            3:("Baltic Avenue",60),4:("Income Tax",200),
            5:("Reading Railroad",200),6:("Oriental Avenue",100),
            7:("Chance",0),8:("Vermont Avenue",100),
            9:("Connecticut Avenue",120),10:("Just Visiting",0),
            11:("St. Charles Place",140),12:("Electric Company",150),
            13:("States Avenue",140),14:("Virginia Avenue",160),
            15:("Pennsylvania Railroad",200),16:("St. James Place",180),
            17:("Community Chest",0),18:("Tennessee Avenue",180),
            19:("New York Avenue",200),20:("Free Parking",0),
            21:("Kentucky Avenue",220),22:("Chance",0),
            23:("Indiana Avenue",220),24:("Illinois Avenue",240),
            25:("B. & O. Railroad",200),26:("Atlantic Avenue",260),
            27:("Ventnor Avenue",260),28:("Water Works",150),
            29:("Marvin Gardens",280),30:("Go To Jail",0),
            31:("Pacific Avenue",300),32:("North Carolina Avenue",300),
            33:("Community Chest",0),34:("Pennsylvania Avenue",320),
            35:("Short Line",200),36:("Chance",0),
            37:("Park Place",350),38:("Luxury Tax",100),
            39:("Boardwalk",400),40:("Go",200),}
        
        self.roadInfo = {1:(2,10,30,90,160,250),2:(0),
            3:(4,20,60,180,320,450),4:(0),
            5:(25),6:(6,30,90,270,400,550),
            7:(0),8:(6,30,90,270,400,550),
            9:(8,40,100,300,450,600),10:(0),
            11:(10,50,150,450,625),12:(4,10),
            13:(10,150,450,625,750),14:(12,60,180,500,700,900),
            15:(25),16:(14,70,200,550,750,950),
            17:(0),18:(14,70,200,550,750,950),
            19:(16,80,220,600,800),20:(0),
            21:(18,90,250,700,875,1050),22:(0),
            23:(18,90,250,700,875,1050),24:(20,100,300,750,925,1100),
            25:(25),26:(22,110,330,800,975,1150),
            27:(22,110,330,800,975,1150),28:(4,10),
            29:(24,120,360,850,1025,1200),30:(0),
            31:(26,130,390,900,1100,1275),32:(26,130,390,900,1100,1275),
            33:(0),34:(28,150,450,1000,1200,1400),
            35:(25),36:(0),
            37:(35,175,500,1100,1300,1500),38:(0),
            39:(50,200,600,1400,1700,2000),40:(0),}
    
        self.house = {1:(50),2:(100),3:(150),4:(200)}
        self.color = {"Brown":["Mediterranean Avenue","Baltic Avenue"],
            "Light Blue":["Oriental Avenue","Vermont Avenue","Connecticut Avenue"],
            "Pink":["St. Charles Place","States Avenue","Virginia Avenue"],
            "Orange":["St. James Place","Tennessee Avenue","New York Avenue"],
            "Red":["Kentucky Avenue","Indiana Avenue","Illinois Avenue"],
            "Yellow":["Atlantic Avenue","Ventnor Avenue","Marvin Gardens"],
            "Green":["Pacific Avenue","North Carolina Avenue","Pennsylvania Avenue"],
            "Dark Blue":["Park Place","Boardwalk"]}
        self.stations = ["Reading Railroad","Pennsylvania Railroad",
                                "B. & O. Railroad","Short Line"]
        self.utilities = ["Electric Company","Water Works"]
        self.chance = {1:["Advance to Go (Collect $200)","Go"],
            2:["Advance to Illinois Ave. - If you pass Go, collect $200","Illinois Ave"],
            3:["Advance to St. Charles Place – If you pass Go, collect $200","St. Charles Place"],
            4:["Bank pays you dividend of $50",50],
            5:["You have won a crossword competition - Collect $100",100],
            6:["Your building loan matures – Collect $150",150],
            7:["You have been elected Chairman of the Board – Pay each player $50",-50.0],
            8:["Take a walk on the Boardwalk – Advance token to Boardwalk","Boardwalk"],
            9:["Pay poor tax of $15",-15]}
    
        self.commChest = {1:["You inherit $100",100],
            2:["You have won second prize in a beauty contest – Collect $10",10],
            3:["Receive $25 consultancy fee",25],
            4:["Pay school fees of $150",-150],
            5:["Pay hospital fees of $100",-100],
            6:["Life insurance matures – Collect $100",100],
            7:["It is your birthday - Collect $10 from each player",10.0],
            8:["Income tax refund – Collect $20",20],
            9:["Holiday Fund matures - Receive $100",100],
            10:["Grand Opera Night – Collect $50 from every player for opening night seats",50.0],
            11:["Advance to Go (Collect $200)","Go"],
            12:["Bank error in your favor – Collect $200",200],
            13:["Doctor's fees – Pay $50",-50],
            14:["From sale of stock you get $50",50]}

class Player(object):
    def __init__(self):
        self.place = []
        self.rail = []
        self.util = []
        self.cash = 1500
        self.mort = []
        self.pos = 0
        self.inJail = False
           
def init(data):
    data.gameMode = 0
    data.prevMode = 0
    data.startIm = Image.open('monopoly-logo.jpg')
    data.boardIm = Image.open('monopoly_converted.jpg')
    data.ruleIm = [Image.open('Rules1.jpg'),Image.open('Rules2.jpg')]
    data.helpPage = 1
    data.p1 = Player()
    data.p2 = Player()
    data.currentPlayer = 1
    data.GameOver = False
    data.fix = 20
    data.BoxInfo = {5:"Roll",4:"Buy",3:"Build",2:"Mortgage",1:"End turn",0:"Help"}
    data.fill= [-1,"red"]
    data.isRolled = False
    data.dice = 0

def mousePressed(event, data):
    for i in range(len(data.BoxInfo)):
        left,up,right,down = getCord(i,data)
        if event.x >= left and event.x <= right and event.y >= up and event.y <= down:
            data.fill[0] = i
            if i == 0:
                data.gameMode = -1
                data.prevMode = 1
            if data.BoxInfo[i] == "Roll" and data.isRolled == False:
                data.dice = random.randint(1,6) + random.randint(1,6)
                if data.currentPlayer == 1:
                    data.p1.pos = getPos(data.p1.pos, data.dice)
                else:
                    data.p2.pos = getPos(data.p2.pos, data.dice)
                data.isRolled = True
            elif data.BoxInfo[i] == "End turn":
                if data.currentPlayer == 1:
                    data.currentPlayer = 2
                else:
                    data.currentPlayer = 1
                data.dice = 0
                data.isRolled = False
                
        
def keyPressed(event, data):
    if data.gameMode == 0:
        if (event.keysym == "Return"):
            data.prevMode = data.gameMode
            data.gameMode = 1
        elif (event.keysym == "space"): 
            data.prevMode = data.gameMode
            data.gameMode = -1
    elif data.gameMode == -1:
        if (event.keysym == "r"):
            data.gameMode, data.prevMode = data.prevMode, data.gameMode
        if (event.keysym == "Right"): data.helpPage = 2
        elif (event.keysym == "Left"): data.helpPage = 1
        

def timerFired(data):
    if data.GameOver == False:
        if data.p1.cash == 0 and data.p1.place == [] and data.p1.util == [] and data.p1.rail == []:
            data.GameOver == True
        if data.p2.cash == 0 and data.p2.place == [] and data.p2.util == [] and data.p2.rail == []:
            data.GameOver == True

def redrawAll(canvas, data):
    if data.gameMode == 0:
        loadStart(canvas, data)
    elif data.gameMode == 1:
        loadBoard(canvas, data)
        drawBox(canvas,data)
        drawPlayer(canvas,data)
        drawGameInfo(canvas,data)
    elif data.gameMode == -1:
        loadHelp(canvas,data)
        
    
def loadBoard(canvas, data):
    canvas.image = ImageTk.PhotoImage(data.boardIm)
    canvas.create_image(0, 0, anchor = NW, image=canvas.image)
    
def loadStart(canvas, data):
    msg1 = "Welcome to the Monopoly Game!"
    msg2 = "Press enter to start!"
    msg3 = "Press space for instructions!"
    canvas.image = ImageTk.PhotoImage(data.startIm)
    canvas.create_image(data.width/2,data.height/3, image=canvas.image)
    canvas.create_text(data.width/2,data.height*0.6,text=msg1,fill="red",font="Times 28 bold")
    canvas.create_text(data.width/2,data.height*0.7,text=msg2,fill="green",font="Times 28 bold")
    canvas.create_text(data.width/2,data.height*0.8,text=msg3,fill="blue",font="Times 28 bold")
    
def loadHelp(canvas, data):
    if data.helpPage == 1:
        msg = "Press right arrow to view the next page!"
        canvas.image = ImageTk.PhotoImage(data.ruleIm[0])
        canvas.create_image(data.width/2, data.height*0.48, image=canvas.image)
        canvas.create_text(data.width*0.9,data.height*0.9,text=msg,fill="red",font="Times 15 bold")
    else:
        msg = "Press left arrow to view the next page!"
        canvas.image = ImageTk.PhotoImage(data.ruleIm[1])
        canvas.create_image(data.width/2, data.height*0.48, image=canvas.image)
        canvas.create_text(data.width*0.9,data.height*0.9,text=msg,fill="red",font="Times 15 bold")
    returnMsg = "Press R to return!"
    canvas.create_text(data.width*0.9,data.height*0.8,text=returnMsg,fill="red",font="Times 15 bold")
    
def drawBox(canvas,data):
    for i in range(len(data.BoxInfo)):
        left,up,right,down = getCord(i,data)
        canvas.create_rectangle(left,up,right,down, fill="yellow")
        if i not in data.fill:
            canvas.create_text((left+right)/2,(up+down)/2,text=data.BoxInfo[i])
        else:
            canvas.create_text((left+right)/2,(up+down)/2,text=data.BoxInfo[i],
                                fill = data.fill[1])
        
def getCord(i,data):
    margin = 10
    height = 40
    width = 80 
    left = data.width-width*(i%3+1)-margin*(i%3+1)
    up = data.height-height*(i//3+1)-margin*(i//3+1)-data.fix
    right = left + width
    down = up + height
    return (left,up,right,down)
 
def drawPlayer(canvas,data):
    pSize = 10
    cx,cy = getPLayerCod(canvas,data,1)
    canvas.create_rectangle(cx-pSize,cy-pSize,cx+pSize,cy+pSize,fill = "white")
    cx,cy = getPLayerCod(canvas,data,2)
    canvas.create_rectangle(cx-pSize,cy-pSize,cx+pSize,cy+pSize,fill = "white")
    
def getPLayerCod(canvas,data,player):
    smallMargin = 65
    largeMargin = 100
    if player == 1:
        startLeft = 710
        startDown = 700
        if data.p1.pos == 10:
            if data.p1.inJail == True:
                return(80,700)
            else:
                return (startLeft-9*smallMargin-largeMargin,startDown)
        elif data.p1.pos == 20:
            return (startLeft-9*smallMargin-largeMargin,startDown-9*smallMargin-largeMargin)
        elif data.p1.pos == 0:
            return (startLeft,startDown)
        elif data.p1.pos//10 == 0:
            return (startLeft-data.p1.pos*smallMargin,startDown)
        elif data.p1.pos//10 == 1:
            return (startLeft-9*smallMargin-largeMargin, startDown-(data.p1.pos%10)*smallMargin)
        elif data.p1.pos//10 == 2:
            return (startLeft-(10-data.p1.pos%10)*smallMargin, startDown-9*smallMargin-largeMargin)
        elif data.p1.pos//10 == 3:
            return (startLeft, startDown-(10-data.p1.pos%10)*smallMargin)
    if player == 2:
        startLeft = 710
        startDown = 725
        if data.p2.pos == 10:
            if data.p2.inJail == True:
                return(80,700)
            else:
                return (startLeft-9*smallMargin-largeMargin,startDown)
        elif data.p2.pos == 20:
            return (startLeft-9*smallMargin-largeMargin,startDown-9*smallMargin-largeMargin)
        elif data.p2.pos == 0:
            return (startLeft,startDown)
        elif data.p2.pos//10 == 0:
            return (startLeft-data.p2.pos*smallMargin,startDown)
        elif data.p2.pos//10 == 1:
            return (startLeft-9*smallMargin-largeMargin, startDown-(data.p2.pos%10)*smallMargin)
        elif data.p2.pos//10 == 2:
            return (startLeft-(10-data.p2.pos%10)*smallMargin, startDown-9*smallMargin-largeMargin)
        elif data.p2.pos//10 == 3:
            return (startLeft, startDown-(10-data.p2.pos%10)*smallMargin)
    
def drawGameInfo(canvas,data):
    diceMsg = "Roll Result: %d" %(data.dice)
    playerMsg = "Player %d's turn" %(data.currentPlayer)
    width,height = 100,50
    left,up,right,down = getCord(5,data)
    bUp = up-height-data.fix
    bRight = left+width
    bDown = up-data.fix
    canvas.create_rectangle(left,bUp,bRight,bDown,fill="yellow")
    canvas.create_rectangle(left+width+data.fix,bUp,bRight+width+data.fix,bDown,fill="yellow")
    canvas.create_text(left+width/2,up-data.fix-height/2,text=diceMsg)
    canvas.create_text(left+width*3/2+data.fix,bUp+height/2,text=playerMsg)
    
def getPos(player, dice):
    result = player + dice
    if result >= 40:
        result -= 40
    return result

    

####################################
# use the run function as-is
####################################

def run(width=1000, height=1000):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1425, 800)