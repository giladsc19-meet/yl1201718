from turtle import *
import random
import math

class Rectangle(Turtle):
	def __init__(self,dx,dy,width,height):
		Turtle. __init__(self)
		
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.width=width
		self.height=height