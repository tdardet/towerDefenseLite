"""Starts Python 2.7 Tower Defense game by Tomas Dardet, requires Tkinter and
    Pillow (install using: pip install pillow)
"""
#Created by: Tomas J. Dardet Preston
#Copyright Tomas Dardet 2014

#This game was developed on Python 2.7.8

#It may work with other versions of python 2
#@!requires files(grayTower.png; grayTowerDisabled2.png;
#               redTower.png; redTowerDisabled1.png;
#               yellowTower.png; yellowTowerDisabled3.png;
#               whiteTower.png; whiteTowerDisabled4.png)


################################################################################
#############################  TERM PROJECT  ###################################
############################ TowerDefense LITE #################################
################################################################################
from Tkinter import *
import math
from PIL import ImageTk

global canvas
root = Tk()
border = 2
spaceUI = 5*42
rows = 16 ### I want to change this to len((x)Map) need it to be that way
cols = 15 ### same but with the len ((x)Map[0]) need it to be that way
cellWidth = 42
cellHeight = 42
canvasWidth = 2*border + cols*cellWidth + spaceUI
canvasHeight = 2*border + rows*cellHeight
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bd=0)
canvas.pack()
root.resizable(width=0, height=0)
root.canvas = canvas.canvas = canvas
class Struct: pass
canvas.data = Struct()
canvas.data.spaceUI = spaceUI
canvas.data.border = border
canvas.data.canvasWidth = canvasWidth
canvas.data.canvasHeight = canvasHeight
canvas.data.cellWidth = cellWidth
canvas.data.cellHeight = cellHeight
canvas.data.rows = rows
canvas.data.cols = cols

def init(map_index):
    # numbers indicate index of a list that will give the cell its visual
    # 0 = wall, 1 = path, 2 = start, 3 = end, 4 = tower1, 5 = tower2,
    # 6 = tower3, 7 = tower 4

    firstMap = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    secondMap = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    thirdMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    fourthMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [3, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                 [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]]

    # Initialize creep types by radii and adds three for health bar
    canvas.data.healthBar = 4
    orangeCircleCreep = ((4.5/8)*canvas.data.cellWidth)/2
        #normal
    redCircleCreep = ((3.5/8)*canvas.data.cellWidth)/2
        #fast
    blueCircleCreep = ((5.0/8)*canvas.data.cellWidth)/2
        #large

    ## Map Information
    canvas.data.maps = [firstMap, secondMap, thirdMap, fourthMap]
        #stores maps
    canvas.data.mapStartDirection = [[0, 1], [0, 1], [1, 0], [0, -1]]
         #[[dx, dy]]
    canvas.data.mapIndex = map_index
        # starts the game with the first Map
    canvas.data.currentMap = canvas.data.maps[canvas.data.mapIndex]
    canvas.data.cellColor = ["darkgreen", "black", "limegreen", "tomato",
                             "", "", "", "", "", ""]
        # extra values for range issues
    canvas.data.cellBorderColor = ["green", "black", "green", "green",
                                   "", "", "", "", ""]
        #extra values for range issues
    canvas.data.backgroundColorFill = "black"
    canvas.data.uiBorderColor = "black"
    canvas.data.buttonColor = "red"

    ## Creep Information
    canvas.data.creepStartDirection = (
        canvas.data.mapStartDirection[canvas.data.mapIndex])
        # sets starting value for creep
    canvas.data.creeps = []
        # creeps in game at the moment
        #stores[[cX, cY, dx, dy,
        #       radius, speed, color, health, score, money, timesMoved]]
        # initialized with makeNewCreep
    canvas.data.creepRadiusList = [orangeCircleCreep, redCircleCreep,
                                   blueCircleCreep]
        # Number indicates type of creep and its radius
    canvas.data.creepColorList = ["orange", "red", "blue"]
        # Indicates fill by index
    canvas.data.creepSpeedList = [4, 6, 3]
        # stores speed according to index
    canvas.data.creepInitialHealthList = [125, 45, 350]
        # damage able to take
    canvas.data.creepScoreList = [10, 12, 15]
        # score you get for killing
    canvas.data.creepKillMoneyList = [1, 2, 3]
        # money you get for killing
    #canvas.data.creepTypeIndex = 0 ## using waves now
        # called by makeNewCreep a set number of times
        #in order to make diff types of creeps according to info regarding Wave
        ## makeNewCreep should callc creep NUmber per wave list
        # posibility for randomness =
            # canvas.data.totalCreepType = len(canvas.data.creepRadiusList)
        # not used anymore = canvas.data.creepCenterYList = []
        # not used anymore = canvas.data.creepCenterXList = [] ###

    ## Tower Information ########fix
    canvas.data.towers = []
    canvas.data.towerColorOneList = ["red", "gray", "orange", "white"]
    canvas.data.towerColorTwoList = ["blue", "green", "purple", "blue"]
    canvas.data.towerSizeFactorOneList = [20, 20, 20, 20]
    canvas.data.towerSizeFactorTwoList = [5, 5, 4, 6]
    canvas.data.pressedTowerCost = [10, 10000, 10000, 50]
    canvas.data.towerName = ["Quick Rectangle Tower", "Diamond Fury Tower",
                             "Tri Tower", "Super Star Tower"]
    canvas.data.towerInfo = ["Pretty Cheap..",
                             "Out of Commision\nDon't use",
                             "Out of Commision\nDon't use",
                             "Boss Tower"]
    canvas.data.towerDamage = [5, 15, 8, 25]
    canvas.data.fireRate = ["Fast", "Slow", "Slow", "Fast"]
    canvas.data.towerRange = [65, 50, 75, 120]
    canvas.data.firstTowerShotList = []
    canvas.data.secondTowerShotList = []
    canvas.data.thirdTowerShotList = []
    canvas.data.fourthTowerShotList = []
    canvas.data.speedShot = [15, 10, 0, 13]
    canvas.data.shotColors = ["yellow", "gray", "purple", "blue"]
    canvas.data.pressedTowerIndex = None ##

    ##Wave Information
    canvas.data.creepSpacingCounter = 0
    canvas.data.currentWaveIndex = 0
    canvas.data.creepSpacingFactorPerWave = [10, 10, 8, 10, 10, 10, 10, 10, 10,
                                             10, 5, 8, 10, 10, 5, 6, 3, 4, 6, 7,
                                             5]
        # higher values = more time between creeps
    canvas.data.creepNumberPerWaveList = [[5, 0, 0], [6, 0, 0], [0, 5, 0],
                                          [0, 0, 5], [5, 5, 0], [0, 5, 5],
                                          [7, 7, 0], [6, 6, 6], [0, 15, 0],
                                          [0, 0, 15], [15, 0, 5], [10, 5, 5],
                                          [13, 10, 8], [20, 5, 5], [0, 30, 0],
                                          [10, 25, 10], [15, 15, 15],
                                          [20, 15, 15], [0, 40, 0], [10, 0, 40],
                                          [40, 40, 40]]
        # 2dlist, rows = wave, cols = creep type number
    canvas.data.creepMakingList = [] # makes a list of creepTypeIndeces
    canvas.data.makeCreep = 0 ###

    ## Images for tower UI
    canvas.data.redTower = ImageTk.PhotoImage(file="redTower.png")
    canvas.data.redTowerDisabled = ImageTk.PhotoImage(file="redTowerDisabled1.png")
    canvas.data.yellowTower = ImageTk.PhotoImage(file="yellowTower.png")
    canvas.data.yellowTowerDisabled = ImageTk.PhotoImage(
        file="yellowTowerDisabled3.png")
    canvas.data.grayTower = ImageTk.PhotoImage(file="grayTower.png")
    canvas.data.grayTowerDisabled = ImageTk.PhotoImage(file="grayTowerDisabled2.png")
    canvas.data.whiteTower = ImageTk.PhotoImage(file="whiteTower.png")
    canvas.data.whiteTowerDisabled = ImageTk.PhotoImage(file="whiteTowerDisabled4.png")
    canvas.data.imageTower = [canvas.data.redTower, canvas.data.grayTower,
                              canvas.data.yellowTower, canvas.data.whiteTower]
    canvas.data.disabledTower = [canvas.data.redTowerDisabled,
                                 canvas.data.grayTowerDisabled,
                                 canvas.data.yellowTowerDisabled,
                                 canvas.data.whiteTowerDisabled]
    ## UI coords
    canvas.data.spaceBorderUI = 5
    canvas.data.boxColorUI = "black"

    ##Game Modifiers
    canvas.data.pauseGame = True
    canvas.data.gameOver = False
    canvas.data.splashScreen = True
    canvas.data.score = 0
    canvas.data.lives = 10
    canvas.data.money = 30
    canvas.data.waveButtonPressed = False
    canvas.data.waveSpacingCounter = 0
    canvas.data.timeBetweenWaves = 350
    canvas.data.printNoMoney = False
    canvas.data.timeBetweenShots = 100 ###
    canvas.data.speedButton = False

################################################################################
############################# Interface events   ###############################
################################################################################

def mouse_pressed(event):
    doMousePressedTowerPlacement(event)
    doMousePressedWaveButton(event)
    doMousePressedTowerMaker(event)

def doMousePressedTowerPlacement(event):
    xAjust = canvas.data.spaceUI
    yAjust = canvas.data.border
    cellH = canvas.data.cellHeight
    cellW = canvas.data.cellWidth
    pressedTowerIndex = canvas.data.pressedTowerIndex
    if pressedTowerIndex == None:
        return
    pressedTowerCost = canvas.data.pressedTowerCost[pressedTowerIndex]
    for row in xrange(len(canvas.data.currentMap)):
        for col in xrange(len(canvas.data.currentMap[0])):
            if ((event.x < (col+1)*cellW + xAjust)
                    and (event.x > col*cellW + xAjust) # where you click
                    and (event.y < (row+1)*cellH + yAjust) #square check
                    and (event.y > row*cellH + yAjust)
                    and canvas.data.currentMap[row][col] == 0): #only on walls
                if canvas.data.money >= pressedTowerCost:
                    makeNewTower(row, col, pressedTowerIndex)
                    canvas.data.currentMap[row][col] = pressedTowerIndex + 4
                        # +4 bcause towers are from 4 onwards
                    canvas.data.money -= pressedTowerCost
                    canvas.data.printNoMoney = False
                else:
                    canvas.data.printNoMoney = True

def doMousePressedWaveButton(event):
    fix = 7
    x0 = canvas.data.spaceBorderUI
    y0 = (9)*canvas.data.cellHeight/2 - fix
    x1 = canvas.data.spaceUI - canvas.data.spaceBorderUI
    y1 = y0 + canvas.data.cellHeight + fix
    if event.x > x0 and event.x < x1 and event.y > y0 and event.y < y1:
        canvas.data.waveSpacingCounter = 0
        canvas.data.waveButtonPressed = True

def doMousePressedTowerMaker(event):
    imageSpacing = 60
    x0 = canvas.data.spaceBorderUI + 3
    x1 = x0 + 43
    for i in xrange(len(canvas.data.imageTower)):
        y0 = canvas.data.canvasHeight/1.7 + imageSpacing*i + x0 - 20
        y1 = y0 + 45
        if event.x > x0 and event.x < x1 and event.y > y0 and event.y < y1:
            if canvas.data.pressedTowerIndex == i:
                canvas.data.pressedTowerIndex = None
            else:
                canvas.data.pressedTowerIndex = i

def keyPressed(event):
    if not canvas.data.gameOver:
        if canvas.data.splashScreen and event.keysym == "Return":
            canvas.data.splashScreen = False
            canvas.data.pauseGame = False
        if not canvas.data.pauseGame and not canvas.data.splashScreen:
            doKeyPressedTowerMaker(event)
            if event.char == ("w"):
                canvas.data.waveSpacingCounter = 0
                canvas.data.waveButtonPressed = True
            if event.char == ("s"):
                canvas.data.speedButton = not canvas.data.speedButton
        if (event.char == "p") and (not canvas.data.splashScreen):
            pauseGame()
        if canvas.data.pauseGame and (event.char == "m"):
            newMap = canvas.data.mapIndex + 1
            totalMaps = len(canvas.data.maps)
            init(newMap % totalMaps)
    elif event.char == "r":
        init(canvas.data.mapIndex)

def doKeyPressedTowerMaker(event):
    if event.keysym == "1":
        if canvas.data.pressedTowerIndex != 0:
            canvas.data.pressedTowerIndex = 0
        else:
            canvas.data.pressedTowerIndex = None
    elif event.keysym == "2":
        if canvas.data.pressedTowerIndex != 1:
            canvas.data.pressedTowerIndex = 1
        else:
            canvas.data.pressedTowerIndex = None
    elif event.keysym == "3":
        if canvas.data.pressedTowerIndex != 2:
            canvas.data.pressedTowerIndex = 2
        else:
            canvas.data.pressedTowerIndex = None
    elif event.keysym == "4":
        if canvas.data.pressedTowerIndex != 3:
            canvas.data.pressedTowerIndex = 3
        else:
            canvas.data.pressedTowerIndex = None

def pauseGame():
    canvas.data.pauseGame = not canvas.data.pauseGame

################################################################################
################################  Movement #####################################
################################################################################

def moveCreeps(creeps):
    #creeps =[[cX, cY, dx, dy, radius, speed, color, health, score, timesMoved]]
    for creep in xrange(len(creeps)):
        cX = creeps[creep][0]
        cY = creeps[creep][1]
        dx = creeps[creep][2]
        dy = creeps[creep][3]
        r = creeps[creep][4]
        color = creeps[creep][6]
        moveCreep(cX, cY, dx, dy, r, color, creep, creeps)
    removeCreep()
    redrawAll()

def moveCreep(cX, cY, dx, dy, radius, color, index, creeps): ## take color out
    ##creeps=[[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    negativeX = -dx
    negativeY = -dy
    if isMoveLegal(cX, cY, dx, dy, radius):
        creeps[index][0] += dx
        creeps[index][1] += dy
        creeps[index][2] = dx
        creeps[index][3] = dy
        creeps[index][10] += creeps[index][5]

    else:
        if (isMoveLegal(cX, cY, dy, dx, radius) and
                minDistanceFromWall(cX, cY, dy, dx, radius)): #move later check
            creeps[index][0] += dy #move center x
            creeps[index][1] += dx #movecenter y
            creeps[index][2] = dy # save movement value dx
            creeps[index][3] = dx  #save movement value dy
            creeps[index][10] += creeps[index][5]

        elif (isMoveLegal(cX, cY, negativeY, negativeX, radius) and
              minDistanceFromWall(cX, cY, negativeY, negativeX, radius)):
            creeps[index][0] += negativeY
            creeps[index][1] += negativeX
            creeps[index][2] = negativeY
            creeps[index][3] = negativeX
            creeps[index][10] += creeps[index][5]


    # you can never move backwards


def minDistanceFromWall(cX, cY, dx, dy, radius):
    minDistance = 3 # 3 movements, don't change unless you change creep speed
    timesMoved = 0
    check = 0
    x = cX
    y = cY
    while check < minDistance:
        check += 1
        if isMoveLegal(x, y, dx, dy, radius):
            timesMoved += 1
            x += dx
            y += dy
    return minDistance == timesMoved

def isMoveLegal(cX, cY, dx, dy, radius):
    newXCenter = cX + dx
    newYCenter = cY + dy
    healthBar = canvas.data.healthBar
    x0Creep = newXCenter - radius - healthBar
    x1Creep = newXCenter + radius + healthBar
    y0Creep = newYCenter - radius - healthBar
    y1Creep = newYCenter + radius + healthBar
    for row in xrange(len(canvas.data.currentMap)):
        for col in xrange(len(canvas.data.currentMap[0])):
            if (canvas.data.currentMap[row][col] == 0 or
                    canvas.data.currentMap[row][col] > 3):
                x0 = canvas.data.spaceUI + canvas.data.cellWidth*col
                x1 = x0 + canvas.data.cellWidth
                y0 = canvas.data.border + canvas.data.cellHeight*row
                y1 = y0 + canvas.data.cellHeight
                if (rectanglesIntersect(x0, y0, x1, y1,
                                        x0Creep, y0Creep, x1Creep, y1Creep)):
                    return False
    return True


def rectanglesIntersect(x01, y01, x11, y11, x02, y02, x12, y12):
    return (x01 <= x12) and (x11 >= x02) and (y01 <= y12) and (y11 >= y02)

################################################################################
############################## All Creep Stuff #################################
################################################################################

def removeCreep():
    #creeps =[[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    discardCreeps = []
    leftEdge = canvas.data.spaceUI
    rightEdge = canvas.data.canvasWidth
    bottomEdge = canvas.data.canvasHeight
    for creep in xrange(len(canvas.data.creeps)):
        cX = canvas.data.creeps[creep][0]
        cY = canvas.data.creeps[creep][1]
        radius = canvas.data.creeps[creep][4]
        health = canvas.data.creeps[creep][7]
        score = canvas.data.creeps[creep][8]
        money = canvas.data.creeps[creep][9]
        if ((int(cX) <= radius + leftEdge) or (int(cY) <= radius)
                or (int(cX) >= rightEdge - radius) or
                (int(cY) >= bottomEdge - radius)):
            discardCreeps.append(canvas.data.creeps[creep])
            canvas.data.lives -= 1
        elif health <= 0:
            discardCreeps.append(canvas.data.creeps[creep])
            canvas.data.score += score
            canvas.data.money += money
    for remove in xrange(len(discardCreeps)):
        canvas.data.creeps.remove(discardCreeps[remove])
    if canvas.data.lives < 1:
        canvas.data.gameOver = True


def drawCreeps(creeps): #takes in 2dList of creeps
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,timesMoved]]
    if len(creeps) > 0:
        for creep in xrange(len(creeps)):
            cX = creeps[creep][0]
            cY = creeps[creep][1]
            radius = creeps[creep][4]
            color = creeps[creep][6]
            health = creeps[creep][7]
            canvas.create_oval(cX-radius, cY-radius, cX+radius, cY+radius,
                               fill=color)
            canvas.create_text(cX -radius, cY - radius,
                               text=str(health), fill=color,
                               font="Times 6", anchor=SW)

def makeWaveCreeps(creepList, count):
    if (len(creepList)-1) < count:
        return None
    return creepList[count]

def makeWaveCreepList(creepQuantity):
    canvas.data.creepMakingList = []
    countIndex = 0
    for index in xrange(len(creepQuantity)):
        while countIndex < creepQuantity[index]:
            canvas.data.creepMakingList.append(index)
            countIndex += 1
        countIndex = 0
    return canvas.data.creepMakingList

def makeNewCreepAtStart(indexOfTypeOfCreep, wave):
    # searching for 2 in the 2dList because it denotes the start
    if indexOfTypeOfCreep == None:
        return
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            if canvas.data.currentMap[row][col] == 2:
                makeNewCreep(row, col, indexOfTypeOfCreep, wave)

def makeNewCreep(row, col, index, wave):
    #finds the center of the row and column for adjustment
    ##creepIndex = canvas.data.currentCreepIndex
    colCenter = (2*col + 1)/2.0
    rowCenter = (2*row + 1)/2.0
    cX = canvas.data.spaceUI + canvas.data.cellWidth*colCenter #center of col
    cY = canvas.data.border + canvas.data.cellHeight*rowCenter #center of row
    speed = canvas.data.creepSpeedList[index]
    dx = canvas.data.creepStartDirection[0]* speed
    dy = canvas.data.creepStartDirection[1]* speed
    radius = canvas.data.creepRadiusList[index]
    color = canvas.data.creepColorList[index]
    health = canvas.data.creepInitialHealthList[index]+ wave*50
    score = canvas.data.creepScoreList[index] + wave*5
    money = canvas.data.creepKillMoneyList[index]
    timesMoved = 0
    canvas.data.creeps.append([cX, cY, dx, dy, radius,
                               speed, color, health, score, money, timesMoved])

################################################################################
##############################  Shooting #######################################
################################################################################

def towersThatShoot():
    for row in xrange(len(canvas.data.currentMap)):
        for col in xrange(len(canvas.data.currentMap[0])):
            cX = (2*col +1)*canvas.data.cellWidth/2 + canvas.data.spaceUI
            cY = (2*row +1)*canvas.data.cellHeight/2 + canvas.data.border
            if canvas.data.currentMap[row][col] == 4:
                makeFirstTowerShots(cX, cY, 0)
            #elif canvas.data.currentMap[row][col] == 5:
                #makeSecondTowerShots(cX, cY, 1)
            #elif canvas.data.currentMap[row][col] == 6:
                #makeThirdTowerShots(cX, cY, 2)
            elif canvas.data.currentMap[row][col] == 7:
                makeFourthTowerShots(cX, cY, 3)

def makeFirstTowerShots(cX0, cY0, towerType):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    towerRange = canvas.data.towerRange[towerType]
    listCreep = []
    listCreepDistance = []
    for creep in xrange(len(canvas.data.creeps)):
        cX = canvas.data.creeps[creep][0]
        cY = canvas.data.creeps[creep][1]
        if math.sqrt((cX0 - cX)**2+(cY0 - cY)**2) < towerRange:
            listCreep.append(creep)
            listCreepDistance.append(canvas.data.creeps[creep][10])
    if len(listCreepDistance) != 0:
        creepIndex = findFurthestCreepIndex(listCreep, listCreepDistance)
        makeTowerShot(cX0, cY0, towerType, creepIndex)

def makeTowerShot(cX, cY, towerType, creepIndex):
    if creepIndex == None:
        return
    radiusOfShot = canvas.data.towerSizeFactorTwoList[towerType]
    destinationX = canvas.data.creeps[creepIndex][0]
    destinationY = canvas.data.creeps[creepIndex][1]
    normalizeVectorFactor = math.sqrt((destinationX-cX)**2 +
                                      (destinationY - cY)**2)
    speedOfShot = canvas.data.speedShot[towerType]
    dx = speedOfShot*(destinationX - cX)/normalizeVectorFactor
    dy = speedOfShot*(destinationY - cY)/normalizeVectorFactor
    damageShot = canvas.data.towerDamage[towerType]
    colorShot = canvas.data.shotColors[towerType]
    if towerType == 0:
        canvas.data.firstTowerShotList.append([cX, cY, radiusOfShot, dx, dy,
                                               destinationX, destinationY,
                                               damageShot, colorShot])
    elif towerType == 1:
        canvas.data.secondTowerShotList.append([cX, cY, radiusOfShot, dx, dy,
                                                destinationX, destinationY,
                                                damageShot, colorShot])
    elif towerType == 2:
        canvas.data.thirdTowerShotList.append([cX, cY, radiusOfShot, dx, dy,
                                               destinationX, destinationY,
                                               damageShot, colorShot])
    elif towerType == 3:
        canvas.data.fourthTowerShotList.append([cX, cY, radiusOfShot, dx, dy,
                                                destinationX, destinationY,
                                                damageShot, colorShot])

def findFurthestCreepIndex(listIndeces, listDistances):
    listDistanceCopy = listDistances + []
    largestDistance = 0
    largestDistanceIndex = None
    for dist in xrange(len(listDistances)):
        if listDistanceCopy[dist] > largestDistance:
            largestDistance = listDistanceCopy[dist]
            largestDistanceIndex = listIndeces[dist]
    return largestDistanceIndex

#### I was going to implement these but couldn't
'''
def makeSecondTowerShots(cX0,cY0,towerType):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    towerRange = canvas.data.towerRange[towerType]
    listCreep = []
    listCreepDistance = []
    for creep in xrange(len(canvas.data.creeps)):
        cX = canvas.data.creeps[creep][0]
        cY = canvas.data.creeps[creep][1]
        if math.sqrt((cX0 - cX)**2+(cY0 - cY)**2) < towerRange:
            listCreep.append(creep)
            listCreepDistance.append(canvas.data.creeps[creep][10])
    if (len(listCreepDistance) != 0):
        creepIndex = findFurthestCreepIndex(listCreep,listCreepDistance)
        makeTowerShot(cX0,cY0,towerType,creepIndex)
                   
def makeThirdTowerShots(cX0,cY0,towerType):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    towerRange = canvas.data.towerRange[towerType]
    listCreep = []
    listCreepDistance = []
    for creep in xrange(len(canvas.data.creeps)):
        cX = canvas.data.creeps[creep][0]
        cY = canvas.data.creeps[creep][1]
        if math.sqrt((cX0 - cX)**2+(cY0 - cY)**2) < towerRange:
            listCreep.append(creep)
            listCreepDistance.append(canvas.data.creeps[creep][10])
    if (len(listCreepDistance) != 0):
        creepIndex = findFurthestCreepIndex(listCreep,listCreepDistance)
        makeTowerShot(cX0,cY0,towerType,creepIndex)
'''
def makeFourthTowerShots(cX0, cY0, towerType):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    towerRange = canvas.data.towerRange[towerType]
    listCreep = []
    listCreepDistance = []
    for creep in xrange(len(canvas.data.creeps)):
        cX = canvas.data.creeps[creep][0]
        cY = canvas.data.creeps[creep][1]
        if math.sqrt((cX0 - cX)**2+(cY0 - cY)**2) < towerRange:
            listCreep.append(creep)
            listCreepDistance.append(canvas.data.creeps[creep][10])
    if len(listCreepDistance) != 0:
        creepIndex = findFurthestCreepIndex(listCreep, listCreepDistance)
        makeTowerShot(cX0, cY0, towerType, creepIndex)

def drawFourthTowerShots(shotList):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    #type of tower is 0 because it is the first tower
    if len(shotList) < 1:
        return
    for shot in xrange(len(shotList)):
        r = shotList[shot][2]
        cX = shotList[shot][0]
        cY = shotList[shot][1]
        x0 = cX - r
        y0 = cY + 2*r/3 -1
        y00 = cY - 2*r/3 + 1
        x1 = cX
        y1 = cY - r - 1
        y11 = cY +r+1
        x2 = cX + r
        y2 = cY + 2*r/3 +1
        y22 = cY - 2*r/3 +1
        color = shotList[shot][8]
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill=color)
        canvas.create_polygon(x0, y00, x1, y11, x2, y22, fill=color)

def moveFourthShots(fourthShotList):
    for shot in xrange(len(fourthShotList)):
        cX = fourthShotList[shot][0]
        cY = fourthShotList[shot][1]
        dx = fourthShotList[shot][3]
        dy = fourthShotList[shot][4]
        canvas.data.fourthTowerShotList[shot][0] += dx
        canvas.data.fourthTowerShotList[shot][1] += dy
    removeFourthShotsTest()

def removeFourthShotsTest():
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    #type of tower is 0 because it is the first tower
    discardShots = []
    shotList = canvas.data.fourthTowerShotList
    safety = 10
    topEdge = safety
    leftEdge = canvas.data.spaceUI + safety
    rightEdge = canvas.data.canvasWidth - safety
    bottomEdge = canvas.data.canvasHeight - safety
    for shot in xrange(len(canvas.data.fourthTowerShotList)):
        cX = canvas.data.fourthTowerShotList[shot][0]
        cY = canvas.data.fourthTowerShotList[shot][1]
        radius = canvas.data.fourthTowerShotList[shot][2]
        damage = canvas.data.fourthTowerShotList[shot][7]
        destinationX = canvas.data.fourthTowerShotList[shot][5]
        destinationY = canvas.data.fourthTowerShotList[shot][6]
        if((int(cX) <= leftEdge) or (int(cY) <= topEdge) or
           (int(cX) >= rightEdge) or (int(cY) >= bottomEdge)):
            discardShots.append(canvas.data.fourthTowerShotList[shot])
        for creep in xrange(len(canvas.data.creeps)):
            if (collidedCircle(shot, creep, canvas.data.fourthTowerShotList,
                               canvas.data.creeps) and
                    (canvas.data.fourthTowerShotList[shot] not in
                     discardShots)):
                discardShots.append(canvas.data.fourthTowerShotList[shot])
    if len(discardShots) == 0:
        return
    for shot1 in discardShots:
        canvas.data.fourthTowerShotList.remove(shot1)

def moveFirstShots(firstShotList):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    #type of tower is 0 because it is the first tower
    for shot in xrange(len(firstShotList)):
        cX = firstShotList[shot][0]
        cY = firstShotList[shot][1]
        dx = firstShotList[shot][3]
        dy = firstShotList[shot][4]
        canvas.data.firstTowerShotList[shot][0] += dx
        canvas.data.firstTowerShotList[shot][1] += dy
    removeFirstShotsTest()

def drawSecondTowerShots(shotList):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,money,timesMoved]]
    # canvas.data.secondTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    #type of tower is 0 because it is the first tower
    if len(shotList) < 1:
        return
    for shot in xrange(len(shotList)):
        x0 = shotList[shot][0] - shotList[shot][2]
        y0 = shotList[shot][1] - shotList[shot][2]
        x1 = shotList[shot][0] + shotList[shot][2]
        y1 = shotList[shot][1] + shotList[shot][2]
        color = shotList[shot][8]
        canvas.create_oval(x0, y0, x1, y1, fill=color)

def makeNewTower(row, col, indexOfTower): # make the list -
                        #towers to draw them later with drawTowers
                                        # changes map values

    #canvas.data.currentMap[row][col] += indexOfTower + 4
        # + 4 because tower values start on 4 for the map
    colorOne = canvas.data.towerColorOneList[indexOfTower]
    colorTwo = canvas.data.towerColorTwoList[indexOfTower]
    sizeFactorOne = canvas.data.towerSizeFactorOneList[indexOfTower]
    sizeFactorTwo = canvas.data.towerSizeFactorTwoList[indexOfTower]
    canvas.data.towers.append([row, col, colorOne, colorTwo, sizeFactorOne,
                               sizeFactorTwo, indexOfTower])

def drawFirstTowerShots(shotList):
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    #type of tower is 0 because it is the first tower
    if len(shotList) < 1:
        return
    for shot in xrange(len(shotList)):
        x0 = shotList[shot][0] - shotList[shot][2]
        y0 = shotList[shot][1] - shotList[shot][2]
        x1 = shotList[shot][0] + shotList[shot][2]
        y1 = shotList[shot][1] + shotList[shot][2]
        color = shotList[shot][8]
        #color = "yellow"
        canvas.create_oval(x0, y0, x1, y1, fill=color)

def removeFirstShotsTest():
    ## creeps = [[cX,cY,dx,dy,radius,speed,color,health,score,timesMoved]]
    # canvas.data.firstTowerShotList = [[cX,cY,radius,dx,dy,destinationX,
    #                                       destinationY,damageShot,colorShot]]
    #type of tower is 0 because it is the first tower
    discardShots = []
    shotList = canvas.data.firstTowerShotList
    safety = 10
    topEdge = safety
    leftEdge = canvas.data.spaceUI + safety
    rightEdge = canvas.data.canvasWidth - safety
    bottomEdge = canvas.data.canvasHeight - safety
    for shot in xrange(len(canvas.data.firstTowerShotList)):
        cX = canvas.data.firstTowerShotList[shot][0]
        cY = canvas.data.firstTowerShotList[shot][1]
        radius = canvas.data.firstTowerShotList[shot][2]
        damage = canvas.data.firstTowerShotList[shot][7]
        destinationX = canvas.data.firstTowerShotList[shot][5]
        destinationY = canvas.data.firstTowerShotList[shot][6]
        if ((int(cX) <= leftEdge) or (int(cY) <= topEdge) or
                (int(cX) >= rightEdge) or (int(cY) >= bottomEdge)):
            discardShots.append(canvas.data.firstTowerShotList[shot])
        for creep in xrange(len(canvas.data.creeps)):
            if (collidedCircle(shot, creep, canvas.data.firstTowerShotList,
                               canvas.data.creeps) and
                    (canvas.data.firstTowerShotList[shot] not in discardShots)):
                discardShots.append(canvas.data.firstTowerShotList[shot])
    if len(discardShots) == 0:
        return
    for shot1 in discardShots:
        canvas.data.firstTowerShotList.remove(shot1)

def collidedCircle(shot, creep, shotList, creeps):
    cXShot = shotList[shot][0]
    cYShot = shotList[shot][1]
    radiusShot = shotList[shot][2]
    damageShot = shotList[shot][7]
    destinationX = shotList[shot][5]
    destinationY = shotList[shot][6]
    cXCreep = canvas.data.creeps[creep][0]
    cYCreep = canvas.data.creeps[creep][1]
    radiusCreep = canvas.data.creeps[creep][4]
    return collidedCircleHelper((cXShot - cXCreep),
                                (cYShot - cYCreep),
                                (radiusShot + radiusCreep), creep, damageShot)

def collidedCircleHelper(x, y, d, creep, damageShot):
    if math.sqrt((x**2 + y**2)) <= d:
        canvas.data.creeps[creep][7] -= damageShot
        return True
    return False

def drawTowers(towers):
    if len(towers) > 0:
        for tower in xrange(len(towers)):
            row = towers[tower][0]
            col = towers[tower][1]
            colorOne = towers[tower][2]
            colorTwo = towers[tower][3]
            sizeFactorOne = towers[tower][4]
            sizeFactorTwo = towers[tower][5]
            towerType = towers[tower][6]
            drawTowerInGame(row, col, colorOne, colorTwo,
                            sizeFactorOne, sizeFactorTwo, towerType)

def drawTowerInGame(row, col, color1, color2,
                    sizeFactorOne, sizeFactorTwo, towerType):
    xCenterFactor = 1.0*canvas.data.cellWidth/2
    yCenterFactor = 1.0*canvas.data.cellHeight/2
    addToX = canvas.data.spaceUI
    addToY = canvas.data.border
    cX = (1 + 2*col)*xCenterFactor + addToX
    cY = (1 + 2*row)*yCenterFactor + addToY
    drawCell(row, col, 0) # to draw the wall behind the tower
    if towerType == 0:
        canvas.create_rectangle(cX-sizeFactorOne, cY - sizeFactorOne,
                                cX + sizeFactorOne, cY + sizeFactorOne,
                                fill=color1)
        canvas.create_rectangle(cX-sizeFactorTwo, cY - sizeFactorTwo,
                                cX + sizeFactorTwo, cY + sizeFactorTwo,
                                fill=color2)
        # rectangle with rectangle inside - shoots quick circles
    elif towerType == 1:
        canvas.create_polygon(cX-sizeFactorOne, cY, cX, cY-sizeFactorOne,
                              cX + sizeFactorOne, cY,
                              cX, cY + sizeFactorOne, fill=color1)
        canvas.create_polygon(cX-sizeFactorTwo, cY, cX, cY-sizeFactorTwo,
                              cX + sizeFactorTwo, cY,
                              cX, cY+ sizeFactorTwo, fill=color2)
        # diamond Shaped - "shoots" (extends outwards) to hit area around it.
    elif towerType == 2:
        canvas.create_polygon(cX-sizeFactorOne, cY + sizeFactorOne - 6,
                              cX, cY-sizeFactorOne,
                              cX + sizeFactorOne, cY + sizeFactorOne - 6,
                              fill=color1)
        canvas.create_oval(cX - sizeFactorTwo, cY - sizeFactorTwo,
                           cX + sizeFactorTwo, cY + sizeFactorTwo,
                           fill=color2)
         # triangle with cicle inside - shoots lazers
    elif towerType == 3:
        canvas.create_polygon(cX - sizeFactorOne,
                              cY + sizeFactorOne*(2.0/3) - 3, cX,
                              cY-sizeFactorOne, cX + sizeFactorOne,
                              cY + sizeFactorOne*(2.0/3) - 3, fill=color1)
        canvas.create_polygon(cX - sizeFactorOne,
                              cY - sizeFactorOne*(2.0/3) + 3, cX,
                              cY + sizeFactorOne, cX + sizeFactorOne,
                              cY - sizeFactorOne*(2.0/3) + 3, fill=color1)
        canvas.create_polygon(cX - sizeFactorTwo,
                              cY + sizeFactorTwo*(2.0/3) - 1, cX,
                              cY - sizeFactorTwo - 1, cX + sizeFactorTwo,
                              cY + sizeFactorTwo*(2.0/3) - 1, fill=color2)
        canvas.create_polygon(cX - sizeFactorTwo,
                              cY - sizeFactorTwo*(2.0/3) + 1, cX,
                              cY + sizeFactorTwo + 1, cX + sizeFactorTwo,
                              cY - sizeFactorTwo*(2.0/3) + 1, fill=color2)
         # two triangles making a star with star inside-- shoots stars
                # stars explode for splash damage

##############################################################################
################################# Timer Fired ################################
##############################################################################

def timerFired():
    if not canvas.data.pauseGame and not canvas.data.gameOver:
        if canvas.data.waveButtonPressed:
            if ((len(canvas.data.creepNumberPerWaveList)) >
                    canvas.data.currentWaveIndex):
                wave = canvas.data.currentWaveIndex
                creepQuantity = canvas.data.creepNumberPerWaveList[wave]
                creepSpace = canvas.data.creepSpacingFactorPerWave[wave]
                creepMake = canvas.data.makeCreep
                creepCount = canvas.data.creepSpacingCounter
                waveCount = canvas.data.waveSpacingCounter
                waveSpace = canvas.data.timeBetweenWaves
                listUse = makeWaveCreepList(creepQuantity)
                if ((canvas.data.creepSpacingCounter % creepSpace == 0) and
                        canvas.data.waveSpacingCounter == 0):
                    if makeWaveCreeps(listUse, canvas.data.makeCreep) != None:
                        makeNewCreepAtStart(makeWaveCreeps(
                            listUse, canvas.data.makeCreep), wave)
                        canvas.data.makeCreep += 1
                    elif makeWaveCreeps(listUse, canvas.data.makeCreep) == None:
                        if (len(canvas.data.creepNumberPerWaveList)) > wave:
                            #checks if there is another wave
                            canvas.data.currentWaveIndex += 1
                            canvas.data.waveSpacingCounter = 1
                            canvas.data.makeCreep = 0 # resets for next wave
                    canvas.data.creepSpacingCounter += 1
                else: # waveCount has changed to 1 so
                      #previous doesnt run till it is 0 again
                    if waveCount % waveSpace == 0:
                        canvas.data.waveSpacingCounter = 0
                    else:
                        canvas.data.waveSpacingCounter += 1
                    canvas.data.creepSpacingCounter += 1
            else:
                if len(canvas.data.creeps) == 0:
                    canvas.data.gameOver = True
            towersThatShoot()
            moveFirstShots(canvas.data.firstTowerShotList)
            moveFourthShots(canvas.data.fourthTowerShotList)
            moveCreeps(canvas.data.creeps)

    redrawAll()
    if canvas.data.speedButton:
        delay = 1 # milliseconds
    else:
        delay = 25 # milliseconds
    canvas.after(delay, timerFired) # pause for delay, call timerFired again

########################################################################
###################### Drawing Background/Map/UI########################
###################### RedrawAll and drawGame ##########################
########################################################################

def drawBackground():
    borderAdjust = 2
    canvas.create_rectangle(borderAdjust, 0,
                            canvas.data.canvasWidth,
                            canvas.data.canvasHeight + borderAdjust,
                            fill=canvas.data.backgroundColorFill)
def drawMap():
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            if canvas.data.currentMap[row][col] == 1:
                drawCell(row, col, canvas.data.currentMap[row][col])
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            if canvas.data.currentMap[row][col] != 1:
                drawCell(row, col, canvas.data.currentMap[row][col])

                ## this is to draw everything after the path


def drawCell(row, col, colorIndex):
    x0 = canvas.data.spaceUI + canvas.data.cellWidth*col
    y0 = canvas.data.border + canvas.data.cellHeight*row
    x1 = x0 + canvas.data.cellWidth
    y1 = y0 + canvas.data.cellHeight
    color = canvas.data.cellColor
    borderColor = canvas.data.cellBorderColor
    canvas.create_rectangle(x0, y0, x1, y1, fill=color[colorIndex],
                            outline=borderColor[colorIndex])
def drawTitle():
    cX = canvas.data.spaceUI*1.0/2
    sY = canvas.data.cellHeight*(2.6/3)
    border = canvas.data.spaceBorderUI
    canvas.create_rectangle(border, border,
                            canvas.data.spaceUI - border, sY*2,
                            fill=canvas.data.boxColorUI,
                            outline=canvas.data.uiBorderColor, width=2)

    canvas.create_text(cX, sY, text="Tower Defense Lite", fill="white",
                       font="Times 18", anchor=S)
    canvas.create_text(cX, sY*2-10, text="Author:  Tomas Dardet",
                       fill="white",
                       font="Times 14", anchor=S)
def drawScoreAndMoney():
    border = 5
    canvas.create_rectangle(canvas.data.spaceBorderUI,
                            2*canvas.data.cellHeight-canvas.data.spaceBorderUI,
                            canvas.data.spaceUI - canvas.data.spaceBorderUI,
                            canvas.data.spaceBorderUI+ 4*canvas.data.cellHeight,
                            fill=canvas.data.boxColorUI,
                            outline=canvas.data.uiBorderColor, width=2)
    canvas.create_text(canvas.data.spaceBorderUI+ border,
                       canvas.data.cellHeight*2,
                       text="Score:        " + str(canvas.data.score),
                       fill="yellow",
                       font="Times 14", anchor=NW)
    canvas.create_text(canvas.data.spaceBorderUI + border,
                       canvas.data.cellHeight*3.2,
                       text="Money($):  " + str(canvas.data.money),
                       fill="yellow",
                       font="Times 14", anchor=NW)
def drawLives():
    border = 5
    canvas.create_text(canvas.data.spaceBorderUI + border,
                       5*canvas.data.cellHeight/2 + 2,
                       text="Lives:        " + str(canvas.data.lives),
                       fill="blue",
                       font="Times 14", anchor=NW)
def drawSplashScreen():
    canvas.create_rectangle(0, 0, canvas.data.canvasWidth,
                            canvas.data.canvasHeight,
                            fill="black", stipple="gray75")
    yTop = 90
    yTop2 = yTop + 100
    spaceBetweenVertical = 35
    edgeAdjust = 3
    canvas.create_text(canvas.data.canvasWidth/2 + 95, yTop,
                       text="Tower Defense Lite", fill="white",
                       font="Times 42")
    instruct = ["Kill creeps with towers to win!",
                "Don't lose all your lives!",
                " ",
                "To play - Press Enter", "(instructions for gameplay below)",
                " ",
                "Instructions: ",
                "Press 'P' to Pause the game",
                "Press 'M' to choose a Differnt Map",
                "Select a Tower with 1, 2, 3, or 4",
                "Click on the map to Place Selected Tower",
                "Press the START GAME button to start"]
    for i in xrange(len(instruct)):
        y0 = yTop2 + spaceBetweenVertical * i
        canvas.create_text(canvas.data.canvasWidth/2 + 95, y0,
                           text=instruct[i], fill="white",
                           font="Times 22")
def drawTowerInfo():
    check = canvas.data.pressedTowerIndex
    edgeOfRect1 = canvas.data.spaceBorderUI
    edgeOfInfo = canvas.data.spaceBorderUI + 5
    height = canvas.data.canvasHeight
    width = canvas.data.spaceUI
    spaceBetweenText = 30
    canvas.create_rectangle(edgeOfRect1, height/2, width - edgeOfRect1,
                            height - edgeOfRect1,
                            fill=canvas.data.boxColorUI,
                            outline=canvas.data.uiBorderColor, width=2)
    if check != None:
        info = [str(canvas.data.towerName[check]),
                "Cost($): " + str(canvas.data.pressedTowerCost[check]),
                "Damage: " + str(canvas.data.towerDamage[check]),
                "Fire Rate: " + str(canvas.data.fireRate[check]),
                "Range: " + str(canvas.data.towerRange[check]),
                "Info: " + str(canvas.data.towerInfo[check])]
        color = canvas.data.towerColorOneList[check]
        towerInfo(edgeOfInfo, height,
                  width, spaceBetweenText, info, check, color)
    else:
        info = ["No Tower Selected", "Press from 1 to 4",
                "to View and Select", "Tower"]
        color = "white"
        towerInfo(edgeOfInfo, height, width,
                  spaceBetweenText, info, check, color)

def towerInfo(edgeOfInfo, height, width, spaceBetweenText, info, check, color):
    for row in xrange(len(info)):
        y = height/1.7 + spaceBetweenText*row + edgeOfInfo
        if row == 0:
            canvas.create_text(width/2+20, height/1.7 + edgeOfInfo,
                               text=info[row],
                               fill=color, font="Times 12")
        else:
            canvas.create_text(width/3.0-10, y, text=info[row],
                               fill=color,
                               font="Times 12", anchor=W)

def drawTowerImages():
    towerType = canvas.data.pressedTowerIndex
    edgeOfRect1 = canvas.data.spaceBorderUI
    edgeOfInfo = canvas.data.spaceBorderUI + 5
    height = canvas.data.canvasHeight
    width = canvas.data.spaceUI
    imageSpacing = 60
    for i in xrange(len(canvas.data.imageTower)):
        y = height/1.7 + imageSpacing*i + edgeOfInfo
        if towerType == i:
            canvas.create_image(edgeOfInfo, y,
                                image=canvas.data.imageTower[i],
                                activeimage=canvas.data.imageTower[i],
                                anchor=W)
        else:
            canvas.create_image(edgeOfInfo, y,
                                image=canvas.data.disabledTower[i],
                                activeimage=canvas.data.imageTower[i],
                                anchor=W)

def drawWaveButton():
    fix = 7
    x0 = canvas.data.spaceBorderUI
    y0 = (9)*canvas.data.cellHeight/2 - fix
    x1 = canvas.data.spaceUI - canvas.data.spaceBorderUI
    y1 = y0 + canvas.data.cellHeight + fix
    canvas.create_rectangle(x0, y0, x1, y1, fill=canvas.data.boxColorUI,
                            outline=canvas.data.buttonColor, width=2)
    if not canvas.data.waveButtonPressed:
        canvas.create_text(x0 +(x1-x0)/2, y0 +(y1 - y0)/2,
                           text="->START GAME!<-",
                           font="Times 16", activefill="red", fill="azure")
    else:
        canvas.create_text(x0 +(x1-x0)/2, y0 +(y1 - y0)/2,
                           text="      Next Wave\n[click here or press 'w']",
                           font="Times 13", activefill="red", fill="azure")
def drawCurrentWave():
    fix = 7
    x0 = canvas.data.spaceBorderUI
    y0 = (12)*canvas.data.cellHeight/2 - fix
    x1 = canvas.data.spaceUI - canvas.data.spaceBorderUI
    y1 = y0 + canvas.data.cellHeight + fix
    canvas.create_rectangle(x0, y0, x1, y1, fill=canvas.data.boxColorUI,
                            outline=canvas.data.uiBorderColor, width=2)
    canvas.create_text(x0 +(x1-x0)/2, y0 +(y1 - y0)/2,
                       text="Wave " + str(canvas.data.currentWaveIndex+1) +\
                    " | "+str(len(canvas.data.creepNumberPerWaveList)+1),
                       font="Times 17",
                       fill="azure")
def drawPrintNoMoney():
    if canvas.data.printNoMoney:
        canvas.create_text(canvas.data.spaceUI/2,
                           3*canvas.data.canvasHeight/6,
                           text="NOT ENOUGH MONEY ($)", font="Times 13",
                           fill="limegreen", anchor=S)
        canvas.create_text(canvas.data.spaceUI/2+42,
                           2*canvas.data.canvasHeight/6-69,
                           text="<<<--- ", font="Times 15",
                           fill="limegreen", anchor=S)
def drawPauseMessage():
    canvas.create_text(canvas.data.spaceUI/2,
                       canvas.data.canvasHeight-14,
                       text="'S' - Game Speed x 2\n'P' - Pause Game",
                       font="Times 14",
                       fill="white", anchor=S)

def drawGame():
    drawBackground()
    drawMap()
    drawTitle()
    drawScoreAndMoney()
    drawLives()
    drawTowerInfo()
    drawTowerImages()
    drawWaveButton()
    drawCurrentWave()
    drawPrintNoMoney()
    drawPauseMessage()
    drawCreeps(canvas.data.creeps)
    drawTowers(canvas.data.towers)
    drawFirstTowerShots(canvas.data.firstTowerShotList)
    drawFourthTowerShots(canvas.data.fourthTowerShotList)

def redrawAll():
    canvas.delete(ALL)
    drawGame()
    space = 35
    if canvas.data.gameOver and canvas.data.lives <= 0:
        canvas.create_rectangle(0, 0, canvas.data.canvasWidth,
                                canvas.data.canvasHeight,
                                fill="black", stipple="gray75")
        canvas.create_text(canvas.data.canvasWidth/2 + 90,
                           canvas.data.canvasHeight/2 - space*2,
                           text="Final Score: " + str(canvas.data.score),
                           fill="yellow", font="Times 40")
        canvas.create_text(canvas.data.canvasWidth/2 + 90,
                           canvas.data.canvasHeight/2,
                           text="GAME OVER", fill="white",
                           font="Times 32")
        canvas.create_text(canvas.data.canvasWidth/2 + 90,
                           canvas.data.canvasHeight/2 + space*2,
                           text="Press 'R' to RESTART", fill="white",
                           font="Times 28")
    elif canvas.data.gameOver and not canvas.data.splashScreen:
        canvas.create_rectangle(0, 0, canvas.data.canvasWidth,
                                canvas.data.canvasHeight,
                                fill="black", stipple="gray75")
        canvas.create_text(canvas.data.canvasWidth/2 + 90,
                           canvas.data.canvasHeight/2 - space*2,
                           text="Final Score: " + str(canvas.data.score),
                           fill="yellow", font="Times 40")
        canvas.create_text(canvas.data.canvasWidth/2 + 90,
                           canvas.data.canvasHeight/2,
                           text="!! YOU WIN !!", fill="white",
                           font="Times 36")
        canvas.create_text(canvas.data.canvasWidth/2 + 90,
                           canvas.data.canvasHeight/2 + space*2,
                           text="Press 'R' to RESTART", fill="white",
                           font="Times 28")
    elif canvas.data.splashScreen:
        drawSplashScreen()
    elif canvas.data.pauseGame:
        canvas.create_rectangle(0, 0, canvas.data.canvasWidth,
                                canvas.data.canvasHeight,
                                fill="black", stipple="gray50")
        canvas.create_text(canvas.data.canvasWidth/2 + 58,
                           canvas.data.canvasHeight/2,
                           text=("GAME PAUSED\n\nPress 'P' to CONTINUE\n"
                                 "\nPress 'M' to\nRESTART or choose a NEW MAP"),
                           fill="white", font="Times 28")

##############################################################################


########### copy-paste below here ###########

def run():
    init(0)
    root.bind("<Button-1>", mouse_pressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    root.mainloop()

run()
