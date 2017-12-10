from turtle import *
import random
import math

class Rectruingle(Turtle):
	def __init__(self, height, width, color, speed):
		Turtle.__init__(self)
		
		self.shapesize(height,width)
		rec = turtle.registershape((0,0),(width,0),(width,height),(0,height))
		self.shape("rec")
		self.color(color)
		self.speed(speed)

rec1 = Rectruingle(10,20,"black",1)
rec2 = Rectruingle(10,20,"gray",1)

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
ball1 = Ball(10,"red",1)
ball2 = Ball(10,"orange",1)

ball1.penup()
ball2.penup()
ball1.goto(110,0)
ball2.goto(70,0)

def check_collision(ball1, ball2):
	if (ball1.shapesize()[0])*10+(ball2.shapesize()[0])*10>=math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)):
		print("collision")
		ball1.color("black")
		ball2.color("gray")
	else:
		print("no collision")
check_collision(ball1,ball2)
mainloop()

