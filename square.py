from turtle import *
import random

colormode(255)
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)

class Square(Turtle):

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