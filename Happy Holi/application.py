# 									Happy Diwali

import os
import time
import turtle

def func():
	# Turtle Window
	win = turtle.Screen()
	win.setup(600,600)
	holi_s = ['holi/'+file for file in os.listdir('holi/')]
	dribbles = ['dribbles/'+file for file in os.listdir('dribbles/')]
	fireworks = ['fireworks/'+file for file in os.listdir('fireworks/')]
	for firework in fireworks:
		win.addshape(firework)
	for dribble in dribbles:
		win.addshape(dribble)
	for holi in holi_s:
		win.addshape(holi)

	# Animations
	win.tracer(False)

	h = turtle.Turtle()
	h.speed(0)
	h.up()
	h.goto(-10,0)  

	f1 = turtle.Turtle()
	f1.speed(0)
	f1.up()
	f1.goto(200,-220)  

	f2 = turtle.Turtle()
	f2.speed(0)
	f2.up()
	f2.left(45)
	f2.goto(-200,260)

	d1 = turtle.Turtle()
	d1.speed(0)
	d1.up()
	d1.goto(-200,-220) 

	d2 = turtle.Turtle()
	d2.speed(0)
	d2.up()
	d2.goto(200,260) 

	findex = 1
	hindex = 1
	dindex = 1
	rindex = 1

	while True:
		win.update()
		h.shape(f'holi/holi{hindex}.gif')
		f1.shape(f'fireworks/firework{findex}.gif')
		f2.shape(f'fireworks/firework{findex}.gif')
		d1.shape(f'dribbles/dribble{dindex}.gif')
		d2.shape(f'dribbles/dribble{dindex}.gif')
		findex = (findex + 1) % 12
		dindex = (dindex + 1) % 366
		rindex += 1
		if rindex % 10 == 0:
			hindex = (hindex + 1) % 3
		if findex == 0:
			findex = 1
		if hindex == 0:
			hindex = 1
		if dindex == 0:
			dindex = 1
		time.sleep(0.05)

if __name__ == '__main__':	
	try:
		func()
		turtle.done()
	except:
		pass