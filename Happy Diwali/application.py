# 									Happy Diwali

import os
import time
import turtle
import winsound
from customizer import CharacterWriter, star, spiral

def func():
	# Turtle Window
	win = turtle.Screen()
	win.setup(600,600)
	diyas = ['diyas/'+file for file in os.listdir('diyas/')]
	fireworks = ['fireworks/'+file for file in os.listdir('fireworks/')]
	for diya in diyas:
		win.addshape(diya)
	for firework in fireworks:
		win.addshape(firework)

	# Text Writer
	pen = CharacterWriter(shape='turtle')
	pen.up()
	pen.goto((-120,130))
	pen.down()
	pen.write_h('red')

	pen.up()
	pen.right(90)
	pen.forward(30)
	pen.down()
	pen.write_a('green')

	pen.up()
	pen.left(180)
	pen.forward(80)
	pen.right(90)
	pen.forward(70)
	pen.left(90)
	pen.down()
	pen.write_p('blue')

	pen.up()
	pen.left(90)
	pen.forward(80)
	pen.down()
	pen.write_p('orange')

	pen.up()
	pen.left(90)
	pen.forward(100)
	pen.down()
	pen.write_y('lime')

	pen.up()
	pen.goto((-250, -130))
	pen.right(90)
	pen.down()
	pen.write_d('navy')

	pen.up()
	pen.right(180)
	pen.forward(110)
	pen.down()
	pen.write_i('skyblue')
	pen.left(90)
	pen.write_i('skyblue')

	pen.up()
	pen.left(90)
	pen.forward(10)
	pen.down()
	pen.write_w('yellow')

	pen.up()
	pen.right(180)
	pen.forward(100)
	pen.left(90)
	pen.forward(30)
	pen.down()
	pen.write_a('gray')

	pen.up()
	pen.left(180)
	pen.forward(80)
	pen.right(90)
	pen.forward(65)
	pen.left(90)
	pen.down()
	pen.write_l('magenta')

	pen.up()
	pen.forward(30)
	pen.down()
	pen.write_i('chocolate')


	# Stars
	pen.width(2)
	pen.speed(0)

	pen.color('gold')
	star(pen)
	pen.up()
	pen.goto((100, 60))
	pen.color('red')
	pen.down()
	star(pen)
	pen.up()
	pen.goto((-60, 10))
	pen.color('purple')
	pen.down()
	star(pen)
	pen.up()
	pen.goto((-150, -210))
	pen.color('skyblue')
	pen.down()
	star(pen)
	pen.up()
	pen.goto((0, -260))
	pen.color('green')
	pen.down()
	star(pen)
	
	# Spirals
	pen.up()
	pen.goto(-280,-270)
	pen.color('red')
	pen.down()
	spiral(pen)
	
	pen.up()
	pen.goto(280,270)
	pen.color('turquoise')
	pen.down()
	spiral(pen)

	# Animations
	win.tracer(False)

	d = turtle.Turtle()
	d.speed(0)
	d.up()
	d.goto(-210,70)  
	dindex = 1

	f1 = turtle.Turtle()
	f1.speed(0)
	f1.up()
	f1.goto(200,-220)  

	f2 = turtle.Turtle()
	f2.speed(0)
	f2.up()
	f2.left(45)
	f2.goto(-200,260)

	findex = 1

	winsound.PlaySound('assets/fireworks.wav',winsound.SND_ASYNC)
	while True:
		win.update()
		d.shape(f'diyas/diya{dindex}.gif')
		f1.shape(f'fireworks/firework{findex}.gif')
		f2.shape(f'fireworks/firework{findex}.gif')
		dindex = (dindex + 1) % 49
		findex = (findex + 1) % 12
		if dindex == 0:
			dindex = 1
		if findex == 0:
			findex = 1
		time.sleep(0.05)

if __name__ == '__main__':	
	try:
		func()
		turtle.done()
	except:
		pass