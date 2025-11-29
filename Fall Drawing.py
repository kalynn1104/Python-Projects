from graphics import *   # import everything from the graphics library
import random   # import the random library

def main():   # define the main function
   
    win = GraphWin("Welcome to Fall", 600, 600)   # GraphWin-class, new window titled "Welcome to Fall" (600x600 pixel)                                                 
    win.setBackground("skyblue")   
    
    drawSun(0, 0, 200, win)   # center point, radius, draw in the window 
    drawTree(350, 100, 250, 500, win)   # top left x & y value, width & height

    for i in range(random.randint(6, 8)):   # draw 6, 7, or 8 trees
        drawLeaf(random.randint(3, 300),    # x value
                 random.randint(250, 350),  # y value
                 random.randint(50, 100),   # width
                 random.randint(100, 125),  # height
                 win
                 )

    orangePumpkin = drawPumpkin(7, 455, 130, 180, "orange red", win)
    redPumpkin = drawPumpkin(350, 505, 80, 111, "brown", win)
    yellowPumpkin = drawPumpkin(260, 520, 60, 91, "gold", win)

    squirrel = Image(Point(495, 200), "squirrel.png")   
    squirrel.draw(win)

    pumpkinSpeed = -10   # y coordinate increases downward -> pumpkin goes up
    while True:   # infinate loop

        clickPoint = win.checkMouse()   
        if clickPoint != None:
            drawPumpkin(clickPoint.getX(), clickPoint.getY(), random.randint(30, 50), random.randint(30, 50),  
                        random.choice(["red2", "orange red", "gold", "forest green", "dodger blue", "blue violet"]), win)
        if win.checkMouse():
            break

        k = win.checkKey()
        if k == "w":
            squirrel.move(0, -10)   # up
        elif k == "s":
            squirrel.move(0, 10)    # down
        elif k == "a":
            squirrel.move(-10, 0)   # left
        elif k == "d":
            squirrel.move(10, 0)    # right

        for part in orangePumpkin:
            part.move(0, pumpkinSpeed)
        if orangePumpkin[0].getP1().getY() < 0:   # [0]-first item on the list, .getP1()-get the top left corner point, .getY()-get y value
            pumpkinSpeed = 10
        elif orangePumpkin[0].getP1().getY() > 500:
            pumpkinSpeed = -10

        update(30)   # set animation at 30 frames per second
        


def drawSun(x, y, r, win):
    sun = Circle(Point(x, y), r)
    sun.setFill("yellow")
    sun.setOutline("black")
    sun.draw(win)



def drawTree(x, y, w, h, win):
    bottom = Polygon(Point(x + 0.5*w, y + 0.25*h), 
                     Point(x, y + 0.75*h), 
                     Point(x + w, y + 0.75*h))
    bottom.setFill("forestgreen")
    bottom.draw(win)

    middle = Polygon(Point(x + 0.5*w, y + 0.125*h), 
                     Point(x + 0.125*w, y + 0.5*h), 
                     Point(x + 0.875*w, y + 0.5*h))
    middle.setFill("forestgreen")
    middle.draw(win)

    top = Polygon(Point(x + 0.5*w, y), 
                  Point(x + 0.25*w, y + 0.25*h), 
                  Point(x + 0.75*w, y + 0.25*h))
    top.setFill("forestgreen")
    top.draw(win)

    stump = Rectangle(Point(x + 0.375*w, y + 0.75*h), 
                      Point(x + 0.625*w, y + h))
    stump.setFill("saddlebrown")
    stump.draw(win)



def drawLeaf(x, y, w, h, win):
    spike1 = Polygon(Point(x + 0.1875*w, y + 0.8125*h), 
                  Point(x + 0.5*w, y + 0.75*h), 
                  Point(x + 0.375*w, y + 0.625*h))
    spike1.setFill("red4")
    spike1.draw(win)

    spike2 = Polygon(Point(x + 0.125*w, y + 0.375*h), 
                     Point(x + 0.375*w, y + 0.625*h), 
                     Point(x + 0.375*w, y + 0.5*h))
    spike2.setFill("red4")
    spike2.draw(win)

    spike3 = Polygon(Point(x + 0.5*w, y + 0.125*h), 
                     Point(x + 0.375*w, y + 0.5*h), 
                     Point(x + 0.625*w, y + 0.5*h))
    spike3.setFill("red4")
    spike3.draw(win)

    spike4 = Polygon(Point(x + 0.875*w, y + 0.375*h), 
                     Point(x + 0.625*w, y + 0.5*h), 
                     Point(x + 0.625*w, y + 0.625*h))
    spike4.setFill("red4")
    spike4.draw(win)

    spike5 = Polygon(Point(x + 0.625*w, y + 0.625*h), 
                     Point(x + 0.8125*w, y + 0.8125*h), 
                     Point(x + 0.53125*w, y + 0.75*h))
    spike5.setFill("red4")
    spike5.draw(win)

    fillIn = Polygon(Point(x + 0.375*w, y + 0.625*h), 
                     Point(x + 0.375*w, y + 0.5*h),
                     Point(x + 0.625*w, y + 0.5*h), 
                     Point(x + 0.625*w, y + 0.625*h), 
                     Point(x + 0.5*w, y + 0.75*h))
    fillIn.setFill("red4")
    fillIn.draw(win)

    stem = Rectangle(Point(x + 0.46875*w, y + 0.75*h), 
                      Point(x + 0.53125*w, y + h))
    stem.setFill("red4")
    stem.draw(win)



def drawPumpkin(x, y, w, h, pumpkinColor, win):

    parts = []   # create an empty list to add left, right, etc.

    left = Oval(Point(x+0.125*w, y + 0.21875*h),    # top left of invisible rectangle
                Point(x + 0.5*w, y + 0.78125*h))   # bottom right of invisible rectangle
    left.setFill(pumpkinColor)
    left.setOutline(pumpkinColor)
    left.draw(win)
    parts.append(left)   # adds left to the list "part"

    right = Oval(Point(x+0.5*w, y + 0.78125*h), 
                      Point(x + 0.875*w, y + 0.21875*h))
    right.setFill(pumpkinColor)
    right.setOutline(pumpkinColor)
    right.draw(win)
    parts.append(right)

    middle = Oval(Point(x+0.25*w, y + 0.21875*h),   
                      Point(x + 0.75*w, y + 0.78125*h))   
    middle.setFill(pumpkinColor)
    middle.setOutline(pumpkinColor)
    middle.draw(win)
    parts.append(middle)

    stem = Rectangle(Point(x + 0.46875*w, y + 0.0625*h), 
                      Point(x + 0.53125*w, y + 0.25*h))
    stem.setFill("green4")
    stem.draw(win)
    parts.append(stem)

    leftEye = Polygon(Point(x + 0.375*w, y + 0.33*h),
                      Point(x + 0.33*w, y + 0.41*h),
                      Point(x + 0.41*w, y + 0.41*h))
    leftEye.setFill("gray1")
    leftEye.draw(win)
    parts.append(leftEye)

    rightEye = Polygon(Point(x + 0.625*w, y + 0.33*h),
                       Point(x + 0.58*w, y + 0.41*h),
                       Point(x + 0.66*w, y + 0.41*h))
    rightEye.setFill("gray1")
    rightEye.draw(win)
    parts.append(rightEye)

    return parts   # list all parts



if __name__ == "__main__":   # only if directly executed by the python interpreter (not imported)
    main()   # calls and starts the main function (entry point)
