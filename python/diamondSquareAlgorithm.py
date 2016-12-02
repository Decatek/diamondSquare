import random
from turtle import *

#Israel Nebot, 2016
#israel.nebot@gmail.com
#Feel free to contribute / add / tweak!

#Turtle declaration
turtle = Turtle()
screen = Screen()
screen.colormode(255)
screenx = 300
screeny = 300
screen.setup(400,400)
screen.screensize(screenx, screeny)
turtle.speed(10)
turtle.hideturtle()


def diamondSquare(squares, middlePoints, edgeMiddles, squareIndex, iteration, iterations):
    
    if(iteration<=iterations):
        
        edgeMiddles = []
        middlePoints = []
        
    #Step #1: Get the middle point of the square given at first. Using any two vertices works.
 
        squareMiddlePoint = ((squares[squareIndex][0] + squares[squareIndex+1][0])/2, #X POSITION
                             (squares[squareIndex][1]+squares[squareIndex+3][1])/2, #Y POSITION
                             ((squares[squareIndex][2]+
                               squares[squareIndex+1][2]+
                               squares[squareIndex+2][2]+
                               squares[squareIndex+3][2])/4) +random.random()*2 #AVERAGE OF HEIGHTS
                             )
        
        middlePoints.append(squareMiddlePoint)
        
    #Step #2: Get the middle point of the edges.

                        #1-0
        edgeMiddles = [((squares[squareIndex+1][0]+squares[squareIndex][0])/2,
                        squares[squareIndex+1][1],
                        (squares[squareIndex+1][2]+squares[squareIndex][2])/2)
                       ,#0-2
                       (squares[squareIndex][0],
                        (squares[squareIndex][1]+squares[squareIndex+2][1])/2,
                        (squares[squareIndex][2]+squares[squareIndex+2][2])/2)
                       ,#3-2
                       ((squares[squareIndex+3][0]+squares[squareIndex+2][0])/2,
                        squares[squareIndex+3][1],
                        (squares[squareIndex+3][2]+squares[squareIndex+2][2])/2)
                       ,#1-3
                       ((squares[squareIndex+1][0],
                         (squares[squareIndex+1][1]+squares[squareIndex+3][1])/2,
                         (squares[squareIndex+1][2]+squares[squareIndex+3][2])/2))
                       ]
        
        #Step #3: Append the newly created inner squares to the squares array
        
        #new Square 1
        squares.append(squares[squareIndex])
        squares.append(edgeMiddles[0])
        squares.append(edgeMiddles[1])
        squares.append(middlePoints[0])
        
        
        #new Square 2
        squares.append(edgeMiddles[0])
        squares.append(squares[squareIndex+1])
        squares.append(middlePoints[0])
        squares.append(edgeMiddles[3])
  
        #new Square 3
        squares.append(edgeMiddles[1])
        squares.append(middlePoints[0])
        squares.append(squares[squareIndex+2])
        squares.append(edgeMiddles[2])
        #new Square 4
        squares.append(middlePoints[0])
        squares.append(edgeMiddles[3])
        squares.append(edgeMiddles[2])
        squares.append(squares[squareIndex+3])


        #Step #4, Recursively call the function on each new square.
        
        return diamondSquare(squares, middlePoints, edgeMiddles, squareIndex+4, iteration+1, iterations)
    
    
        
        


#FIRST SQUARE:
                            
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


                            
diamondSquare(squares, [], [], 0, 1, 85) #85 -> Full map coverage (more: More dots, more definition)
                                         #                        (less: Less dots, less definition)


#TURTLE PAINT
i=0
while(i<len(squares)):
    
    turtle.penup()
    turtle.goto(squares[i][0]*125,squares[i][1]*125)
    height = squares[i][2]
    if(abs(0+round(height*50)-80) <=255): #So we don't get colours with >255 (ERROR!)
        turtle.dot(10, 0, abs(0+round(height*50)-20),0) # Size, R, G, B
    else:
        turtle.dot(10, 0, abs(0+round(height*50)-40),0)
    i+=1

    

