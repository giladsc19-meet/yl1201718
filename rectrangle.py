from turtle import *
import random

class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle. __init__(self)
		
		register_shape("myshape", ((width,0), (width,height), (0,height), (0,0)))
		self.shape("myshape")
		self.setheading(90)

a = Rectangle(100,50)
mainloop()



