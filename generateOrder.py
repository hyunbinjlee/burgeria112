#Sources: from 112 notes on dictionaries and OOP pt 2
#Creating OOP class Order
#https://www.cs.cmu.edu/~112/notes/notes-sets.html
#https://www.cs.cmu.edu/~112/notes/notes-dictionaries.html
#https://www.cs.cmu.edu/~112/notes/notes-oop-part2.html

#Order generation is recursive - from 112 course notes on recursion
#https://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html
#https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html

#No external sources, no external help, all images cited at the bottom of main.
#All code is my own.

import random
from main import *
from foodclasses import *
from servingfoodclasses import *

#generate an order
def createOrder(app):
    newOrder = Order(app, 0, 0)
    newOrder.generateOrder(app)
    newOrder.generateScore()
    app.orders.append(newOrder)

#OOP class Order
class Order(): 
    def __init__(self, app, x, y):
        self.x = x
        self.y = y
        self.details = []
        self.stringDetails = ''
        self.points = 0
        self.timer = 100000
        self.img = app.order
    def addItem(self, item):
        self.details.append(item)
    def expire(self, timerDelay):
        self.timer -= timerDelay
    def setImage(self, img):
        self.img = img
    def resetTimer(self):
        #restores to a reasonable expiration timer for orders
        if self.timer <= 70000:
            self.timer *= 1.2

    #random order generation
    #randomly generates 0, 1, 2, 3, 4 fries (dependent on the level you are on)
    def generateFries(self, app, friesCount): 
        for fries in range(friesCount-1):
            self.details.append(Fries(app, 0, 0))

    #randomly generates 0, 1, 2, 3, 4 drinks (dependent on the level you are on)
    #also generates random drink flavor
    def generateDrink(self, app, drinkCount):
        for drink in range(drinkCount-1):
            #randomizes flavor of the drink
            drinkFlavor = app.flavors[random.randint(0,2)]
            self.details.append(Drink(app, drinkFlavor, 0, 0))

    #randomly recursively generates burger ingredients (tomato, lettuce, cheese)
    def generateTomato(self, app, tomatoRange, count): #either 0 or 1
        if tomatoRange <= 0:
            if count != 0:
                return Tomato(app, count, 0, 0)
            else:
                return 
        return self.generateTomato(app, tomatoRange - 1, count + 1)
    
    def generateLettuce(self, app, lettuceRange, count):
        if lettuceRange <= 0:
            if count != 0:
                return Lettuce(app, count, 0, 0)
            else:
                return
        return self.generateLettuce(app, lettuceRange - 1, count + 1)

    def generateCheese(self, app, cheeseRange, count):
        if cheeseRange <= 0:
            if count != 0:
                return Cheese(app, count, 0, 0)
            else:
                return
        return self.generateCheese(app, cheeseRange - 1, count + 1)

    #randomly generates burger, calling the lettuce, tomato, cheese helpers
    #every burger must have a cooked patty and a top bun so that is default
    #orders do not have lettuce or tomato until they are unlocked
    def generateBurger(self, app):
        ingredients = [CookedPatty(app, 0, 0)]
        #on day 3, you unlock lettuce (dayCounter is incremented after this is called)
        if app.dayCounter >= 2:
            ingredients.append(self.generateLettuce(app, random.randrange(0, 2), 0))
        #on day 5, you unlock tomato
        if app.dayCounter >= 4:
            ingredients.append(self.generateTomato(app, random.randrange(0, 2), 0))
        ingredients.append(self.generateCheese(app, random.randrange(0, 2), 0))
        ingredients.append(TopBun(app, 0, 0))
        self.details.append(Burger(app, 0, 0, ingredients))

    #randomizes an order- up to 4 burgers, up to 4 fries, up to 4 drinks
    #complexity of order depends on the level
    #accesses app.diff dictionary containing the difficulty levels by day
    def generateOrder(self, app): 
        for burger in range(random.randrange(0, app.diff[app.dayCounter][0])):
            self.generateBurger(app)
        self.generateFries(app, random.randint(0, app.diff[app.dayCounter][1]))
        self.generateDrink(app, random.randint(0, app.diff[app.dayCounter][2]))
    
    #creates a score appropriate to the size of the order
    #larger order sizes are rewarded more points for completion
    def generateScore(self):
        for orderItem in self.details:
            if isinstance(orderItem, Burger):
                #helper function that calculates points for the burger
                points = orderItem.calculateScore()
                self.points += points
            elif isinstance(orderItem, Fries):
                self.points += 300
            elif isinstance(orderItem, Drink):
                self.points += 200
    
    #allows the order to be shown onto the screen by converting it into string
    def convertDetailsToString(self):
        burgers=0
        fries=0
        drinks=0
        orderStr = ''
        for orderItem in self.details:
            if isinstance(orderItem, Burger):
                burgers += 1
                #helper function that turns burger ingredients to words
                burgerIngredients = repr(orderItem)
                orderStr += 'Burger with' + "\n" + f'{burgerIngredients}' + "\n"
                #strHelper for burger turns burger ingredients into a string
            elif isinstance(orderItem, Drink):
                drinks += 1
                orderStr += f'{orderItem.flavor}' + "\n"
            elif isinstance(orderItem, Fries):
                fries += 1
        return orderStr + f'{fries} Fries' + "\n"

    #order is displayed on the screen along with how many points it earns
    def __repr__(self):
        return self.convertDetailsToString() + "\n" + f'${self.points}'

