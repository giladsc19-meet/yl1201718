from turtle import *
import random

colormode(255)
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)

class Shapes(Turtle):
	pass

class Rectangle(Shapes):
	def __init__(self,width,height):
		Turtle. __init__(self)
		
		register_shape("myshape", ((width,0), (width,height), (0,height), (0,0)))
		self.shape("myshape")
		self.setheading(90)

a = Rectangle(100,50)

class Square(Shapes):

	def __init__(self,size):
		Turtle. __init__(self)
		self.shapesize(size)
		self.shape('circle')
		self.size = size
		self.color(red,green,blue)

	def random_color(self):
		print(red,green,blue)

a = Square(12)
a.random_color()

mainloop()