import random
from turtle import *
import dsquare
import timeit




turtle = Turtle()
screen = Screen()
screen.colormode(255)
screen.title("Diamond-Square Algorithm (v1.0)")
screenx = 300
screeny = 300
screen.setup(400,400)
screen.screensize(screenx, screeny)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
bgcolor(255,255,255)




#Create the first square...
squares = [(0.0,1.0,random.random()*2),
           (1.0,1.0,random.random()*2),
           (0.0,0.0,random.random()*2),
           (1.0,0.0,random.random()*2)]


#Do the diamond-square algorithm to generate the heightmap
dsquare.diamondSquare(squares, [], [], 0, 1, 85)



#Draw the heightmap
def draw(i):
    
    places = []
    drawn = 0
    while(i<len(squares)):
        
        turtle.goto((squares[i][0]*300)-160,(squares[i][1]*300)-150)
        currentPos = turtle.pos()
        
        if(currentPos not in places):
            
            places.append(currentPos)
            height = squares[i][2]

            
            #Water & coast
            
            if(height <= 1):

                
                colorR = 0
            
                colorG = round(66 - 2*height)
                if(colorG>=255): colorG = 255
                if(colorG<=0): colorG = 0
            
                colorB = round(255 - (255*height))
                if(colorB>=255): colorB = 255
                if(colorB<=0): colorB = 0

            #Land
                
            elif(height > 1 and height <= 2): 
            
                colorR = round(10 + height) 
                if(colorR>=255): colorR = 255
                if(colorR<=0): colorR = 0
            
                colorG = round(60 + 25*height) 
                if(colorG>=255): colorG = 255
                if(colorG<=0): colorG = 0
            
                colorB = round(10 + height) 
                if(colorB>=255): colorB = 255
                if(colorB<=0): colorB = 0

            #Mountains
                
            else:
                
                colorR = round(60 + 3*height) 
                if(colorR>=255): colorR = 255
                if(colorR<=0): colorR = 0
            
                colorG = round(50 + 2*height)
                if(colorG>=255): colorG = 255
                if(colorG<=0): colorG = 0
            
                colorB = round(40 + height)
                if(colorB>=255): colorB = 255
                if(colorB<=0): colorB = 0

            turtle.shape("square")
            turtle.shapesize(0.9,0.9,1)
            turtle.color(colorR,colorG,colorB)
            turtle.stamp()
            drawn+=1
            i+=1
            
        else:
            i+=1
            
    stop = timeit.default_timer()
    print("Map drawn in {0} seconds ({1} squares in total, ~{2} squares per second)".format(round(stop-start), drawn, (round(drawn/(round(stop-start))))))


if __name__ == "__main__":
    start = timeit.default_timer()
    draw(0)
