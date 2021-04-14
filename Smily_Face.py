
#      *** Smily Face using turtle ***

import turtle
emoji=turtle.Turtle()
x=0
y=-100
emoji.hideturtle()
# emoji.speed(0)

#  *** for Yellow Circle ***

emoji.pensize(4)
emoji.penup()
emoji.goto(x,y)
emoji.pendown()
emoji.begin_fill()
emoji.screen.colormode(255)
emoji.fillcolor(255,240,18)
emoji.circle(200)
emoji.end_fill()

#   *** for eyes ***

emoji.penup()
emoji.goto(100,130)
emoji.pendown()
emoji.pensize(1)
emoji.begin_fill()
emoji.fillcolor("black")
emoji.circle(20)
emoji.penup()
emoji.goto(-100,130)
emoji.pendown()
emoji.circle(20)
emoji.end_fill()

#  *** for face ***

emoji.penup()
emoji.goto(0,-40)
emoji.pendown()
emoji.pensize(4)
emoji.circle(120,60)
emoji.penup()
emoji.goto(0,-40)
emoji.left(300)
emoji.pendown()
emoji.circle(120,-60)


turtle.done()