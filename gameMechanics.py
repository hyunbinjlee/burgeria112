#Sources: 
#Animations from 112 course notes on animations
#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
#
#Order comparison & burger creation from 112 notes on conditionals & loops
#https://www.cs.cmu.edu/~112/notes/notes-conditionals.html
#https://www.cs.cmu.edu/~112/notes/notes-loops.html
#
#Cutting board and drink pouring mechanics uses sets and dictionaries
#from 112 course notes:
#https://www.cs.cmu.edu/~112/notes/notes-sets.html
#https://www.cs.cmu.edu/~112/notes/notes-dictionaries.html

#Burger creation uses recursion, from 112 course notes on recursion:
#https://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html
#https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html

#No external sources, no external help, all images cited at the bottom of main.
#All code is my own.

from main import *
from foodclasses import *
from servingfoodclasses import *
from generateOrder import *
import copy

#handles all game mechanics, once start & how to play & pause screens end
#mechanics: cooks food and creates burgers

def gameMechanics(app):
    #restarts timePassed after the start screen ends
    if app.gameStarted == True and app.timePassed == 4000:
        app.timePassed = 0
        if len(app.orders) < 3:
            #if there are less than 3 orders on the screen, create a new order
            createOrder(app)
            for order in app.orders:
                #cannot have blank orders
                if order.points == 0 or order.details == []:
                    app.orders.remove(order)
                    createOrder(app)
        #handling placement of orders on screen as they are fulfilled
        for orderIndex in range(len(app.orders)):
            order = app.orders[orderIndex]
            space = app.width/8
            order.x = 2 * app.width/3 + space * orderIndex
            order.y = app.height/5

    #cooking/frying/cutting mechanics
    #you can have max 4 patties on the grill, 2 potatoes in the fryer, 
    #1 on the cutting board, 1 in the drink dispenser
    if 0 < app.cookers[0].numberOfPatties <= 4:
        grillCook(app, CookedPatty(app, 0, 0))
    if 0 < app.cookers[1].numberOfPotatoes <= 2:
        fryerCook(app, Fries(app, 0, 0))
    if 0 < app.cookers[2].numberOfItems <= 1:
        cuttingBoardCut(app, {"Uncut Lettuce": Lettuce(app, 0, 0, 0), \
        "Uncut Tomato": Tomato(app, 0, 0, 0), \
        "Uncut Potato": cutPotato(app, 0, 0)})
    if app.cookers[3].numberOfDrinks == 1:
        drinkPour(app)
    if len(app.itemPlaced) >= 2:
        #recurring burger check
        #checks if you can create a burger with what is currently available
        possibleToMakeBurger(app)

#cooking on the grill
def grillCook(app, patties):
    for rawPatty in app.cookers[0].patties:
        if not isinstance(rawPatty, CookedPatty):
            #if patty is fully cooked, change patty to fully cooked state
            if rawPatty.state >= 100:
                #replace raw with cooked
                replaceItem(app, app.cookers[0], rawPatty, patties)
                return
            else:
                #cook the patty if it isn't already cooked
                rawPatty.cookPatty()

#cooking in the fryer
def fryerCook(app, fries):
    for cuttedPotato in app.cookers[1].potatoes:
        if not isinstance(cuttedPotato, Fries):
            #if item is fully fried, change item to fully fried state
            if cuttedPotato.state >= 100:
                #replace raw with fried
                replaceItem(app, app.cookers[1], cuttedPotato, fries)
                if cuttedPotato in app.itemPlaced:
                    app.itemPlaced.remove(cuttedPotato)
                return
            else:
                #fry the potato if it isn't already fried
                cuttedPotato.fryPotato()

#cutting on the board
def cuttingBoardCut(app, d):
    item = app.cookers[2].items[0]
    notIllegalCounter = 0
    illegalList = [Lettuce, Tomato, cutPotato]
    for illegalItem in illegalList:
        if not isinstance(item, illegalItem):
            notIllegalCounter += 1
    if notIllegalCounter == len(illegalList):
        #if item is fully cut, change the item to its fully cut state
        if item.cut >= 100 and item.name != None:
            #if the item is fully cut, replace raw version with cut version
            replaceItem(app, app.cookers[2], item, d[item.name])
            return
        else: 
            #cut the item if it isn't fully cut
            item.cutItem()
            
#pouring from drink dispenser
def drinkPour(app):
    flavors = {'Coke': app.cokeScaled, \
    'Fanta': app.fantaScaled, \
    'Mountain Dew': app.mountainDewScaled}
    for emptyDrink in app.cookers[3].drinks:
        if isinstance(emptyDrink, Drink):
            if emptyDrink.fill >= 100:
                #replace empty drink with full drink if empty drink is full
                emptyDrink.setImage(flavors[emptyDrink.flavor])
                if emptyDrink in app.cookers[3].drinks:
                    app.cookers[3].drinks.remove(emptyDrink)
                    app.cookers[3].numberOfDrinks -= 1
                return
            else:
                #pour drink if it isn't full
                emptyDrink.pour()

#replace raw item with cooked item
def replaceItem(app, cooker, item, sprite):
    #deepcopy the cooked version from the toolbox
    newItem = copy.deepcopy(sprite)
    newItem.x = item.x
    newItem.y = item.y
    app.itemPlaced.append(newItem)
    #remove raw item
    cooker.removeItem(item)
    if item in app.itemPlaced:
        app.itemPlaced.remove(item)

#constructing a burger
def possibleToMakeBurger(app):
    #legality checks for if it is possible for a burger to be made
    currentBurger = None
    potentialIngredients = []
    for burgerBase in app.itemPlaced:
        if not isinstance(burgerBase, Burger):
            continue
        for ingredient in app.itemPlaced:
            if isinstance(ingredient, Burger) or burgerBase == ingredient:
                continue
            #center x and center y are set for ease of placement
            burgerBase.centerX = burgerBase.x
            burgerBase.centerY = burgerBase.y
        #compare 2 items and see if it's possible to turn them into a burger
            #if the items are in proximity check
            if findDistance(burgerBase.centerX, burgerBase.centerY, \
            ingredient.x, ingredient.y) <= 50:
                if ingredient not in burgerBase.ingredients:
                    currentBurger = burgerBase
                    potentialIngredients.append(ingredient)
                    currentIngredient = potentialIngredients[-1]
                    #reverse to convert to string to check for legality
                    reversedCurrentIng = reversed(currentBurger.ingredients)
                    for current in reversedCurrentIng:
                        potentialIngredients.insert(0, current)
    #if the burger itself is legal (found in the dictionary of legal burgers)
    if isLegalBurger(app, potentialIngredients) != False:
        #helper function that checks if the burger that is being created 
        #can be represented by an image (legality check)
        burgerString = isLegalBurger(app, potentialIngredients)
        #creating the burger itself
        currentBurger.ingredients.append(currentIngredient)
        app.itemIsPickedUp = False
        #removing it from your hand and adding it to the burger
        if currentIngredient in app.itemHeld:
            app.itemHeld.remove(currentIngredient)
        app.itemPlaced.remove(currentIngredient)
        currentBurger.setImage(app.burgerImages[burgerString])

def isLegalBurger(app, ingredients):
    #locate matching image in app.burgerImages dict using string
    stringCommas = ', '.join(['bottom'] + convertBurgerToString(ingredients))
    if stringCommas in app.burgerImages:
        return stringCommas
    return False

#string conversion of ingredients to burger for legality check
def convertBurgerToString(ingredients):
    if ingredients == []:
        return []
    elif isinstance(ingredients[0], CookedPatty):
        return ['patty'] + convertBurgerToString(ingredients[1:])
    elif isinstance(ingredients[0], Cheese):
        return ['cheese'] + convertBurgerToString(ingredients[1:])
    elif isinstance(ingredients[0], Lettuce):
        return ['lettuce'] + convertBurgerToString(ingredients[1:])
    elif isinstance(ingredients[0], Tomato):
        return ['tomato'] + convertBurgerToString(ingredients[1:])
    elif isinstance(ingredients[0], TopBun):
        return ['top'] + convertBurgerToString(ingredients[1:])
    else:
        return convertBurgerToString(ingredients[1:])