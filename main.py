#Sources: from 112 course notes on animations
#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
#https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html

#Loading and scaling image from 112 course notes
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html

#No external sources, No external help, All images cited at the bottom.
#All code is my own.

from cmu_112_graphics import *
from mouseEvents import *
from foodclasses import * 
from timerFired import *
from servingfoodclasses import *

def appStarted(app):
    #start screen
    app.startScreen = True
    app.startScreenImg = app.loadImage('images/startscreen.png')
    app.startScreenTime = 0

    #pause screen / end of each day screens
    app.pauseScreen = False
    app.pauseDuration = 0

    #how to play screen
    app.howToPlay = False
    app.howToPlayTime = 0
    app.howToPlayImg = app.loadImage('images/howToPlay.png')

    #day screens
    app.day1Screen = app.loadImage('images/Day1.png')
    app.day2Screen = app.loadImage('images/Day2.png')
    app.day3Screen = app.loadImage('images/Day3.png')
    app.day4Screen = app.loadImage('images/Day4.png')
    app.day5Screen = app.loadImage('images/Day5.png')
    app.day6Screen = app.loadImage('images/Day6.png')
    app.day7Screen = app.loadImage('images/Day7.png')

    app.gameStarted = False
    app.gameOver = False
    app.youWin = False
    app.youWinImg = app.loadImage('images/You-Win.png')
    app.youLose = False
    app.youLoseImg = app.loadImage('images/You-Lose.png')

    #day 1-7
    #5 min for each day
    app.timer = 300000
    app.timePassed = 0 
    app.timerDelay = 1000 

    app.startScreen = True
    app.howToPlay = False
    app.dayStart = False
    app.dayEnd = False

    #levelScores: scores needed to pass to the next level
    app.levelScores = [2000, 3000, 5000, 7000, 10000, 13000, 15000]

    #scores represent the player's scores for each day
    app.scores = [app.day1Screen, app.day2Screen, app.day3Screen, 
    app.day4Screen, app.day5Screen, app.day6Screen, app.day7Screen]
    #playerScore is updated when the game is over (the sum of app.scores)
    app.playerScore = 0

    app.dayCounter = 0
    #dictionary of difficulties assigned by day, accessed by app.dayCounter
    #key : {day: [possible burgers, possible fries, possible drinks]}
    app.diff = {0:[3,2,2], 1:[3,3,3], 2:[4,3,3], 3:[4,4,4], 4:[4,4,4], 
    5:[4,4,4], 6:[4,5,5]}

    #list of all orders inside the system (up to 3, orders are OOP classes)
    app.orders = [] 
    
    #possible drink flavors
    app.flavors = ['Coke', 'Fanta', 'Mountain Dew']
    
    #ingredient images
    app.kitchen = app.loadImage('images/Kitchen.png')

    app.topBun = app.loadImage('images/TopBun.png')
    app.topBunScaled = app.scaleImage(app.topBun, 2/3)
    
    app.bottomBun = app.loadImage('images/BottomBun.png')
    app.bottomBunScaled = app.scaleImage(app.bottomBun, 2/3)

    app.cheese = app.loadImage('images/Cheese.png')
    app.cheeseScaled = app.scaleImage(app.cheese, 2/3)

    app.uncutLettuce = app.loadImage('images/UncutLettuce.png')
    app.uncutLettuceScaled = app.scaleImage(app.uncutLettuce, 2/3)

    app.patty = app.loadImage('images/Patty.png')
    app.pattyScaled = app.scaleImage(app.patty, 2/3)

    app.uncutTomato = app.loadImage('images/UncutTomato.png')
    app.uncutTomatoScaled = app.scaleImage(app.uncutTomato, 4/5)

    app.lettuce = app.loadImage('images/Lettuce.png')
    app.lettuceScaled = app.scaleImage(app.lettuce, 2/3)

    app.tomato = app.loadImage('images/Tomato.png')
    app.tomatoScaled = app.scaleImage(app.tomato, 2/3)

    app.cookedPatty = app.loadImage('images/CookedPatty.png')
    app.cookedPattyScaled = app.scaleImage(app.cookedPatty, 2/3)

    app.potato = app.loadImage('images/Potato.png')
    app.potatoScaled = app.scaleImage(app.potato, 4/5)

    app.cutPotato = app.loadImage('images/CutPotato.png')
    app.cutPotatoScaled = app.scaleImage(app.cutPotato, 2/3)

    app.fries = app.loadImage('images/Fries.png')
    app.friesScaled = app.scaleImage(app.fries, 2/3)

    #burger images
    app.BP = app.loadImage('images/BP.png')
    app.BPScaled = app.scaleImage(app.BP, 2/3)
    app.BPC = app.loadImage('images/BPC.png')
    app.BPCScaled = app.scaleImage(app.BPC, 2/3)
    app.BPCL = app.loadImage('images/BPCL.png')
    app.BPCLScaled = app.scaleImage(app.BPCL, 2/3)
    app.BPCLT = app.loadImage('images/BPCLT.png')
    app.BPCLTScaled = app.scaleImage(app.BPCLT, 2/3)
    app.BPCLTOP = app.loadImage('images/BPCLTOP.png')
    app.BPCLTOPScaled = app.scaleImage(app.BPCLTOP, 2/3)
    app.BPCLTTOP = app.loadImage('images/BPCLTTOP.png')
    app.BPCLTTOPScaled = app.scaleImage(app.BPCLTTOP, 2/3)
    app.BPCT = app.loadImage('images/BPCT.png')
    app.BPCTScaled = app.scaleImage(app.BPCT, 2/3)
    app.BPCTOP = app.loadImage('images/BPCTOP.png')
    app.BPCTOPScaled = app.scaleImage(app.BPCTOP, 2/3)
    app.BPCTTOP = app.loadImage('images/BPCTTOP.png')
    app.BPCTTOPScaled = app.scaleImage(app.BPCTTOP, 2/3)
    app.BPL = app.loadImage('images/BPL.png')
    app.BPLScaled = app.scaleImage(app.BPL, 2/3)
    app.BPLT = app.loadImage('images/BPLT.png')
    app.BPLTScaled = app.scaleImage(app.BPLT, 2/3)
    app.BPLTOP = app.loadImage('images/BPLTOP.png')
    app.BPLTOPScaled = app.scaleImage(app.BPLTOP, 2/3)
    app.BPLTTOP = app.loadImage("images/BPLTTOP.png")
    app.BPLTTOPScaled = app.scaleImage(app.BPLTTOP, 2/3)
    app.BPT = app.loadImage('images/BPT.png')
    app.BPTScaled = app.scaleImage(app.BPT, 2/3)
    app.BPTOP = app.loadImage('images/BPTOP.png')
    app.BPTOPScaled = app.scaleImage(app.BPTOP, 2/3)
    app.BPTTOP = app.loadImage('images/BPTTOP.png')
    app.BPTTOPScaled = app.scaleImage(app.BPTTOP, 2/3)

    #drink images
    app.emptyDrink = app.loadImage('images/D.png')
    app.emptyDrinkScaled = app.scaleImage(app.emptyDrink, 17/20)
    app.coke = app.loadImage('images/DB.png')
    app.cokeScaled = app.scaleImage(app.coke, 17/20)
    app.fanta = app.loadImage('images/DO.png')
    app.fantaScaled = app.scaleImage(app.fanta, 17/20)
    app.mountainDew = app.loadImage('images/DG.png')
    app.mountainDewScaled = app.scaleImage(app.mountainDew, 17/20)

    #miscellaneous images
    #message that appears when you try to serve an item that is not in a bag
    app.cannotServe = app.loadImage('images/cannotserve.png')
    #order that appears at the top right of the screen
    app.order = app.loadImage('images/Order.png')
    #bag to serve the order
    app.bag = app.loadImage('images/Bag.png')
    app.bagScaled = app.scaleImage(app.bag, 2/3)

    #mouse events (drag & drop)
    app.itemIsPickedUp = False
    app.itemIsPlaced = False

    app.itemHeld = []
    app.itemPlaced = []

    #toolbox bounds
    (app.topBunX, app.topBunY) = (app.width*0.083, app.height*0.4)
    (app.bottomBunX, app.bottomBunY) = (app.width*0.083, app.height*0.52)
    (app.cheeseX, app.cheeseY) = (app.width*0.084, app.height*0.655)
    (app.uncutLettuceX, app.uncutLettuceY) = (app.width*0.236, app.height*0.43)
    (app.pattyX, app.pattyY) = (app.width*0.083, app.height*0.794)
    (app.uncutTomatoX, app.uncutTomatoY) = (app.width*0.225, app.height*0.63)
    (app.potatoX, app.potatoY) = (app.width*0.086, app.height*0.938)
    (app.drinkX, app.drinkY) = (app.width*0.25, app.height*0.214)
    (app.bagX, app.bagY) = (app.width*0.647, app.height*0.909)

    #cooker bounds 
    (app.grillX, app.grillX2) = (app.width*0.333, app.width*0.607)
    (app.grillY, app.grillY2) = (app.height*0.369, app.height*0.821)
    (app.fryerX, app.fryerX2) = (app.width*0.715, app.width*0.935)
    (app.fryerY, app.fryerY2) = (app.height*0.646, app.height*0.863)
    (app.cuttingBoardX, app.cuttingBoardX2) = (app.width*0.714, app.width*0.934)
    (app.cuttingBoardY, app.cuttingBoardY2) = (app.height*0.4, app.height*0.608)

    #drink machine bounds
    (app.drinkMachineX, app.drinkMachineX2) = (app.width*0.04, app.height*0.198)
    (app.drinkMachineY, app.drinkMachineY2) = (app.height*0.029, app.height*0.293)
    (app.cokeX, app.cokeX2) = (app.width*0.034, app.width*0.091)
    (app.cokeY, app.cokeY2) = (app.height*0.028, app.height*0.293)
    (app.fantaX, app.fantaX2) = (app.width*0.09, app.width*0.142)
    (app.fantaY, app.fantaY2) = (app.height*0.03, app.height*0.296)
    (app.mountainDewX, app.mountainDewX2) = (app.width*0.141, app.width*0.185)
    (app.mountainDewY, app.mountainDewY2) = (app.height*0.028, app.height*0.291)

    #serving bounds
    (app.bagBoundX, app.bagBoundX2) = (app.width*0.613, app.width*0.71)
    (app.bagBoundY, app.bagBoundY2) = (app.height*0.821, app.height*0.9875)
    (app.windowX, app.windowX2) = (app.width*0.35, app.width*0.545)
    (app.windowY, app.windowY2) = (app.height*0.1625, app.height*0.291)

    #trash bounds
    (app.trashX, app.trashX2) = (app.width*0.867, app.width*0.961)
    (app.trashY, app.trashY2) = (app.height*0.918, app.height*0.977)

    #toolbox : for creating new items
    app.toolbox = {(app.topBunX, app.topBunY): TopBun(app, 0, 0), 
    (app.bottomBunX, app.bottomBunY): Burger(app, 0, 0, []),
    (app.cheeseX, app.cheeseY): Cheese(app, 0, 0, 0),
    (app.uncutLettuceX, app.uncutLettuceY): UncutLettuce(app, 0, 0),
    (app.pattyX, app.pattyY): Patty(app, 0, 0),
    (app.uncutTomatoX, app.uncutTomatoY): UncutTomato(app, 0, 0),
    (app.potatoX, app.potatoY): Potato(app, 0, 0),
    (app.drinkX, app.drinkY): Drink(app, None, 0, 0)}

    #cookers
    app.cookers = [Grill(app), Fryer(app), CuttingBoard(app), DrinkMachine(app),
    Bag(app), Window(app), Trash(app)]

    #burger images dictionary - for constructing a burger
    app.burgerImages = \
    {"bottom, patty": app.BPScaled, 
    "bottom, patty, cheese": app.BPCScaled, 
    "bottom, patty, cheese, top": app.BPCTOPScaled,
    "bottom, patty, cheese, lettuce": app.BPCLScaled,
    "bottom, patty, cheese, lettuce, tomato": app.BPCLTScaled,
    "bottom, patty, cheese, lettuce, top": app.BPCLTOPScaled,
    "bottom, patty, cheese, lettuce, tomato, top": app.BPCLTTOPScaled,
    "bottom, patty, cheese, tomato": app.BPCTScaled,
    "bottom, patty, cheese, tomato, top": app.BPCTTOPScaled,
    "bottom, patty, lettuce": app.BPLScaled,
    "bottom, patty, lettuce, tomato": app.BPLTScaled,
    "bottom, patty, lettuce, top": app.BPLTOPScaled,
    "bottom, patty, lettuce, tomato, top": app.BPLTTOPScaled,
    "bottom, patty, tomato": app.BPTScaled,
    "bottom, patty, top": app.BPTOPScaled,
    "bottom, patty, tomato, top": app.BPTTOPScaled}

#draws the kitchen and toolbox mechanics
def drawGame(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.kitchen))
    canvas.create_text(app.width*0.47, app.height*0.91, text= f'{app.timer//1000}', fill='yellow', font='SegoeUI 32')
    canvas.create_text(app.width*0.825, app.height*0.95, text=f'{app.cookers[5].score}', 
    fill='white', font='SegoeUI 36')
    for item in app.itemPlaced:
        canvas.create_image(item.x, item.y, image=ImageTk.PhotoImage(item.img))
    if app.itemIsPickedUp and not app.itemIsPlaced:
        for item in app.itemHeld:
            if not item == None:
                canvas.create_image(item.x, item.y, image=ImageTk.PhotoImage(item.img))
    for order in app.orders:
        canvas.create_image(order.x, order.y, image=ImageTk.PhotoImage(order.img))
        canvas.create_text(order.x, order.y, text=repr(order), justify='center', anchor='center',
        fill='black', font='SegoeUI 8')

#handles all drawing, including the loading, day start, day end screens)
def redrawAll(app, canvas):
    #start screen
    if app.startScreen:
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.startScreenImg))
    #how to play screen
    elif app.howToPlay:
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.howToPlayImg))
    #day end page
    elif not app.gameOver and app.dayEnd:
        #indexes into app.scores to find the next available day/level
        for dayScreen in app.scores:
            if not isinstance(dayScreen, int):
                canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(dayScreen))
                break
        #lettuce unlocked at day 3
        if app.dayCounter+2 == 3:
            canvas.create_text(app.width/2, app.height*4.5/5, \
                text='Unlocked Lettuce!', fill='white', font='SegoeUI 30')
        #tomato unlocked at day 5
        elif app.dayCounter+2 == 5:
            canvas.create_text(app.width/2, app.height*4.5/5, \
                text='Unlocked Tomato!', fill='white', font='SegoeUI 30')
        canvas.create_text(app.width/2, app.height*3.75/5, \
        text=f'Your Score: {app.playerScore}', fill='white', font='SegoeUI 30')
    #calls drawGame which draws kitchen and toolbox
    elif app.gameStarted or app.dayStart:
        drawGame(app, canvas)
    #handles you lose / you win screens
    elif app.gameOver:
        if app.youLose:
            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.youLoseImg))
        elif app.youWin:
            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.youWinImg))
        canvas.create_text(app.width/2, app.height*3.75/5, \
        text=f'Your Score: {app.playerScore}', fill='white', font='SegoeUI 30')

runApp(width=900, height=560)

#***
#image citations:
#Note: All images were legally purchased off of ShutterStock. 
#Using basic Adobe Illustrator skills and purchased images, 
#I created the kitchen interface as well as the start, how to play, day 1-7, you win, you lose screens. 
#All sources for the images are linked below.

#Start Screen
#Burgeria 112 font: 
#https://www.shutterstock.com/image-vector/neon-alphabet-duo-script-bold-vector-1343064032
#Burgeria 112 restaurant image:
#https://www.shutterstock.com/image-vector/modern-establish-isometric-commercial-restaurant-building-654425158
#Welcome text:
#https://www.shutterstock.com/image-vector/welcome-greeting-card-banner-poster-sticker-1183111462

#You Lose / You Win Screens
#Font Used:
#Note: Using this font I downloaded, I created the "You Lose", "You Win", "Day", "How To Play" icons.
#https://www.shutterstock.com/image-vector/3d-typeface-game-logo-tittle-text-1172080231
#Restart / Quit Buttons:
#https://www.shutterstock.com/image-vector/game-ui-set-buttons-gui-build-1065247244
#Sorry We're Closed Icon:
#https://www.shutterstock.com/image-vector/sorry-we-closed-sign-red-color-1615424080
#You Win Money Icon:
#https://www.shutterstock.com/image-vector/unboxing-present-gift-surprise-box-dollar-769043443
#You Win Falling Money Icon:
#https://www.shutterstock.com/image-vector/falling-dollar-banknotes-money-rain-flat-1175469712

#Day 1-7 Screen Burger & Fries Icons
#https://www.shutterstock.com/image-vector/fast-food-menu-vector-illustration-227109667

#Interface Parts
#Timer:
#https://www.shutterstock.com/image-vector/electronic-alarm-clock-icon-modern-flat-226299877
#Bag:
#https://www.shutterstock.com/image-vector/lunch-bag-flat-vector-illustration-set-1681808371
#Plate:
#https://www.shutterstock.com/image-vector/vector-3d-realistic-white-empty-porcelain-1919796437
#Grill, Fryer, Cutting Board:
#https://www.shutterstock.com/image-vector/vector-set-kitchen-utensils-top-view-2036364308
#Drink Dispenser and Drink:
#Note: I colored the drink blue and drew the "112" icon myself, as I did for the fries.
#https://www.shutterstock.com/image-vector/vending-machine-soda-cinema-vector-illustration-568020922

#Fries in the package:
#Note: I colored the fries blue and drew the "112" icon on the fries as well as the drink myself.
#https://www.shutterstock.com/image-vector/french-fries-hamburger-soda-takeaway-vector-454704091

#Burger Ingredients (TopBun, BottomBun, CookedPatty, Cheese, CutLettuce, CutTomato):
#Note: For the assembled burgers, I created the different combinations using the icons below.
#Also, for the raw patty, I colored the cooked patty red by myself. 
#https://www.shutterstock.com/image-vector/set-ingredients-burger-sandwich-sliced-veggies-713792833

#Vegetables (Lettuce, Tomato, Potato):
#https://www.shutterstock.com/image-vector/set-fruits-vegetables-450863761
#Cut Potato:
#https://www.shutterstock.com/image-vector/potatoes-isolated-on-background-set-wedges-1807440646

