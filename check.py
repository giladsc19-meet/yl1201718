from turtle import *
import random
import time

colormode(255)
tracer(0)
hideturtle()

class Circle(Turtle):
	def __init__(self,x,y,dx,dy,radius):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)

	def move(self):
		curentx = self.xcor()
		curenty = self.ycor()
		self.goto(curentx + self.dx,curenty + self.dy)

my_x = random.randint(-100,100)
my_y = random.randint(-100,100)
circle1 = Circle(my_x,my_y,1,1,60)

my_x = random.randint(-100,100)
my_y = random.randint(-100,100)
circle2 = Circle(my_x,my_y,1,1,60)

while True:
	circle1.move()
	circle2.move()
	getscreen().update()
	time.sleep(0.01)

mainloop()