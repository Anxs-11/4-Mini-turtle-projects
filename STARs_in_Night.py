
#       *** Create infinite  Stars in Night Sky ***

import turtle
import random
n=turtle.Turtle()
n.screen.title("Night Sky")
n.screen.bgcolor("black")
n.screen.screensize(800,500,bg="black")
n.pencolor("white")
n.speed(0)
n.hideturtle()
def star():
    for i in range(5):
        n.pendown()
        n.forward(10)
        n.right(144)
        
n.screen.colormode(255) #changing color mode from name of the color to the rbg format
while(1):
    x=random.randint(-600,600)
    y=random.randint(-600,600)
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    n.pencolor(r,b,g)
    n.penup()
    n.goto(x,y)
    star()
turtle.done()


