from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
ball1 = Ball(10,"red",25)
ball2 = Ball(5,"blue",25)

def check_collision(ball1, ball2):
	if ball1.radius+ball2.radius>math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)):
		print("collision")
check_collision(ball1,ball2)

mainloop()

