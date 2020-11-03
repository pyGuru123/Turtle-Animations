# 								Night sky animation

import turtle
import random

# window setup

win = turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor('black')

colors = ['red','blue','orange','yellow','magenta','purple','peru','ivory','dark orange']

# Turtle objects

moon = turtle.Turtle()
moon.hideturtle()

star = turtle.Turtle()
star.speed(0)
star.hideturtle()

text = turtle.Turtle()
text.speed(6)
text.hideturtle()

# Functions

def draw_moon(pos,color):
	x,y = pos

	moon.color(color)
	moon.begin_fill()
	moon.penup()
	moon.goto(x,y)
	moon.pendown()
	moon.circle(50)
	moon.end_fill()


def stars(x,y,color,length):	
	star.color(color)

	star.penup()
	star.goto(x,y)
	star.pendown()

	star.begin_fill()
	for i in range(5):
		star.forward(length)
		star.right(144)
		star.forward(length)
	star.end_fill()

def random_pos():
	return random.randint(-390,390), random.randint(-200,290)

def random_length():
	return random.randint(5,25)

def write_text(color):
	text.color(color)

	text.penup()
	text.goto(-180,-270)
	text.pendown()
	style = ('Stencil Std Bold',50,'normal')
	text.write('Good Night',font=style,move=True)


# Main program

draw_moon((-300,170),'white')
draw_moon((-278,183),'black')

while True:
	color = random.choice(colors)
	x ,y = random_pos()
	length = random_length()

	stars(x,y,color,length)
	write_text(color)
	# moon.clear()

turtle.done()