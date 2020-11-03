# Republic day Animation
# Visit pyGuru on youTube

import turtle
import winsound

# creating background screen
win = turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor('black')

# playing music
winsound.PlaySound('anthem.wav',winsound.SND_ASYNC)


# adding image
win.addshape('ind.gif')
t = turtle.Turtle()
t.speed(2)
t.shape('ind.gif')
t.goto(-280,0)


# creating flag
stand = turtle.Turtle()
stand.color('white')
stand.shape('square')
stand.penup()
stand.setposition(-100,-280)
stand.pendown()
stand.goto(-100,280)

flag = turtle.Turtle()
flag.color('white')
flag.penup()
flag.setposition(-100,270)
flag.pendown()

length = 400
width = 80

def rect(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(length)
    flag.right(90)
    flag.forward(width)
    flag.right(90)
    flag.forward(length)
    flag.right(180)
    flag.end_fill()

rect('orange')
rect('white')
rect('green')

flag.left(90)
flag.forward(width*3)
flag.hideturtle()

# drawing wheel
wheel = turtle.Turtle()
wheel.color('blue')
wheel.penup()
wheel.width(2)
wheel.goto(100,100)
wheel.pendown()
wheel.circle(50)
wheel.penup()
wheel.goto(100,150)
wheel.pendown()
for i in range(26):
    wheel.forward(48)
    wheel.backward(48)
    wheel.right(13.8)


# writing text
text = turtle.Turtle()
text.hideturtle()
text.speed(2)

def write(message,pos,color):
    x,y = pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style = ('Stencil Std',40,'italic')
    text.write(message,font=style)

write('Happy',(60,-100),'orange')
write('Rep',(10,-160),'white')
write('ub',(124,-160),'blue')
write('lic',(203,-160),'white')
write('Day',(80,-220),'green')

turtle.done()