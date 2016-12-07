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

squares = [(0.0,1.0,random.random()*2),
           (1.0,1.0,random.random()*2),
           (0.0,0.0,random.random()*2),
           (1.0,0.0,random.random()*2)]


#Entry point
dsquare.diamondSquare(squares, [], [], 0, 1, 85)


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
