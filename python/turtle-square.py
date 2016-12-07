import random
from turtle import *
import dsquare

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

squares = [(0.0,1.0,random.random()*3),
           (1.0,1.0,random.random()*3),
           (0.0,0.0,random.random()*3),
           (1.0,0.0,random.random()*3)]


#Entry point
dsquare.diamondSquare(squares, [], [], 0, 1, 85)


#TURTLE PAINT
i=0
turtle.hideturtle()
while(i<len(squares)):
    turtle.penup()
    turtle.goto(squares[i][0]*100,squares[i][1]*100)
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
    turtle.shapesize(0.3125,0.3125,1)
    turtle.pencolor(colorR,colorG,colorB)
    turtle.fillcolor(colorR,colorG,colorB)
    turtle.stamp()
    #turtle.dot(8, colorR, colorG, colorB)
    i+=1

stop = input("Stop the program? (y/n) ")
