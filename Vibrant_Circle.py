
 #    *** Vibrant Circle Using turtle ***

import turtle
k=turtle.Turtle()
k.screen.bgcolor("black")
k.pencolor("green")
k.penup()
k.goto(0,200)
k.pendown()
a=0
b=0
k.speed(0)
while(1):
    k.forward(a)
    k.right(b)
    a+=3
    b+=1
    k.hideturtle()
    if b==210:
        break

turtle.done()