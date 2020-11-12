import turtle

class CharacterWriter(turtle.Turtle):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.width(20)
		self.speed(8)

	def write_h(self, color):
		self.color(color)
		self.left(90)
		self.forward(100)
		self.back(50)
		self.right(90)
		self.forward(50)
		self.left(90)
		self.forward(50)
		self.back(100)

	def write_a(self, color):
		self.color(color)
		self.left(90)
		self.forward(100)
		self.right(90)
		self.forward(50)
		self.right(90)
		self.forward(100)
		self.back(50)
		self.right(90)
		self.forward(50)

	def write_p(self, color):
		self.color(color)
		self.left(90)
		self.forward(100)
		self.right(90)
		self.forward(50)
		self.right(90)
		self.forward(50)
		self.right(90)
		self.forward(50)
		self.left(90)
		self.forward(50)

	def write_y(self, color):
		self.color(color)
		self.left(90)
		self.forward(50)
		self.left(90)
		self.forward(25)
		self.right(90)
		self.forward(50)
		self.back(50)
		self.right(90)
		self.forward(50)
		self.left(90)
		self.forward(50)

	def write_d(self, color):
		self.color(color)
		self.left(90)
		self.forward(100)
		self.right(90)
		self.forward(70)
		self.right(30)
		self.forward(20)
		self.right(60)
		self.forward(70)
		self.right(30)
		self.forward(20)
		self.right(60)
		self.forward(70)

	def write_i(self, color):
		self.color(color)
		self.left(90)
		self.forward(100)

	def write_w(self, color):
		self.color(color)
		self.up()
		self.forward(30)
		self.left(90)
		self.forward(80)
		self.down()
		self.right(170)
		self.forward(90)
		self.left(120)
		self.forward(50)
		self.right(70)
		self.forward(50)
		self.left(120)
		self.forward(90)

	def write_l(self, color):
		self.color(color)
		self.left(90)
		self.forward(100)
		self.right(180)
		self.forward(100)
		self.left(90)
		self.forward(60)


def star(t):
	for i in range(8):
		t.fd(50)
		t.lt(225)	

def spiral(t):
	for i in range(30):
		t.rt(i*2)
		t.fd(i)
		t.circle(i*1.5)