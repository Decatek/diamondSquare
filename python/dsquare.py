import random
import math

#Israel Nebot, 2016
#http://israelnebot.github.io
#Feel free to collaborate / tweak / mod as you want

def diamondSquare(squares, middlePoints, edgeMiddles, squareIndex, iteration, iterations):
    
    if(iteration<=iterations):
        edgeMiddles = []
        middlePoints = []
        
        #Step #1: Get the middle point of the square given at first
        randomValue = (random.random() -0.5)*2
            
        squareMiddlePoint = ((squares[squareIndex][0] + squares[squareIndex+1][0])/2, #X POSITION
                             (squares[squareIndex][1]+squares[squareIndex+3][1])/2, #Y POSITION
                             ((squares[squareIndex][2]+
                               squares[squareIndex+1][2]+
                               squares[squareIndex+2][2]+
                               squares[squareIndex+3][2])/4) + randomValue #AVERAGE OF HEIGHTS
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
    
