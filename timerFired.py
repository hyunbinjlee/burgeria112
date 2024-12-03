#Sources: from 112 course notes on animations
#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html

#Burger creation uses recursion from 112 course notes
#https://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html
#https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html

#No external sources, no external help, all images cited at the bottom of main.
#All code is my own.

from main import *
from foodclasses import *
from servingfoodclasses import *
from generateOrder import *
from gameMechanics import *

def timerFired(app):
    #only activates when the start screen is open
    #expires after 8 seconds
    if app.startScreen:
        app.startScreenTime += app.timerDelay
        if app.startScreenTime == 8000:
            app.startScreenTime = 0
            app.startScreen = False
            app.howToPlay = True
            app.gameStarted = False
            app.dayStart = False
        
    #handles how to play screen duration
    #expires after 9 seconds
    elif app.howToPlay:
        app.howToPlayTime += app.timerDelay
        if app.howToPlayTime == 9000:
            app.howToPlayTime = 0
            app.howToPlay = False
            app.gameStarted = True
            app.dayStart = True

    #activates when the new day begins
    #turns on gameMechanics, which handles all of the gameplay
    if app.dayStart:
        app.timePassed += app.timerDelay
        app.timerDelay = 1000
        app.timer -= app.timerDelay
        gameMechanics(app)
        if app.timer == 0:
            app.dayEnd = True
            app.dayStart = False

    #order expiration if it's not fulfilled in 100 seconds
    if len(app.orders) >= 1:
        for order in app.orders:
            order.expire(app.timerDelay)
            if order.timer <= 0:
                #if order is out of time, remove
                app.orders.remove(order)
 
    #activates when the day ends, resetting timer
    #determines if you lost the game or can move onto the next round
    if app.dayEnd:
        app.timer = 300000
        app.pauseScreen = True
        app.pauseDuration += app.timerDelay
        if app.pauseDuration % 4000 == 0:
            app.pauseDuration = 0
            app.dayCounter += 1
            #if your score is not sufficient or you pass all of the levels,
            #the game is over
            if app.cookers[5].score < app.levelScores[app.dayCounter - 1] \
            or app.dayCounter == len(app.scores):
                app.gameOver = True
                app.dayEnd = False
            else: 
                #adds player score for that day to the list of scores by day
                app.scores[app.dayCounter - 1] = app.cookers[5].score
                # app.pauseDuration = 0
                app.pauseScreen = False
                app.dayEnd = False
                app.dayStart = True
                #resets window score
                app.cookers[5].score = 0
                #reset orders
                app.orders = []
   
    #if the game is over, the player's score is computed
    #if the player has a sufficient score, the player has won the game
    #otherwise, the player has lost
    if app.gameOver:
        app.gameStarted = False
        app.startScreen = False
        app.pauseScreen = False
        scoreCount = 0
        for score in app.scores:
            if isinstance(score, int):
                scoreCount += 1
        if scoreCount == len(app.scores):
            #computing player score
            app.playerScore = sum(app.scores)
        if app.cookers[5].score < app.levelScores[app.dayCounter - 1]:
            #lose condition
            app.youLose = True
        elif app.cookers[5].score >= app.levelScores[app.dayCounter - 1]:
            #win condition
            app.youWin = True
        return 
    