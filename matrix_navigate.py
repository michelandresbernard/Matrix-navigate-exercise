## Coordinates (0,0)(x,y) are the top left element of the matrix 
matrix = [  [1, 2, 3, 4], 
            [5, 6, 7, 8],
            [9, 10, 11, 12], 
            [13, 14, 15, 16], 
            ]
currentposition_x = 0 
currentposition_y = 0
def moveright ():
    global currentposition_x, currentposition_y
    if currentposition_y < len(matrix) -1:
        currentposition_y = currentposition_y + 1
        print ("You are now in:", matrix [currentposition_x][currentposition_y], "with coordinates",currentposition_x, currentposition_y)
    else: print ("You can't leave the Matrix, you are still in ", matrix [currentposition_x][currentposition_y], "with coordinates",currentposition_x,currentposition_y) 
def moveleft ():
    global currentposition_x, currentposition_y
    if currentposition_y != 0:
        currentposition_y = currentposition_y -1
        print ("You are now in:", matrix [currentposition_x][currentposition_y],"with coordinates:", currentposition_x,currentposition_y)
    else: print ("You can't leave the Matrix, you are still in ", matrix [currentposition_x][currentposition_y], "with coordinates",currentposition_x,currentposition_y)
def moveup ():
    global currentposition_x, currentposition_y
    if currentposition_x != 0:
        currentposition_x = currentposition_x -1
        print ("You are now in:", matrix [currentposition_x][currentposition_y],"with coordinates:", currentposition_x,currentposition_y)
    else: print ("You can't leave the Matrix, you are still in ", matrix [currentposition_x][currentposition_y], "with coordinates",currentposition_x,currentposition_y)   
def movedown ():
    global currentposition_x, currentposition_y
    if currentposition_x < len(matrix)-1:
        currentposition_x = currentposition_x +1
        print ("You are now in:", matrix [currentposition_x][currentposition_y], "with coordinates: ", currentposition_x,currentposition_y)
    else: print ("You can't leave the Matrix, you are still in ", matrix [currentposition_x][currentposition_y], "with coordinates",currentposition_x,currentposition_y)   

while True:
    move_direction = input("Where do you want to move?(l,r,u,d)")
    if move_direction == "l": moveleft()
    elif move_direction == "r": moveright()
    elif move_direction == "u": moveup()
    elif move_direction == "d": movedown()
    else: print ("Please input one of the given options")

