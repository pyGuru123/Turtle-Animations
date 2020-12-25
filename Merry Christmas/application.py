import os
import turtle
import winsound
from tree import draw_tree, draw_star

win = turtle.Screen()
win.setup(980,650)
win.bgcolor('black')
win.title('Merry Christmas')

wishes = ['wishes/'+file for file in os.listdir('wishes/')]
santas = ['santas/'+file for file in os.listdir('santas/')]
bells = ['bells/'+file for file in os.listdir('bells/')]
for wish in wishes:
	win.addshape(wish)
for santa in santas:
	win.addshape(santa)
for bell in bells:
	win.addshape(bell)

def func():
	winsound.PlaySound('assets/music.wav',winsound.SND_ASYNC)
	star = turtle.Turtle()
	star.speed(0)
	star.hideturtle()
	star.up()
	star.goto(-190, 290)
	star.down() 

	# drawing tree
	draw_star(star, 'red')
	draw_tree()

	# Animation

	w = turtle.Turtle()
	w.speed(0)
	w.up()
	w.goto(290,-220)

	s = turtle.Turtle()
	s.speed(0)
	s.up()
	s.goto(290,220)

	b = turtle.Turtle()
	b.speed(0)
	b.up()
	b.goto(300,0)


	windex = 1
	sindex = 1

	num = 0
	colors = ['Yellow', 'Red', 'Gold', 'Orange']

	while True:
		c = colors[num % 4]
		draw_star(star, c)
		num += 1

		w.shape(f'wishes/wish{windex}.gif')
		s.shape(f'santas/santa{sindex}.gif')
		b.shape(f'bells/bell{windex}.gif')

		windex = (windex + 1) % 4
		sindex = (sindex + 1) % 3
		if windex == 0:
			windex = 1
		if sindex == 0:
			sindex = 1

try:
	func()
	turtle.done()
except:
	pass