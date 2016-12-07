import random
from turtle import *


#Israel Nebot, 2016
#http://israelnebot.github.io
#Feel free to collaborate / tweak / mod as you want




def diamondSquare(squares, middlePoints, edgeMiddles, squareIndex, iteration, iterations):
    
    if(iteration<=iterations):
        
        edgeMiddles = []
        middlePoints = []
        
        #Step #1: Get the middle point of the square given at first
 
        squareMiddlePoint = ((squares[squareIndex][0] + squares[squareIndex+1][0])/2, #X POSITION
                             (squares[squareIndex][1]+squares[squareIndex+3][1])/2, #Y POSITION
                             ((squares[squareIndex][2]+
                               squares[squareIndex+1][2]+
                               squares[squareIndex+2][2]+
                               squares[squareIndex+3][2])/4) +random.random()*2 #AVERAGE OF HEIGHTS
                             )
        
        middlePoints.append(squareMiddlePoint)
        
        #Step #2: Get the middle point of the edges

                        #1----0
        edgeMiddles = [((squares[squareIndex+1][0]+squares[squareIndex][0])/2,
                        squares[squareIndex+1][1],
                        (squares[squareIndex+1][2]+squares[squareIndex][2])/2)
                       ,#0----2
                       (squares[squareIndex][0],
                        (squares[squareIndex][1]+squares[squareIndex+2][1])/2,
                        (squares[squareIndex][2]+squares[squareIndex+2][2])/2)
                       ,#3----2
                       ((squares[squareIndex+3][0]+squares[squareIndex+2][0])/2,
                        squares[squareIndex+3][1],
                        (squares[squareIndex+3][2]+squares[squareIndex+2][2])/2)
                       ,#1----3
                       ((squares[squareIndex+1][0],
                         (squares[squareIndex+1][1]+squares[squareIndex+3][1])/2,
                         (squares[squareIndex+1][2]+squares[squareIndex+3][2])/2))
                       ]

        
        #Step #3: Create new squares & append them to the squares array
        
        #The problem comes here: we are reusing the vertices of the first
        #square. This way we'll have too many repeated vertices in the end.
        #This part needs inspection.
        
        #TOP LEFT subSQUARE
        squares.append(squares[squareIndex])
        squares.append(edgeMiddles[0])
        squares.append(edgeMiddles[1])
        squares.append(middlePoints[0])
        
        #TOP RIGHT subSQUARE
        squares.append(edgeMiddles[0])
        squares.append(squares[squareIndex+1])
        squares.append(middlePoints[0])
        squares.append(edgeMiddles[3])
  
        #BOTTOM LEFT subSQUARE
        squares.append(edgeMiddles[1])
        squares.append(middlePoints[0])
        squares.append(squares[squareIndex+2])
        squares.append(edgeMiddles[2])
        
        #BOTTOM RIGHT subSQUARE
        squares.append(middlePoints[0])
        squares.append(edgeMiddles[3])
        squares.append(edgeMiddles[2])
        squares.append(squares[squareIndex+3])

        #Step 4: Recursively call the function on each subSQUARE as if
        #it was the first square.
        
        return diamondSquare(squares, middlePoints, edgeMiddles, squareIndex+4, iteration+1, iterations)
    
        
turtle = Turtle()
screen = Screen()
screen.colormode(255)
screenx = 300
screeny = 300
screen.setup(400,400)
screen.screensize(screenx, screeny)
turtle.speed(10)


##DEFINED SQUARE:
                            
##  (0)   (1)
##   o-----o
##   |     |
##   |     |
##   o-----o
##  (2)   (3)
#Assuming Z as height
    
squares = [(0.0,1.0,random.random()*2),
           (1.0,1.0,random.random()*2),
           (0.0,0.0,random.random()*2),
           (1.0,0.0,random.random()*2)]


#Entry point
diamondSquare(squares, [], [], 0, 1, 85)


#TURTLE PAINT
i=0
turtle.hideturtle()
while(i<len(squares)):
    
    turtle.penup()
    turtle.goto(squares[i][0]*125,squares[i][1]*125)
    height = squares[i][2]
    turtle.pensize(0.5)
    turtle.dot(round(height)*3, 0, 0, 0)
    i+=1

    

