#Sources: from 112 course notes on OOP, special methods, inheritance
#https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html
#https://www.cs.cmu.edu/~112/notes/notes-oop-part2.html

#No external sources, no external help, all images cited at the bottom of main.
#All code is my own.

from main import *
from cmu_112_graphics import *
from mouseEvents import * 
import math

#distance helper
def findDistance(x0, y0, x1, y1):
    return math.sqrt(((x1-x0)**2 + (y1-y0)**2))

#sources: from 112 course notes on OOP pt 1 and pt 2
class BottomBun():
    #bottom bun is always initialized as a new burger
    def __init__(self, app, x, y):
        self.name = 'BB'
        self.x = x
        self.y = y
        self.img = app.bottomBunScaled

class TopBun():
    def __init__(self, app, x, y):
        self.name = 'TB'
        self.x = x
        self.y = y
        self.img = app.topBunScaled
    def __eq__(self, other):
        if isinstance(other, TopBun):
            return True
        return False

class Cheese():
    def __init__(self, app, count, x, y):
        self.x = x
        self.y = y
        self.count = count
        self.img = app.cheeseScaled
    def __eq__(self, other):
        if isinstance(other, Cheese):
            return True
        return False

class UncutLettuce():
    def __init__(self, app, x, y):
        self.name = "Uncut Lettuce"
        self.x = x
        self.y = y
        self.cut = 0
        self.img = app.uncutLettuceScaled
    def __eq__(self, other):
        if isinstance(other, UncutLettuce):
            return True
        return False
    def cutItem(self):
        self.cut += 50

class Lettuce():
    def __init__(self, app, count, x, y):
        self.name = None
        self.x = x
        self.y = y
        self.count = count
        self.cut = 100
        self.img = app.lettuceScaled
    def __eq__(self, other):
        if isinstance(other, Lettuce):
            return True
        return False

class UncutTomato():
    def __init__(self, app, x, y):
        self.name = "Uncut Tomato"
        self.x = x
        self.y = y
        self.cut = 0
        self.img = app.uncutTomatoScaled
    def __eq__(self, other):
        if isinstance(other, UncutTomato):
            return True
        return False
    def cutItem(self):
        self.cut += 50

class Tomato():
    def __init__(self, app, count, x, y):
        self.name = None
        self.x = x
        self.y = y
        self.count = count
        self.cut = 100
        self.img = app.tomatoScaled
    def __eq__(self, other):
        if isinstance(other, Tomato):
            return True
        return False

class Patty():
    def __init__(self, app, x, y):
        self.x = x
        self.y = y
        self.state = 0 
        self.img = app.pattyScaled
    def cookPatty(self):
        self.state += 50

class CookedPatty(): 
    def __init__(self, app, x, y):
        self.x = x
        self.y = y
        self.state = 100 #fully cooked
        self.img = app.cookedPattyScaled
    def cookPatty(self):
        self.state += 50
    def __eq__(self, other):
        if isinstance(other, CookedPatty):
            return True
        return False

class Potato():
    def __init__(self, app, x, y):
        self.name = "Uncut Potato"
        super().__init__()
        self.cut = 0
        self.img = app.potatoScaled
    def __eq__(self, other):
        if isinstance(other, Potato):
            return True
        return False
    def cutItem(self):
        self.cut += 50

class cutPotato():
    def __init__(self, app, x, y):
        self.name = None
        self.x = x
        self.y = y
        self.cut = 100 #fully cut
        self.state = 0
        self.img = app.cutPotatoScaled
    def fryPotato(self):
        self.state += 50

class Fries():
    def __init__(self, app, x, y):
        self.name = None
        self.x = x
        self.y = y
        self.cut = 100 #fully cut
        self.state = 100 #fully fried
        self.img = app.friesScaled
    def __eq__(self, other):
        if isinstance(other, Fries):
            return True
        return False

class Burger():
    def __init__(self, app, x, y, ingredients):
        self.x = x
        self.y = y
        self.centerX = x
        self.centerY = y
        self.points = 0 #score of burger is dependent on its ingredients
        self.ingredients = ingredients
        self.img = app.bottomBunScaled
    
    def __eq__(self, other):
        if isinstance(other, Burger):
            return True
        return False

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def setImage(self, img):
        self.img = img

    #helper that calculates score of burger based on its ingredients
    def calculateScore(self):
        for ingredient in self.ingredients:
            if isinstance(ingredient, CookedPatty):
                self.points += 200
            if isinstance(ingredient, Tomato) \
            or isinstance(ingredient, Lettuce):
                self.points += 100
            if isinstance(ingredient, Cheese):
                self.points += 50
            if isinstance(ingredient, TopBun):
                self.points += 50
        return self.points

    #converts burger ingredients into string
    #allows the order to be displayed on the screen
    def __repr__(self):
        ingredientList = []
        for ingredient in self.ingredients:
            if isinstance(ingredient, CookedPatty):
                ingredientList.append('patty')
            elif isinstance(ingredient, Tomato):
                ingredientList.append('tomato')
            elif isinstance(ingredient, Lettuce):
                ingredientList.append('lettuce')
            elif isinstance(ingredient, Cheese):
                ingredientList.append('cheese')
        return ', '.join(ingredientList)

class Drink():
    def __init__(self, app, flavor, x, y):
        self.x = x
        self.y = y
        self.flavor = flavor
        self.fill = 0
        self.img = app.emptyDrinkScaled
    
    def __eq__(self, other):
        if isinstance(other, Drink):
            return True
        return False
    
    def setFlavor(self, app, flavor):
        self.flavor = app.flavors[flavor]
    
    def setImage(self, img):
        self.img = img
        
    def pour(self):
        self.fill += 50

