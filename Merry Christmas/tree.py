import turtle

dx = 190

def draw_tree():
	circle = turtle.Turtle()
	circle.shape('circle')
	circle.color('red')
	circle.speed(0)
	circle.up()

	square = turtle.Turtle()
	square.shape('square')
	square.color('green')
	square.speed(0)
	square.up()

	k = 0
	for i in range(1,17):
		y = 30 * i
		for j in range(i-k):
			x = 30 * j
			square.goto(x-dx, 280 - y)
			square.stamp()
			square.goto(-x-dx, 280 - y)
			square.stamp()

		if i % 4 == 0:
			x = 30 * (j+1)
			circle.color('red')
			circle.goto(-x-dx,-y+280)
			circle.stamp()
			circle.goto(x-dx,-y+280)
			circle.stamp()
			k += 2

		if i % 4 == 3:
			x = 30 * (j+1)
			circle.color('yellow')
			circle.goto(-x-dx,-y+280)
			circle.stamp()
			circle.goto(x-dx,-y+280)
			circle.stamp()

	square.color('brown')
	for i in range(17,20):
		y = 30 * i
		for j in range(3):
			x = 30 * j
			square.goto(x-dx,-y+280)
			square.stamp()
			square.goto(-x-dx,-y+280)
			square.stamp()

def draw_star(t, color):
	t.color(color)
	t.begin_fill()
	for k in range(5):
	        t.forward(13)
	        t.right(144)
	        t.forward(13)
	t.end_fill()

