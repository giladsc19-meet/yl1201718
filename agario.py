import turtle
from turtle import *
import time
import random

turtle.tracer(0)
turtle.hideturtle()

RUNNING = turtle
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

class Ball(Turtle):
	def __init__(self,xpos,ypos,dx,dy,radius):
		Turtle.__init__(self)
		self.pu()
		self.goto(xpos,ypos)
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.shape("circle")
		self.shapesize(radius/10)
		
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)

		def move(self,screen_width,screen_height):
			current_x = self.xcor()
			current_y = self.ycor()
			new_x = current_x + dx
			new_y = current_y + dy

			right_side_ball = new_x + radius
			left_side_ball = new_x - radius
			up_side_ball = new_y + radius
			bottom_side_ball = new_y - radius

			self.goto(new_x,new_y)
			if right_side_ball>=screen_width or left_side_ball<=screen_width:
				self.dx = -self.dx
			if bottom_side_ball>=screen_height or bottom_side_ball<=screen_height:
				self.dy = -self.dy


MY_BALL = Ball(0,0,1,1,5)


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range(NUMBER_OF_BALLS):
	xpos = random.randint(SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	ypos = random.randint(SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = random.randint(random.random(),random.random(),random.random())
	ball = Ball(xpos,ypos,dx,dy,radius,color)
	BALLS.append(ball)

def move_all_balls():
	for ball in range(BALLS):
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball1,ball2):
	if (ball1.shapesize()[0])*10+(ball2.shapesize()[0])*10>=math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)):
		return(True)
	else:
		return(False)

def check_all_balls_collision():
	for ball_a in BALLS():
		for ball_b in BALLS():
			a = collide(ball_a,ball,b)
			if a==True:
				ra = ball_a.radius
				rb = ball_b.radius
				xpos = random.randint(SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				ypos = random.randint(SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = random.randint(random.random(),random.random(),random.random())
				
				if ra>rb:
					ball_b(xpos,ypos,dx,dy,radius,color)
					ball_a += 1
				if ra<rb:
					ball_a(xpos,ypos,dx,dy,radius,color)
					ball_b += 1
