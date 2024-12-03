#Sources: from 112 course notes on OOP classes
#https://www.cs.cmu.edu/~112/notes/notes-oop-part2.html

#No external sources, no external help, all images cited at the bottom of main.
#All code is my own.

from main import *
from generateOrder import *
from foodclasses import *
from foodclasses import *

#serving food- grill, fryer, cutting board, drink dispenser, bag, window

class Grill():
    def __init__(self, app):
        self.patties = []
        self.numberOfPatties = len(self.patties)
        #can fit up to 4 patties
        self.spots = [(app.width*0.414, app.height*0.485), 
        (app.width*0.53, app.height*0.485), 
        (app.width*0.415, app.height*0.688), 
        (app.width*0.53, app.height*0.688)]
    def addItem(self, patty):
        self.patties.append(patty)
    def removeItem(self, patty):
        self.patties.remove(patty)
        self.numberOfPatties -= 1

class Fryer():
    def __init__(self, app):
        self.potatoes = []
        self.numberOfPotatoes = len(self.potatoes)
        #can fit up to 2 potatoes
        self.spots = [(app.width*0.781, app.height*0.743), \
        (app.width*0.874, app.height*0.743)]
    def addItem(self, potato):
        self.potatoes.append(potato)
    def removeItem(self, potato):
        self.potatoes.remove(potato)
        self.numberOfPotatoes -= 1

class CuttingBoard():
    def __init__(self, app):
        self.items = []
        self.numberOfItems = len(self.items)
        #can fit up to 1 item (lettuce, tomato, potato)
        self.x = app.width*0.789
        self.y = app.height*0.496
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
        self.numberOfItems -= 1

class DrinkMachine():
    def __init__(self, app):
        self.drinks = []
        self.numberOfDrinks = len(self.drinks)
        #can fit only 1 drink in 3 different spots
        self.spots = [(app.width*0.068, app.height*0.208), \
        (app.width*0.116, app.height*0.208), \
        (app.width*0.164, app.height*0.208)]
        self.drink = False #changes to True if a drink is placed
        self.flavors = app.flavors
    def addDrink(self, drink):
        self.drinks.append(drink)
    def removeDrink(self, drink):
        self.drinks.remove(drink)
        self.numberOfDrinks -= 1

class Bag():
    def __init__(self, app):
        self.items = []
        self.numberOfItems = len(self.items)
        self.img = app.bagScaled
        self.x = app.bagX
        self.y = app.bagY
    def addToBag(self, app, item): 
        #takes in object and adds to order within bag
        #can only have one order per bag, but multiple items within order
        if self.items == []:
            servingOrder = Order(app, 0, 0)
            servingOrder.addItem(item)
            self.items.append(servingOrder)
        elif len(self.items) == 1:
            if isinstance(self.items[0], Order):
                self.items[0].addItem(item)

class Window():
    #the window class tracks the score for the CURRENT day (self.score)
    def __init__(self, app):
        self.x = 0
        self.y = 0
        self.orders = []
        self.score = 0
    def addOrder(self, order):
        self.orders.append(order)
    #where your score for the order is computed
    def calculateScore(self, app):
        #look at each item in bag and compare it to order to reward points
        for completedOrder in self.orders:
            points = 0
            comparingOrder = app.orders[0]
            #saving the time the order has been completed to variable self.timer
            completedOrder.timer = comparingOrder.timer
            
            #computes score of order
            # completedOrder.generateScore()
            #comparing each individual item in the order with the required items
            for item in completedOrder.details:
                for requiredItem in comparingOrder.details:
                    if isinstance(item, Burger) and item == requiredItem:
                        #comparing burger ingredients and rewarding points
                        for ingredient in item.ingredients:
                            for reqIngredient in requiredItem.ingredients:
                                if isinstance(ingredient, CookedPatty) and \
                                ingredient == reqIngredient:
                                    points += 200
                                elif (isinstance(ingredient, Lettuce) or \
                                isinstance(ingredient, Tomato)) and \
                                ingredient == reqIngredient:
                                    points += 100
                                elif isinstance(ingredient, Cheese) and \
                                ingredient == reqIngredient:
                                    points += 50
                                elif isinstance(ingredient, TopBun) and \
                                ingredient == reqIngredient:
                                    points += 50
                    #comparing drink flavors and rewarding points
                    elif isinstance(item, Drink) and item == requiredItem:
                        if item.flavor != requiredItem.flavor:
                            points += 100
                        else: points += 200
                    #comparing fries and rewarding points
                    elif isinstance(item, Fries) and item == requiredItem:
                        points += 300

            #computing score based on timeliness of order
            #algorithm is designed to reward those who complete orders quickly,
            #but also provides a little padding to orders that are not
            timedPoints = int(points * \
            (int(100*int(100*completedOrder.timer/100000)**2)**(1/3))/100)

            #if your order has extra items, you lose 25 points per item
            if len(completedOrder.details) > len(comparingOrder.details):
                timedPoints -= 25 * \
                (len(completedOrder.details) - len(comparingOrder.details))

            #adds to the score for the day (self.score)
            self.score += timedPoints
            self.orders.remove(completedOrder)
            app.orders.pop(0)
            for remainingOrder in app.orders:
                #resetting timer after every order is served
                remainingOrder.resetTimer
        
class Trash():
    #trash removes the item placed in it from the screen
    def __init__(self, app):
        self.x = 0
        self.y = 0
    def addToTrash(app, item):
        if item in app.itemPlaced:
            app.itemPlaced.remove(item)
        if item in app.itemHeld:
            app.itemHeld.remove(item)