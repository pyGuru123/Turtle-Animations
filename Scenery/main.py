import turtle
import random

WIDTH = 800
HEIGHT = 600
WIDTHHALF = WIDTH // 2
HEIGHTHALF = HEIGHT // 2

def draw_stars(t, x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	t.begin_fill()
	for i in range(5):
		t.forward(15)
		t.right(144)
	t.end_fill()

def draw_moon(t):
	t.penup()
	t.goto(-250, -HEIGHT//2 + 100)
	t.pendown()
	t.begin_fill()
	t.circle(30)
	t.end_fill()

angle = 1
if __name__ == '__main__':
	win = turtle.Screen()
	win.setup(width=800,height=600)
	win.bgcolor('navy')

	# stars & moon
	star = turtle.Turtle()
	star.speed(0)
	star.pencolor('yellow')
	star.color('gold')
	star.hideturtle()

	# for i in range(30):
	# 	x = random.randint(-WIDTHHALF, WIDTHHALF)
	# 	y = random.randint(-80, HEIGHTHA:F)
	# 	draw_stars(star, x, y)
	draw_moon(star)
	

	# river and rocks
	river = turtle.Turtle()
	river.speed(0)
	river.pencolor('cyan')
	river.color('cyan')
	river.penup()
	river.goto(-WIDTHHALF, -HEIGHTHALF)
	river.pendown()
	river.left(90)
	river.begin_fill()
	river.forward(120)
	river.right(90)
	for i in range(45):
		angle *= -1
		river.forward(10)
		river.left(angle)
	river.right(120)
	river.forward(150)
	river.end_fill()

	turtle.done()