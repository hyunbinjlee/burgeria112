#Sources: from 112 course notes on conditionals, loops, animations
#https://www.cs.cmu.edu/~112/notes/notes-conditionals.html
#https://www.cs.cmu.edu/~112/notes/notes-loops.html
#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html

#No external sources, no external help, all images cited at the bottom of main.
#All code is my own.

from main import *
from foodclasses import * 
from servingfoodclasses import * 
import copy

#legality check if the item is legally placed into the machine by its bounds
#strings are returned if the legality check passes which then begins cooking
def isLegalPlacement(app, machine, potentialItem, event):
    #bounds check for grill
    if isinstance(machine, Grill) and \
    isinstance(potentialItem, Patty) and \
    app.grillX <= potentialItem.x <= app.grillX2 \
    and app.grillY <= potentialItem.y <= app.grillY2:
        return "grill"
    #bounds check for fryer
    elif isinstance(machine, Fryer) and \
    (isinstance(potentialItem, cutPotato)) and \
    app.fryerX <= potentialItem.x <= app.fryerX2 \
    and app.fryerY <= potentialItem.y <= app.fryerY2:
        return "fryer"
    #bounds check for cutting board
    elif isinstance(machine, CuttingBoard) and \
    app.cuttingBoardX <= potentialItem.x <= app.cuttingBoardX2 \
    and app.cuttingBoardY <= potentialItem.y <= app.cuttingBoardY2:
        return "cutting board"
    #bounds check for drink dispenser
    elif isinstance(machine, DrinkMachine) and \
    app.cokeX <= potentialItem.x <= app.cokeX2 \
    and app.cokeY <= potentialItem.y <= app.cokeY2:
        return "drink machine C"
    elif isinstance(machine, DrinkMachine) and \
    app.fantaX <= potentialItem.x <= app.fantaX2 \
    and app.fantaY <= potentialItem.y <= app.fantaY2:
        return "drink machine F"
    elif isinstance(machine, DrinkMachine) and \
    app.mountainDewX <= potentialItem.x <= app.mountainDewX2 \
    and app.mountainDewY <= potentialItem.y <= app.mountainDewY2:
        return "drink machine M"
    #bounds check for bag
    elif isinstance(machine, Bag) and \
    not isinstance(potentialItem, Order):
        if app.bagBoundX <= event.x <= app.bagBoundX2 \
            and app.bagBoundY <= event.y <= app.bagBoundY2:
                return "bagged"
    #bounds check for serving window
    elif isinstance(machine, Window) and \
    app.windowX <= potentialItem.x <= app.windowX2 \
    and app.windowY <= potentialItem.y <= app.windowY2:
        return "served"
    #bounds check for trash
    elif isinstance(machine, Trash) and \
    app.trashX <= potentialItem.x <= app.trashX2 and \
    app.trashY <= potentialItem.y <= app.trashY2:
        return "trashed"
    #returns false if legality check doesn't pass
    return False

#helpers for grill, fryer, cutting board, drink dispenser, bag
#checks if the machine is full, if not you can place another item

def fillGrill(app, machine, potentialItem):
    #if the grill isn't full, place another patty
    if 0 <= machine.numberOfPatties < 4:
        #cooking patty
        potentialItem.x = machine.spots[machine.numberOfPatties][0]
        potentialItem.y = machine.spots[machine.numberOfPatties][1]
        potentialItem.state = 0
        machine.addItem(potentialItem)
        machine.numberOfPatties += 1
    else: 
        #if the grill is full, you can't place another, reset to original pos
        potentialItem.x = app.pattyX
        potentialItem.y = app.pattyY
        app.itemPlaced.pop()

def fillFryer(app, machine, potentialItem):
    #if the fryer isn't full, place another potato
    if 0 <= machine.numberOfPotatoes < 2:
        #cooking potato
        potentialItem.x = machine.spots[machine.numberOfPotatoes][0]
        potentialItem.y = machine.spots[machine.numberOfPotatoes][1]
        potentialItem.state = 0
        machine.addItem(potentialItem)
        machine.numberOfPotatoes += 1
    else:
        #if the fryer is full, you can't place another, reset to original pos
        potentialItem.x = app.potatoX
        potentialItem.y = app.potatoY
        app.itemPlaced.pop()

def fillCuttingBoard(app, machine, potentialItem):
    #if the cutting board isn't full, place another lettuce, tomato, or potato
    if 0 <= machine.numberOfItems < 1:
        #cutting item
        potentialItem.x = machine.x
        potentialItem.y = machine.y
        potentialItem.state = 0
        machine.addItem(potentialItem)
        machine.numberOfItems += 1
    else:
        #if the cutting board is full, you can't place another, reset position
        for item in [UncutLettuce(app, app.uncutLettuceX, app.uncutLettuceY), \
        UncutTomato(app, app.uncutTomatoX, app.uncutTomatoY), \
            Potato(app, app.potatoX, app.potatoY)]:
            if potentialItem == item:
                #legality check
                potentialItem.x = item.x
                potentialItem.y = item.y
                app.itemPlaced.pop()

def fillDrinkMachine(app, machine, potentialItem, flavor):
    #if the drink machine isn't full, place another drink
    if 0 <= machine.numberOfDrinks < 1:
        potentialItem.x = machine.spots[flavor][0]
        potentialItem.y = machine.spots[flavor][1]
        potentialItem.fill = 0
        potentialItem.setFlavor(app, flavor)
        machine.addDrink(potentialItem)
        machine.numberOfDrinks += 1
    else:
        #if the machine is full, you can't place another, reset to original pos
        potentialItem.x = app.drinkX
        potentialItem.y = app.drinkY
        app.itemPlaced.pop()

def placeItemInBag(app, machine, potentialItem):
    #if the bag isn't full, place in bag
    illegalItems = [Bag, Window]
    if 0 <= machine.numberOfItems < 1:
        if potentialItem not in illegalItems:
            #place in bag
            machine.addToBag(app, potentialItem)

#serving mechanics helper:
#placing fulfilled orders in your bag
def createBag(app, event, cookers):
    if app.itemHeld == [] and \
    findDistance(app.bagX, app.bagY, event.x, event.y) <= 50:
    #if your hand is empty and you click on the bag you can serve:
        #create a new bag
        if cookers[4].items == []:
            cookers[4].items.append(Order (app, 0, 0))
        bag = copy.deepcopy(cookers[4].items[-1])
        cookers[4].items.pop()
        #add item to your bag
        bag.setImage(app.bagScaled)
        app.itemHeld.append(bag)
        app.itemIsPlaced = False
        app.itemIsPickedUp = True

#helper handling all placement of items
def startCooking(app, cookers, event):
    if app.itemPlaced != []:
        potentialItem = app.itemPlaced[-1]
    if cookers == []:
        return False
    elif isLegalPlacement(app, cookers[0], potentialItem, event) == "grill":
        fillGrill(app, cookers[0], potentialItem)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) == "fryer":
        fillFryer(app, cookers[0], potentialItem)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) \
    == "cutting board":
        fillCuttingBoard(app, cookers[0], potentialItem)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) \
    == "drink machine C":
        fillDrinkMachine(app, cookers[0], potentialItem, 0)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) \
    == "drink machine F":
        fillDrinkMachine(app, cookers[0], potentialItem, 1)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) \
    == "drink machine M":
        fillDrinkMachine(app, cookers[0], potentialItem, 2)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) == "bagged":
        placeItemInBag(app, cookers[0], potentialItem)
        #in the correct bounds of the bag
        if potentialItem in app.cookers[4].items[0].details:
            #if item is bagged, disappear from screen
            app.itemPlaced.remove(potentialItem)
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) == "served":
        #if the order is legal, you serve it
        if isinstance(potentialItem, Order):
            cookers[0].addOrder(potentialItem)
            #calculate score based on order accuracy
            cookers[0].calculateScore(app)
            #if item is served, disappear from screen
            app.itemPlaced.remove(potentialItem)
        else:
            #show cannot serve message if you try to serve a non-order
            potentialItem.img = app.cannotServe
        return True
    elif isLegalPlacement(app, cookers[0], potentialItem, event) == "trashed":
        #put items in the trash (remove it from the screen)
        if potentialItem in app.itemPlaced:
            app.itemPlaced.remove(potentialItem)
        if potentialItem in app.itemHeld:
            app.itemHeld.remove(potentialItem)
    return startCooking(app, cookers[1:], event)

def mousePressed(app, event):      
    cookers = app.cookers
    createBag(app, event, cookers)

    #item is to be placed 
    if app.itemIsPickedUp:
        app.itemIsPickedUp = False
        app.itemIsPlaced = True
        app.itemHeld[-1].x = event.x
        app.itemHeld[-1].y = event.y
        if not app.itemHeld[-1] in app.itemPlaced:
            app.itemPlaced.append(app.itemHeld[-1])
        app.itemHeld.pop()
        startCooking(app, cookers, event)

    else:
        #picking up item from default spot
        app.itemIsPickedUp = True
        app.itemIsPlaced = False
        
        #if an item is clicked on
        for sprite in app.toolbox:
            if abs(event.x - sprite[0]) < 30 and abs(event.y - sprite[1]) < 10:
                newSprite = copy.deepcopy(app.toolbox[sprite])
                newSprite.x = event.x
                newSprite.y = event.y
                app.itemHeld.append(newSprite)
                for instance in app.itemHeld:
                    if instance == None:
                        app.itemHeld.remove(None)
                return

        else:
            if app.itemPlaced == []:
                #None guard - for when you click on empty space
                app.itemIsPickedUp = False
                app.itemIsPlaced = False

            #pathfinding closest item if you don't directly click on an object
            closestDistance = 5
            closestItem = None
            for placedItem in app.itemPlaced:
                dist= findDistance(placedItem.x, placedItem.y, event.x, event.y)
                if closestItem == None or (dist < closestDistance):
                    closestDistance = dist
                    closestItem = placedItem
            if closestItem != None:
                app.itemHeld.append(closestItem)

def mouseMoved(app, event):
    #only activates when an item is currently in your possession
    if app.gameStarted == True:
        if app.itemIsPickedUp:
            app.itemHeld[-1].x = event.x
            app.itemHeld[-1].y = event.y

