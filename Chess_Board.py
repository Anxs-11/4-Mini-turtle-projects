
#     *** Chess Board using turtle ***

import turtle
l=int(input("enter side : ")) #enter side of each box
ch=turtle.Turtle()
ch.speed(0)
ch.hideturtle()
def sqau(l):
    for i in range(4):
        ch.pendown()
        ch.forward(l)
        ch.left(90)
        
x=-650
y=-450
c=0
while(1):
    ch.penup()
    ch.goto(x,y)
    ch.begin_fill()
    if c%2==0:
        ch.fillcolor("black")   
    else:
        ch.fillcolor("white")   
    sqau(l)
    ch.end_fill()
    x=x+l
    c=c+1
    if x==l*8-650:
        x=-650
        y=y+l
        c=c+1
       
    if y==l*8-450:
        break
    

turtle.done()