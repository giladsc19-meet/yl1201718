from turtle import *
import random

class Ball(Turtle):
	def __init__(self,xpos,ypos,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(xpos,ypos)
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.shape("circle")
		self.shapesize(radius/10)
		self.color(color)

	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx
		new_y = current_y + self.dy

		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		up_side_ball = new_y + self.radius
		bottom_side_ball = new_y - self.radius

		self.goto(new_x,new_y)
		if right_side_ball>=screen_width or left_side_ball<=-screen_width:
			self.dx = -self.dx
		if bottom_side_ball<=-screen_height or up_side_ball>=screen_height:
			self.dy = -self.dy


class Food(Turtle):
	def __init__(self,xpos,ypos,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(xpos,ypos)
		self.shape("circle")
		self.shapesize(10/10)
		self.color(color)

