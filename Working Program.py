#Initialising


import turtle
import math
from turtle import Screen, Turtle
turtle.Turtle(visible=False)
turtle.getscreen()
turtle.speed(-1)
turtle.ht()
screen = Screen()
screen.setup(800,800)
turtle.title('MA1008 Mini Project By Zheng Siyi')

lst = list() # list of coordinate for polygon created as [[0,100],[100,-100],...]
lstOfLines = list() # create list of lines (side of polygon) for intersection check during creation
clickPoint = list() # store x,y value of click point to check inside/outside as [x,y]
sideLst = list() # create list to store the sides of polygon in order to determine inside/outside polygon
numColourLst = list() # to store outline and interior colour of polygons opened as [[1,outline1,fill1],[2,outline2,fill2],...]
nameNumLst = list() # to store the name of file and the corresounding number as [[fileName1,1],[...],...]

box = [[-380,380],[-340,380],[-340,360],[-360,360],[-380,360]] # UI button outline
polygonCount = 0 # count number of polygon in display
polygonSelect = None # to store the num of polyon selected, first-1, second-2 ... 




# Defined functions
# CONTENT

# 1. general functions

# 2. polygon creation functions
## 2.1 pre-required functions
## 2.2 functions to check for intersection
## 2.3 functions for creation

# 3. polygon display functions

# 4. polygon manipulation functions
## 4.1 delete/add vertex functions
## 4.2 move functions
## 4.3 rotate functions
## 4.4 scale functions
## 4.5 linear and rotation pattern functions

# 5. polygon analytical tools functions
## 5.1 perimeter of polygon functions
## 5.2 area of polygon functions
## 5.3 click point inside or outside polygon

# 6. User Interface functions





# 1. general functions


def saveList(fileName): # define a function to save the list containing polygon vertices into a file 
    global lst
    with open(fileName,'w') as File:
        for i in range(len(lst)):
            print(f'{lst[i][0]} {lst[i][1]}',file = File)

def readFile(fileName): # used when analysing a polygon
    global lst
    lst = list() # clear last polygon info
    with open(fileName,'r') as File:
        for line in File:
            pointStr = line.split()
            point = [int(pointStr[0]),int(pointStr[1])]
            lst.append(point)
    drawPolygon()

def openFile(fileName): # used when opening a polygon
    global lst
    global nameNumLst
    global polygonCount
    count = 0
    lst = list() # clear last polygon info
    with open(fileName,'r') as File:
        for line in File:
            pointStr = line.split()
            point = [int(pointStr[0]),int(pointStr[1])]
            lst.append(point)
    drawPolygon()
    createlstOfLines() # polygonCount add 1
    if len(nameNumLst) == 0:
        nameNumLst.append([fileName,polygonCount])
    else:
        for i in range(len(nameNumLst)):
            if fileName == nameNumLst[i][0]:
                count += 1
        if count == 0:
            nameNumLst.append([fileName,polygonCount]) 

def updateLst(polygonNum): # after selection, update lst to current selected polygon
    global nameNumLst
    global lst
    for i in range(len(nameNumLst)):
        if polygonNum == nameNumLst[i][1]:
            lst = list() # clear lst
            with open(nameNumLst[i][0],'r') as File:
                for line in File:
                    pointStr = line.split()
                    point = [int(pointStr[0]),int(pointStr[1])]
                    lst.append(point)
            
def drawPolygon(): # used to draw a polygon from lst
    global lst
    turtle.up()
    turtle.goto(lst[-1]) # start and end at last point in file
    turtle.write(lst[-1])
    turtle.pd()
    for i in range(len(lst)):
        turtle.goto(lst[i])
        turtle.write(lst[i])

def inputPoint(S): # ask for input, check for input, convert to a list store coordinate as (x,y)
    while True:
        try:
            coorStr = input(f'Enter coordinate of {S}: ')
            coorStrLst = coorStr.split(',')
            if len(coorStrLst) != 2: # try to product error when input is like '6,7,8'
                int('s')
            coorLst = [int(coorStrLst[0]),int(coorStrLst[1])] # convert to integer
            return coorLst
        except :
            print('Incorrect input, please enter again.')

def savePolygon():
    global lst
    global polygonSelect
    global nameNumLst
    for i in range(len(nameNumLst)):
        if polygonSelect == nameNumLst[i][1]:
            fileName = nameNumLst[i][0]
            saveList(fileName)
    
def drawAllPolygon():
    global nameNumLst
    global numColourLst
    for i in range(len(nameNumLst)):
        if nameNumLst[i][1] == numColourLst[i][0]:
            colour(nameNumLst[i][0],outline = numColourLst[i][1],fill = numColourLst[i][2])

def clearAll():
    global lst 
    global lstOfLines 
    global clickPoint
    global sideLst 
    global numColourLst 
    global nameNumLst 
    global polygonCount 
    global polygonSelect 
    lst = list()
    lstOfLines = list()
    clickPoint= list()
    sideLst = list()
    numColourLst = list()
    nameNumLst = list()
    polygonCount = 0
    polygonSelect = None

def clearForRedraw():
    global lst 
    global lstOfLines 
    global clickPoint
    global sideLst  
    global polygonCount 
    global polygonSelect
    turtle.clear()
    lst = list()
    lstOfLines = list()
    clickPoint= list()
    sideLst = list()
    polygonCount = 0
    polygonSelect = None
    
def createlstOfLines(): # create a list to store the sides features of a polygon for inside/outside check
    global lst
    global sideLst
    global polygonCount
    lstOfSides = list()
    for i in range(len(lst)):
        if i == len(lst)-1:
            lstOfSides.append(line(lst[-1],lst[0]))
        else:
            lstOfSides.append(line(lst[i],lst[i+1]))
    sideLst.append(lstOfSides)
    polygonCount += 1

            
# 2. polygon creation function


## 2.1 pre-required functions


def inputC(): # input check for enter coordinate
    while True:
        try:
            coorStr = input('Enter coordinate of vertex: ')
            if coorStr == '': # define empty str as end of creation
                return 'end'
            coorStrLst = coorStr.split(',')
            if len(coorStrLst) != 2: # try to product error when input is like '6,7,8'
                int('s')
            coorLst = [int(coorStrLst[0]),int(coorStrLst[1])] # convert to integer
            global lst
            if coorLst in lst: # current input same as previous input
                print('Same input as before, please re-enter')
                continue
            return coorLst
        except :
            print('Incorrect input, please enter again.')

def gotoClickPoint(x,y): # turtle go to rounded click point, print point coordinate on screen, save point, check intersection
    global lst
    x,y = round(x),round(y) # round to integer
    if len(lst) == 0:
        turtle.pu()
        turtle.goto(x,y)
        turtle.write(f'({x},{y})')
        turtle.pd()
    else:
        turtle.goto(x,y)
        turtle.write(f'({x},{y})')
    coorlst = [round(turtle.xcor()),round(turtle.ycor())]
    lst.append(coorlst)
    checkIntersect()

def goto(point): # define a function to goto the point entered as a list
    x,y = point
    if len(lst) == 0:
        turtle.pu()
        turtle.goto(x,y)
        turtle.write(f'({x},{y})')
        turtle.pd()
    else:
        turtle.goto(x,y)
        turtle.write(f'({x},{y})')

def closePolygon(): # check for home intersect and close polygon
    global lst
    global lstOfLines
    if checkHomeIntersect(): # need to re-create polygon if self-intersect on the way to origin
            print('Intersect!')
            turtle.clear() # clear screen, delete previous values
            lst = list()
            lstOfLines = list()
            return False
    else:
        turtle.goto(lst[0]) # go to origin
        return True

def closeClickPolygon(): # check for home intersect and close polygon
    global lst
    global lstOfLines
    global stopMouseClick
    if checkHomeIntersect(): # need to re-create polygon if self-intersect on the way to origin
            print('Intersect! Re-create new polygon!')
            turtle.clear() # clear screen, delete previous values
            lst = list()
            lstOfLines = list()
            setupUI()
            turtle.listen()
            turtle.onscreenclick(clickBox,1)
            turtle.mainloop()
    elif len(lst) <= 2:
        print('Not enough vertices!')
        recreatePolygon()
    else:
        turtle.goto(lst[0]) # close polygon
        print('Polygon Creation Completed!')
        while True:
            try:
                name = input('Enter file name to save polygon: ')
                saveList(name)
                break
            except:
                print('Invalid Input!')
                continue                         
        print('Polygon saved!')
        lst = list() # clear list for next creation
        lstOfLines = list()
        turtle.clear()
        setupUI()
        turtle.listen()
        turtle.onscreenclick(clickBox,1)
        turtle.mainloop()               

def recreatePolygon(): # when polygon intersect, ask user to recreate polygon
    global lst
    global lstOfLines
    print('Re-create new polygon!')
    turtle.clear()
    lst = list()
    lstOfLines = list()
    setupUI()
    turtle.listen()
    turtle.onscreenclick(clickBox,1)
    turtle.mainloop()
            

## 2.2 functions to check for intersection


def line(p1,p2): # input parameter p1 is starting point and p2 is end point
    A = p1[0]
    B = p2[0] - p1[0]
    C = p1[1]
    D = p2[1] - p1[1]
    return [[A,B],[C,D]]

def intersect(l1,l2): # l1 and l2 are list return by line() function, l1 is last line draw
    A = l1[0][1]
    B = -l2[0][1]
    C = l2[0][0] - l1[0][0]
    D = l1[1][1]
    E = -l2[1][1]
    F = l2[1][0] - l1[1][0]
    try : # if parallel, t1 and t2 cannot be solved, ZeroDivisionError will occur
        t1 = (C*E - B*F)/(A*E - B*D) # equation to solve simultaneous equations derived from cramer's rule
        t2 = (A*F - C*D)/(A*E - B*D) 
    except ZeroDivisionError:
        if checkOverlap():
            return True
        else:
            return False
    if t1 == 0 and t2 == 1: # when check with last line, new line and last line intersect at end point
        return False
    elif (t1 >= 0 and t1 <= 1) and (t2 >= 0 and t2 <= 1): # both t1 and t2 need to be between 0-1
        return True # True for intersection
    else:
        return False

def checkIntersect(): # should be put after append point to lst
    global lst
    global lstOfLines
    if len(lst) >= 2: # check if there at least two points to create a line
        lstOfLines.append(line(lst[-2],lst[-1]))
    if len(lst) >= 3: # intersection will only occur after third vertex is created
        for i in range(len(lst)-2): # for n vertices, there are n-2 sides to check for intersection 
            if intersect(lstOfLines[-1],lstOfLines[i]): # check intersection of last side draw with all previous sides
                print('Intersect')
                turtle.undo()
                turtle.undo()
                lst.pop()
                lstOfLines.pop()
                return True
    return False

def checkOverlap(): # check overlap of last line draw and the previous line draw
    global lst
    l2 = line(lst[-3],lst[-1]) # the end point of last line draw and start point of previous line draw
    l1 = line(lst[-1],lst[-2]) # last line draw
    A = l1[0][1]
    B = -l2[0][1]
    C = l2[0][0] - l1[0][0]
    D = l1[1][1]
    E = -l2[1][1]
    F = l2[1][0] - l1[1][0]
    try : 
        t1 = (C*E - B*F)/(A*E - B*D) 
        t2 = (A*F - C*D)/(A*E - B*D)
        return False # if can solve, twl line not parallel
    except ZeroDivisionError: # two lines parallel
        return True

def checkHomeIntersect():
    global lst
    global lstOfLines
    if len(lst) >= 2: # check if there at least two points to create a line
        lstOfLines.append(line(lst[-1],lst[0]))
    if len(lst) >= 4: # intersection will only occur after fourth vertex is created
        for i in range(len(lst)-2): # does not check for the first side created because close the polygon will intersect with the first side
            if intersect(lstOfLines[-1],lstOfLines[i+1]): 
                return True
    return False


## 2.3 functions for creation


def coordinateCreate(): # function for coordinate creation
    global lst
    while True:
        point = inputC()
        if point == 'end' and len(lst) < 3:
            print('Not enough points to form a polygon')
            recreatePolygon()
        elif point == 'end': # check if input ends
            if closePolygon():
                print('Polygon Creation Completed!')
                while True:
                    try:
                        name = input('Enter file name to save polygon: ')
                        saveList(name)
                        break
                    except:
                        print('Invalid Input!')
                        continue                         
                print('Polygon saved!')
                turtle.clear()
                lst = list() # clear list for next creation
                lstOfLines = list()
                break
            else:
                recreatePolygon()
        goto(point)
        lst.append(point)
        checkIntersect()

def mouseClickCreation(): # function for mouseclikc creation
    print('Click to enter point, press enter to finish.') 
    turtle.listen()
    turtle.onscreenclick(gotoClickPoint,1)
    turtle.onkey(closeClickPolygon,'Return') # tap return to finish polygon creation
    turtle.mainloop()





# 3. polygon display functions


def colour(fileName,outline = None,fill = None): # colour a polygon when it is opened
    if outline == None and fill == None:
        openFile(fileName)
    elif outline == None:
        turtle.color('black',fill)
        turtle.begin_fill()
        openFile(fileName)
        turtle.end_fill()
    elif fill == None:
        turtle.pencolor(outline)
        openFile(fileName)
    else:
        turtle.color(outline,fill)
        turtle.begin_fill()
        openFile(fileName)
        turtle.end_fill()
    turtle.pencolor('black')

    



# 4. polygon manipulation functions


## 4.1 delete/add vertex functions

def intersectAdd(l1,l2): # l1 and l2 are list return by line() function, l1 is last line draw
    A = l1[0][1]
    B = -l2[0][1]
    C = l2[0][0] - l1[0][0]
    D = l1[1][1]
    E = -l2[1][1]
    F = l2[1][0] - l1[1][0]
    try : # if parallel, t1 and t2 cannot be solved, ZeroDivisionError will occur
        t1 = (C*E - B*F)/(A*E - B*D) # equation to solve simultaneous equations derived from cramer's rule
        t2 = (A*F - C*D)/(A*E - B*D) 
    except ZeroDivisionError:
        if checkOverlap():
            return True
        else:
            return False
    if t1 == 0 and t2 == 1: # when check with last line, new line and last line intersect at end point
        return False
    elif (t1 > 0 and t1 < 1) and (t2 > 0 and t2 < 1): # both t1 and t2 need to be between 0-1
        return True # True for intersection
    else:
        return False
    
def deleteVertex(indexOfVertex):
    global lst
    sideLst = list()
    if len(lst) == 4:
        lst.pop(indexOfVertex)
        savePolygon() # polygon change saved
        clearForRedraw()
        setupUI()
        drawAllPolygon()
        return True
    for i in range(len(lst)):
        if i == len(lst)-1:
            sideLst.append(line(lst[i],lst[0]))
        else:       
            sideLst.append(line(lst[i],lst[i+1]))
    if indexOfVertex == len(lst)-1: # last vertex requires special handling
        newL = line(lst[0],lst[-2])
    else:
        newL = line(lst[indexOfVertex-1],lst[indexOfVertex+1])
    sideLst.pop(indexOfVertex)
    sideLst.pop(indexOfVertex-1)
    for i in range(len(sideLst)): # skip two removed sides
        if intersectAdd(sideLst[i],newL):
                print('Intersect')
                return False
    lst.pop(indexOfVertex)
    savePolygon() # polygon change saved
    clearForRedraw()
    setupUI()
    drawAllPolygon()
    return True

def addVertex(vertexAdd,adjacent1Index,adjacent2Index): # assume adjacent vertices are next to check other, adjacent1Index < adjacent2Index
    global lst
    line1 = line(vertexAdd,lst[adjacent1Index])
    line2 = line(lst[adjacent2Index],vertexAdd)
    for i in range(len(lst)):
        if i != adjacent1Index:
            if i == len(lst)-1:
                lineCheck = line(lst[i],lst[0]) # when loop to the last point in lst
                if intersectAdd(lineCheck,line1) or intersectAdd(line2,lineCheck):
                    print('Intersect')
                    return False
                    
            else:
                lineCheck = line(lst[i],lst[i+1])
                if intersectAdd(lineCheck,line1) or intersectAdd(line2,lineCheck):
                    print('Intersect')
                    return False
    if adjacent2Index == 0:
        lst.insert(-1,vertexAdd)
    else:
        lst.insert(adjacent2Index,vertexAdd)
    savePolygon() # polygon change saved
    clearForRedraw()
    setupUI()
    drawAllPolygon()
    return True


## 4.2 move functions


def movePolygon(direction,distance): # direction in angle 0-360, distance > 0
    dx = distance*math.cos(math.radians(direction))
    dy = distance*math.sin(math.radians(direction))
    global lst
    for i in range(len(lst)):
        lst[i] = [round(lst[i][0] + dx),round(lst[i][1] + dy)] # round to integer
    savePolygon() # polygon change saved
    clearForRedraw()
    setupUI()
    drawAllPolygon()


## 4.3 rotate functions


def matrixProduct(X,Y): # s
    a,b,c,d = X
    x,y = Y
    return [a*x + b*y,c*x + d*y]

def rotation(point,angle): # angle in degree 0-360, point in [x,y], clockwise rotation
    global lst
    angle = math.radians(angle)
    X = [math.cos(angle),math.sin(angle),-math.sin(angle),math.cos(angle)]
    for i in range(len(lst)):
        Y = [lst[i][0]-point[0],lst[i][1]-point[1]]
        product = matrixProduct(X,Y)
        newX,newY = product[0]+point[0],product[1]+point[1]
        newP = [round(newX),round(newY)]
        lst[i] = newP
    savePolygon() # polygon change saved
    clearForRedraw()
    setupUI()
    drawAllPolygon()

    
## 4.4 scale functions


def scalePolygon(scale):
    global lst
    for i in range(len(lst)):
        x,y = lst[i]
        x,y = x*scale,y*scale
        x,y = round(x),round(y)
        lst[i] = [x,y]
    savePolygon() # polygon change saved
    clearForRedraw()
    setupUI()
    drawAllPolygon()
    
## 4.5 linear and rotation pattern functions
        

def scalePolygonPattern(scale):
    global lst
    for i in range(len(lst)):
        x,y = lst[i]
        x,y = x*scale,y*scale
        lst[i] = [x,y]

def rotationForPattern(point,angle): # angle in degree 0-360, point in [x,y], clockwise rotation
    global lst
    angle = math.radians(angle)
    X = [math.cos(angle),math.sin(angle),-math.sin(angle),math.cos(angle)]
    for i in range(len(lst)):
        Y = [lst[i][0]-point[0],lst[i][1]-point[1]]
        product = matrixProduct(X,Y)
        newX,newY = product[0]+point[0],product[1]+point[1]
        newP = [round(newX),round(newY)]
        lst[i] = newP

def movePolygonPattern(direction,distance): # direction in angle 0-360, distance > 0
    dx = distance*math.cos(math.radians(direction))
    dy = distance*math.sin(math.radians(direction))
    global lst
    for i in range(len(lst)):
        lst[i] = [round(lst[i][0] + dx),round(lst[i][1] + dy)] # round to integer

def linearPattern(direction,distance,number,scale): # distance > 0
    global polygonSelect
    global numColourLst
    for i in range(len(numColourLst)):
        if polygonSelect == numColourLst[i][0]:
            outline = numColourLst[i][1]
            fill = numColourLst[i][2]
    if outline == None and fill == None: # no fill, no outline
        for i in range(number):
            scalePolygonPattern(scale)
            movePolygonPattern(direction,distance)
            drawPolygon()
    elif outline != None and fill == None: # yes outline
        for i in range(number):
            scalePolygonPattern(scale)
            movePolygonPattern(direction,distance)
            turtle.pencolor(outline)
            drawPolygon()
            turtle.pencolor('black')
    elif outline == None and fill != None: # yes fill
        for i in range(number):
            scalePolygonPattern(scale)
            movePolygonPattern(direction,distance)
            turtle.color('black',fill)
            turtle.begin_fill()
            drawPolygon()
            turtle.end_fill()
            turtle.pencolor('black')
    else: # yes fill and outline
        for i in range(number):
            scalePolygonPattern(scale)
            movePolygonPattern(direction,distance)
            turtle.color(outline,fill)
            turtle.begin_fill()
            drawPolygon()
            turtle.end_fill()
            turtle.pencolor('black')
            

def rotationPattern(point,angle,number,scale):
    global polygonSelect
    global numColourLst
    
    for i in range(len(numColourLst)):
        if polygonSelect == numColourLst[i][0]:
            outline = numColourLst[i][1]
            fill = numColourLst[i][2]
    if outline == None and fill == None: # no fill, no outline
        for i in range(number):
            scalePolygonPattern(scale)
            rotationForPattern(point,angle)
            drawPolygon()
    elif outline != None and fill == None: # yes outline
        for i in range(number):
            scalePolygonPattern(scale)
            rotationForPattern(point,angle)
            turtle.pencolor(outline)
            drawPolygon()
            turtle.pencolor('black')
    elif outline == None and fill != None: # yes fill
        for i in range(number):
            scalePolygonPattern(scale)
            rotationForPattern(point,angle)
            turtle.color('black',fill)
            turtle.begin_fill()
            drawPolygon()
            turtle.end_fill()
            turtle.pencolor('black')
    else: # yes fill and outline
        for i in range(number):
            scalePolygonPattern(scale)
            rotationForPattern(point,angle)
            turtle.color(outline,fill)
            turtle.begin_fill()
            drawPolygon()
            turtle.end_fill()
            turtle.pencolor('black')





# 5. polygon analytical tools functions


## 5.1 perimeter of polygon functions


def distance(p1,p2):
    D = math.hypot((p1[0] - p2[0]),(p1[1] - p2[1]))
    return D

def perimeter(fileName):
    readFile(fileName)
    peri = 0
    for i in range(len(lst)):
        if i == len(lst)-1:
            d = distance(lst[-1],lst[0])
            peri += d
        else:
            d = distance(lst[i],lst[i+1])
            peri += d
    return round(peri,2) # to two decimal places


## 5.2 area of polygon functions


def vThreeP(p1,p2,p3): # v1 from p2 to p1, v2 from p2 to p3
    v1 = [p1[0]-p2[0],p1[1]-p2[1]]
    v2 = [p3[0]-p2[0],p3[1]-p2[1]]
    return v1,v2

def areaTri(v1,v2):
    x1,y1 = v1
    x2,y2 = v2
    A = 0.5*(x1*y2 - y1*x2)
    return A

def areaPolygon(fileName):
    global lst
    readFile(fileName)
    area = 0
    for i in range(len(lst)-2):
        v1,v2 = vThreeP(lst[i+1],lst[0],lst[i+2])
        A = areaTri(v1,v2)
        area += A
    area = round(abs(area),1)
    return area


## 5.3 click point inside or outside polygon


def clickP(x,y): # click point for inside/outside polygon
    global clickPoint
    clickPoint = [round(x),round(y)]
    # print(clickPoint)
    checkIOIntersect()
    print('')

def endIO(): # exit the inside outside polygon mode
    global polygonSelect
    polygonSelect = None
    print('Exit click mode')
    turtle.listen()
    turtle.onscreenclick(clickBox,1)
    turtle.mainloop()

def intersectIO(l1,l2): # l1 and l2 are list return by line() function, l1 is last line draw
    A = l1[0][1]
    B = -l2[0][1]
    C = l2[0][0] - l1[0][0]
    D = l1[1][1]
    E = -l2[1][1]
    F = l2[1][0] - l1[1][0]
    try : # if parallel, t1 and t2 cannot be solved, ZeroDivisionError will occur
        t1 = (C*E - B*F)/(A*E - B*D) # equation to solve simultaneous equations derived from cramer's rule
        t2 = (A*F - C*D)/(A*E - B*D) 
    except ZeroDivisionError:
        if checkOverlap():
            return True
        else:
            return False
    if t2 >= 0 and t2 <= 1 and t1 >= 0: # t1 >=0 because projection line extend in one direction
        return True # True for intersection
    else:
        return False
    
def checkIOIntersect(): # intersection check 
    global clickPoint
    global sideLst
    IOinfo = list()
    for num in range(len(sideLst)): # go through the number of polygons in display
        # print(len(sideLst))
        inside = 0
        for theta in range(0,360,1): # project line in different directions
            intersectCount = 0
            if theta == 90:
                diVect = [0,1]
            elif theta == 270:
                diVect = [0,-1]
            elif 90 > theta >= 0 or 360 > theta > 270:
                yP1 = round(math.tan(math.radians(theta)),2)
                diVect = [1,yP1]
            else:
                yP1 = round(math.tan(math.radians(theta)),2)
                diVect = [-1,-yP1]
            # print(diVect)
            lineRound = line(clickPoint,diVect)
            for i in range(len(sideLst[num])): # go through the sides
                if intersectIO(lineRound,sideLst[num][i]):
                    intersectCount +=1
            # print(intersectCount)
            if intersectCount%2 != 0: # odd number
                inside += 1
        if inside > 0:
            print('Inside polygon',num+1)
            IOinfo.append(['I',num])
        else:
            print('Outside polygon',num+1)
            IOinfo.append(['O',num])
    return IOinfo




# 5.4 Select a polygon


def clickSelect(x,y):
    global clickPoint
    global polygonSelect
    clickPoint = [round(x),round(y)]
    InorOut = checkClickIOIntersect() # format: [['O', 0], ['I', 1]]
    # print(InorOut)
    for i in range(len(InorOut)):
        if InorOut[i][0] == 'I':
            polygonSelect = InorOut[i][1] + 1 # 1 for first polygon, 2 for second polygon ...
            print(f'Polygon {polygonSelect} selected!')      
    turtle.listen()
    turtle.onscreenclick(clickBox,1)
    turtle.mainloop()

def checkClickIOIntersect(): # check intersection for polygon selection
    global clickPoint
    global sideLst
    IOinfo = list()
    for num in range(len(sideLst)): # go through the number of polygons in display
        # print(len(sideLst))
        inside = 0
        for theta in range(0,360,1): # project line in different directions
            intersectCount = 0
            if theta == 90:
                diVect = [0,1]
            elif theta == 270:
                diVect = [0,-1]
            elif 90 > theta >= 0 or 360 > theta > 270:
                yP1 = round(math.tan(math.radians(theta)),2)
                diVect = [1,yP1]
            else:
                yP1 = round(math.tan(math.radians(theta)),2)
                diVect = [-1,-yP1]
            # print(diVect)
            lineRound = line(clickPoint,diVect)
            for i in range(len(sideLst[num])): # go through the sides
                if intersectIO(lineRound,sideLst[num][i]):
                    intersectCount +=1
            # print(intersectCount)
            if intersectCount%2 != 0: # odd number
                inside += 1
        if inside > 0:
            # print('Inside polygon',num+1)
            IOinfo.append(['I',num])
        else:
            # print('Outside polygon',num+1)
            IOinfo.append(['O',num])
    return IOinfo





# 6. User Interface functions

    
def moveBox(direction,distance): # to duplicate the button
    global box
    if direction == 'x':
        for i in range(len(box)):
            box[i][0] += distance
    if direction == 'y':
        for i in range(len(box)):
            box[i][1] += distance
            
def setupUI(): # to set up the user interface
    global box
    box = [[-380,380],[-340,380],[-340,360],[-360,360],[-380,360]]
    creater = [[380,-380],[320,-380],[260,-380],[260,-360],[380,-360]]
    name = ['create','open','edit','find','select','clear']
    turtle.pu()
    turtle.goto(creater[-1])
    turtle.pd()
    for i in range(len(creater)):
        turtle.goto(creater[i])
        if i == 1:
            turtle.write('Created by Zheng Siyi',align = 'center',font = ('Arial',12,'normal'))
    for i in range(6):
        turtle.pu()
        turtle.goto(box[-1])
        turtle.pd()
        for j in range(len(box)):
            turtle.goto(box[j])
            if j == 3:
                turtle.write(name[i],align = 'center',font = ('Arial',13,'normal'))
        moveBox('x',50)
        

def checkUIinput(): # check user integer input
    while True:
        try:
            w = int(input('Input: '))
            return w
            break
        except:
            print('Invalid input!')

    
def clickBox(x,y): # the main running function for this program
    global lst
    global polygonSelect
    global nameNumLst
    global lstOfLines 
    global clickPoint 
    global sideLst
    global numColourLst
    global polygonCount
    x,y = round(x),round(y)
    if x in range(-380,-340) and y in range(360,380): # create box
        turtle.clear()
        setupUI()
        lst = list()
        lstOfLines = list()
        print('1 - Create by enter coordinate')
        print('2 - Create by mouse click enter')
        while True:
            w = checkUIinput()
            if w in range(1,3):
                break
            else:
                print('Invalid input!')
                continue
        if w == 1:
            coordinateCreate()
            setupUI()
        elif w == 2:
            mouseClickCreation()
            setupUI()
    elif x in range(-330,-290) and y in range(360,380): # open box
        while True: # check for file name
            a = 0
            try:
                fileName = input('Enter name of file: ')
                for i in range(len(nameNumLst)):
                    if fileName == nameNumLst[i][0]:
                        print('File already opened!')
                        a += 1
                if a > 0:
                    continue
                fileToOpen = open(fileName,'r')
                fileToOpen.close()
                break
            except FileNotFoundError:
                print('File not found!')
        colourEndCheck = 0
        while True: # check for colour polygon
            if colourEndCheck == 1:
                colourEndCheck = 0
                break
            print('Do you want to colour the outline of the polygon?')
            colourYN1 = input('Y/N: ')
            print('Do you want to colour the interior of the polygon?')
            colourYN2 = input('Y/N: ')
            if colourYN1 == 'Y' and colourYN2 == 'Y': # both outline and interior
                while True:
                    outlineColour = input('Enter outline colour: ')
                    interiorColour = input('Enter interior colour: ')
                    try:
                        colour(fileName,outline = outlineColour,fill = interiorColour)
                        colourEndCheck += 1
                        numColourLst.append([polygonCount,outlineColour,interiorColour])
                        break
                    except:
                        print('Colour not found!')
            elif colourYN1 == 'Y' and colourYN2 == 'N': # outline but not interior
                while True:
                    outlineColour = input('Enter outline colour: ')
                    try:
                        colour(fileName,outline = outlineColour)
                        colourEndCheck += 1
                        numColourLst.append([polygonCount,outlineColour,None])
                        break
                    except:
                        print('Colour not found!')
                    continue
            elif colourYN1 == 'N' and colourYN2 == 'Y': # interior but not outline
                while True:
                    interiorColour = input('Enter interior colour: ')
                    try:
                        colour(fileName,fill = interiorColour)
                        colourEndCheck += 1
                        numColourLst.append([polygonCount,None,interiorColour])
                        break
                    except:
                        print('Colour not found!')
                        continue
            elif colourYN1 == 'N' and colourYN2 == 'N': # no colour
                openFile(fileName)
                numColourLst.append([polygonCount,None,None])
                break
            else:
                print('Invalid input!')
                continue
    elif x in range(-280,-240) and y in range(360,380) and len(lst) != 0 and polygonSelect!= None: # edit box
        updateLst(polygonSelect)
        print('1 - Delete/Add Vertex')
        print('2 - Move Polygon')
        print('3 - Rotate Polygon')
        print('4 - Scale Polygon')
        print('5 - Linear Pattern')
        print('6 - Circular Pattern')
        while True:
            try:
                editInput = int(input('Enter corresponding number to edit polygon: '))
                if editInput in range(1,7):
                    break
                else:
                    print('Invalid input!')
                    continue          
            except ValueError:
                print('Invalid input!')
                continue
        if editInput == 1: # Add/delete vertex
            print('1 - Add vertex')
            print('2 - Delete vertex')
            while True:
                try:
                    addDeleteInput = int(input('Enter corresponding number: '))
                    if addDeleteInput not in range(1,3):
                        print('Invalid input!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            if addDeleteInput == 1: # Add vertex
                while True:
                    newVertex = inputPoint('new vertex')
                    if newVertex in lst:
                        print('New vertex already exist!')
                        continue
                    else:
                        break
                while True:
                    Adj1 = inputPoint('first vertex to be connected to')
                    Adj2 = inputPoint('second vertex to be connected to')
                    if Adj1 not in lst or Adj2 not in lst:
                        print('Point enterted not a vertex!')
                        continue
                    index1 = lst.index(Adj1)
                    index2 = lst.index(Adj2)
                    if (index1 == len(lst)-1):
                        if addVertex(newVertex,index1,0):
                            break
                        else:
                            continue
                    elif (index2 == len(lst)-1) :
                        if addVertex(newVertex,index2,0):
                            break
                        else:
                            continue
                    elif index2 > index1:
                        if addVertex(newVertex,index1,index2):
                            break
                        else:
                            continue
                    elif index1 > index2:
                        if addVertex(newVertex,index2,index1):
                            break
                        else:
                            continue
                    else:
                        continue
            elif addDeleteInput == 2: # Delete vertex
                if len(lst) > 3:
                    while True:
                        deletedVertex = inputPoint('vertex you want to delete')
                        if deletedVertex not in lst:
                            print('Not a vertex of polygon!')
                            continue
                        indexOfVertex = lst.index(deletedVertex)
                        if deleteVertex(indexOfVertex):
                            break
                        else:
                            continue
                else:
                    print('Not enough vertices!')                                          
        elif editInput == 2: # Move Polygon
            while True:
                try:
                    moveDirection = float(input('Enter the direction to move the polygon in degree (0-360): '))
                    if not 0 <= moveDirection <= 360:
                        print('Input out of range!')
                        continue
                    moveDistance = float(input('Enter the distance to move the polygon: '))
                    if moveDistance <= 0:
                        print('Please enter positive value!')
                        continue
                    movePolygon(moveDirection,moveDistance)
                    break
                except ValueError:
                    print('Invalid input!')
                    continue
        elif editInput == 3: # Rotate Polygon
            rotationPoint = inputPoint('point of rotation for polygon')
            while True:
                try:
                    rotationAngle = float(input('Enter the rotation angle clockwise in degree (0-360): '))
                    if not 0 <= rotationAngle <= 360: # in range 0-360 degree
                        print('Input out of range!')
                        continue
                    rotation(rotationPoint,rotationAngle)
                    break
                except ValueError:
                    print('Invalid input!')
                    continue
        elif editInput == 4: # Scale Polygon
            while True:
                try:
                    scaleFactor = float(input('Enter scale factor to scale polygon: ')) # positive scale factor
                    if scaleFactor <= 0:
                        print('Scale factor out of range!')
                        continue
                    scalePolygon(scaleFactor)
                    break
                except:
                    print('Invalid input!')
                    continue
        elif editInput == 5: # Linear Pattern
            while True:
                try:
                    linearPatternDirection = float(input('Enter the direction to move the polygon in degree (0-360): '))
                    if not 0 <= linearPatternDirection <= 360: # 0-360 degree
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            while True:
                try:
                    linearPatternDistance = float(input('Enter the distance to move the polygon: ')) # distance > 0
                    if linearPatternDistance <= 0:
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            while True:
                try:
                    linearPatternNumber = int(input('Enter the number to copy: ')) # integer number > 0
                    if linearPatternNumber <= 0:
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            while True:
                try:
                    linearPatternScale = float(input('Enter the scale to copy: ')) # float number > 0
                    if linearPatternScale <= 0:
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            linearPattern(linearPatternDirection,linearPatternDistance,linearPatternNumber,linearPatternScale)
        elif editInput == 6: # rotation pattern
            rotationPatternPoint = inputPoint('point of rotation: ')
            while True:
                try:
                    rotationPatternAngle = float(input('Enter the rotation angle clockwise in degree (0-360): '))
                    if not 0 <= rotationPatternAngle <= 360: # in range 0-360 degree
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            while True:
                try:
                    rotationPatternNumber = int(input('Enter the number to copy: ')) # integer number > 0
                    if rotationPatternNumber <= 0:
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            while True:
                try:
                    rotationPatternScale = float(input('Enter the scale to copy: ')) # float number > 0
                    if rotationPatternScale <= 0:
                        print('Input out of range!')
                        continue
                    else:
                        break
                except:
                    print('Invalid input!')
                    continue
            rotationPattern(rotationPatternPoint,rotationPatternAngle,rotationPatternNumber,rotationPatternScale)
        polygonSelect = None
    elif x in range(-230,-190) and y in range(360,380) and len(lst) != 0 and polygonSelect != None: # find box
        updateLst(polygonSelect)
        print('1 - Find perimeter')
        print('2 - Find area')
        print('3 - Point inside/outside polygon')
        while True:
            try:
                findInput = int(input('Enter corresponding number: '))
                if findInput in range(1,4):
                    break
                else:
                    print('Invalid input!')
                    continue          
            except ValueError:
                print('Invalid input!')
                continue
        if findInput == 1: # find perimeter
            peri = perimeter(nameNumLst[polygonSelect-1][0]) # calculate original file 
            print(f'Perimeter of polygon is {peri}')
        elif findInput == 2: # find area
            areaP = areaPolygon(nameNumLst[polygonSelect-1][0])
            print(f'Area of polygon is {areaP}')
        elif findInput == 3: # point inside/outside
            print('Clikc mouse on screen to find if click point is inside or outside polygon, press Enter key to exit this mode.')
            turtle.listen()
            turtle.onscreenclick(clickP,1)
            turtle.onkey(endIO,'Return') # click enter to end this mode
            turtle.mainloop()
        polygonSelect = None
    elif x in range(-180,-140) and y in range(360,380) and len(lst) != 0: # select box
        polygonSelect = None
        print('Click inside a polyon once to select it')
        turtle.listen()
        turtle.onscreenclick(clickSelect,1)
        turtle.mainloop()
    elif x in range (-130,-90) and y in range(360,380): # clear box
        turtle.clear()
        clearAll()
        setupUI()
        turtle.listen()
        turtle.onscreenclick(clickBox,1)
        turtle.mainloop()
    elif ((x in range(-230,-190) and y in range(360,380)) or (x in range(-280,-240) and y in range(360,380))) and polygonSelect == None:
        print('Need to select a polygon first!')
    elif ((x in range(-230,-190) and y in range(360,380)) or (x in range(-280,-240) and y in range(360,380))) or (x in range(-180,-140) and y in range(360,380)) and (len(lst) == 0):
        print('Need to open a polygon first!')
    
setupUI()
turtle.listen()
turtle.onscreenclick(clickBox,1)
turtle.mainloop()
