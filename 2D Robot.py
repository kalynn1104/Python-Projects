from graphics import *

def colsInGrid():  
    # Returns the number of columns in the grid
    return len(grid[0])   # length of top row


def rowsInGrid():  
    # Returns the number of rows in the grid
    return len(grid)


def getRobotLocation():
    # Looks through the grid to find where the robot (1) is
    for r in range(rowsInGrid()):
        for c in range(colsInGrid()):
            if grid[r][c] == 1:
                return (r, c)  # return as (row, col)


def isOnGoal():
    # Checks if the robot is on the goal
    return getRobotLocation() == goalLocation


def rotateRight():
    # Turns the robot 90 degrees clockwise
    global facing
    if facing == "R":
        facing = "D"
    elif facing == "D":
        facing = "L"
    elif facing == "L":
        facing = "U"
    else:  # facing == "U"
        facing = "R"


def rotateLeft():
    # Turns the robot 90 degrees counter-clockwise
    global facing
    if facing == "R":
        facing = "U"
    elif facing == "U":
        facing = "L"
    elif facing == "L":
        facing = "D"
    else:  # facing == "D"
        facing = "R"


def canMove(direction):
    # Checks if the robot can move in the given direction
    r, c = getRobotLocation()

    if direction == "R":
        c += 1
    elif direction == "L":
        c -= 1
    elif direction == "U":
        r -= 1
    else:  # direction == "D"
        r += 1

    # Check if new position is out of the grid
    if r < 0 or r >= rowsInGrid() or c < 0 or c >= colsInGrid():
        return False

    # Can move if the square is empty (0) or goal (2)
    return grid[r][c] == 0 or grid[r][c] == 2


def moveForward():
    # This function moves the robot one square forward in the direction it is currently facing.
    # It first checks if the move is possible using canMove().
    
    r, c = getRobotLocation()  
    # Get the robot's current position:
    # r = current row number
    # c = current column number

    if canMove(facing):
        # If the robot can move in the direction it is facing (no wall):
        
        # Remove the robot from its current square, but only if it is not standing on the goal
        if (r, c) != goalLocation:
            grid[r][c] = 0  # Set the current square to empty (0)

        # Update the robot's position based on which direction it is facing
        if facing == "R":  # Robot is facing right
            c += 1          # Move one column to the right
        elif facing == "L":  # Robot is facing left
            c -= 1          # Move one column to the left
        elif facing == "U":  # Robot is facing up
            r -= 1          # Move one row up
        else:  # facing == "D", Robot is facing down
            r += 1          # Move one row down

        # Place the robot in the new square by setting the grid value to 1
        grid[r][c] = 1
    else:
        # If the robot cannot move (there's a wall):
        print("unable to move")  


def displayRobotGrid():
    # Shows the grid in the console and graphics window
    for row in grid:
        print(row)

    # Draw the grid squares
    for r in range(rowsInGrid()):
        for c in range(colsInGrid()):
            sq = Rectangle(Point(20*c, 20*r),
                           Point(20*c + 20, 20*r + 20))

            if (r, c) == goalLocation:
                sq.setFill("yellow")  # highlight goal
            else:
                sq.setFill("white")  # normal cell
            sq.draw(win)

    # Draw the robot as a triangle based on facing direction
    row, col = getRobotLocation()

    if facing == "R": 
        tri = Polygon(Point(20*col, 20*row),
                      Point(20*col, 20*row + 20),
                      Point(20*col + 20, 20*row + 10))
    elif facing == "L": 
        tri = Polygon(Point(20*col + 20, 20*row),
                      Point(20*col + 20, 20*row + 20),
                      Point(20*col, 20*row + 10))
    elif facing == "U": 
        tri = Polygon(Point(20*col, 20*row + 20),
                      Point(20*col + 20, 20*row + 20),
                      Point(20*col + 10, 20*row))
    else:  # facing == "D"
        tri = Polygon(Point(20*col, 20*row),
                      Point(20*col + 20, 20*row),
                      Point(20*col + 10, 20*row + 20))

    tri.setFill("black")  # robot color
    tri.draw(win)


def setup():
    # Sets up the grid, robot, goal, and window
    global win, grid, facing, goalLocation

    # 0 = empty, 1 = robot, 2 = goal
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],    # GOAL
            [0, 0, 0, 0, 0, 0, 0, 1, 0],    # ROBOT
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    facing = "R"  # robot starts facing right
    goalLocation = (1, 4)  # save goal coordinates

    # Set window size based on grid
    gridHeight = 350
    if len(grid) * 20 > 200:
        gridHeight = len(grid)*20 + 150
        
    gridWidth = 400
    if len(grid[0]) * 20 > 400:
        gridWidth = len(grid[0])*20 + 40

    win = GraphWin("Robot", gridWidth, gridHeight, autoflush=False)
    win.setBackground("green")  # background color

    # Instructions on the window
    directionText = Text(Point(win.getWidth()/2, win.getHeight()/6*5),
        "Use right arrow or D to rotate clockwise\n"+
        "Use left arrow or A to rotate counterclockwise\n" + 
        "Use up arrow or W to move in that direction\n" +
        "Use S to exit")
    directionText.setFill("white")
    directionText.draw(win)


def main(): 
    setup()
    over = False
    while not over:
        displayRobotGrid()
        key = win.getKey() #waits for user key press
        if key == 's': #if user presses 's' key, closes window
            over = True 
            win.close()
        elif key == 'd' or key == "Right":
            rotateRight()
        elif key == 'a' or key == "Left":
            rotateLeft()
        elif key == 'w' or key == "Up":
            moveForward()

        # Check if robot reached goal
        if isOnGoal():
            print("YOU REACHED THE GOAL!")
            over = True
            win.close()


# Run the program
if __name__ == "__main__":
    main()
