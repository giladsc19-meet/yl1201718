from turtle import *
from ball import Ball
import time
import random
import math 

tracer(0)
hideturtle()
colormode(255)

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = int(getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(getcanvas().winfo_height()/2)

color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
MY_BALL = Ball(0,0,1,1,20,color)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range(NUMBER_OF_BALLS):
	xpos = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	ypos = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx==0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
	ball = Ball(xpos,ypos,dx,dy,radius,color)
	BALLS.append(ball)

def move_all_balls():
	for i in range(len(BALLS)):
		BALLS[i].move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball1,ball2):
	if (ball1.shapesize()[0])*10+(ball2.shapesize()[0])*10>=math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)):
		return(True)
	else:
		return(False)

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			a = collide(ball_a,ball_b)
			if a==True:
				ra = ball_a.radius
				rb = ball_b.radius
				xpos = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				ypos = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while dx==0:
					dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while dy==0:
					dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
				
				if ra>rb:
					ball_b.goto(xpos,ypos)
					ball_b.dx
					ball_b.dy
					ball_b.radius
					ball_b.color
					ball_a.radius += 1
					ball_a.shapesize(radius/10)
				
				if ra<rb:
					ball_a.goto(xpos,ypos)
					ball_a.dx
					ball_a.dy
					ball_a.radius
					ball_a.color
					ball_b.radius += 1
					ball_b.shapesize(radius/10)

def check_myball_collision():
	for b in BALLS:
		a = collide(MY_BALL, b)
		if a==True:
			rmy = MY_BALL.radius
			ri = b.radius
			xpos = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			ypos = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while dx==0:
				dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			while dy==0:
				dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
			if rmy>ri:
				b.goto(xpos,ypos)
				b.dx = dx
				b.dy = dy
				b.radius = radius
				b.color = color
				MY_BALL.radius += 1
				MY_BALL.shapesize(MY_BALL.radius/10)

			if rmy<ri:
				b.radius += 1
				return False
	return True

def movearound(event):  #event corresponds to the mouse moving on the screen
	MY_BALL.xpos = event.x - SCREEN_WIDTH
	MY_BALL.ypos = SCREEN_HEIGHT - event.y
	MY_BALL.goto(event.x - SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

getcanvas().bind("<Motion>", movearound)
listen()

while RUNNING==True:
	if SCREEN_WIDTH != int(getcanvas().winfo_width()/2) or SCREEN_HEIGHT != int(getcanvas().winfo_height()/2):
		SCREEN_WIDTH = int(getcanvas().winfo_width()/2)
		SCREEN_HEIGHT = int(getcanvas().winfo_height()/2)
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	update()
	time.sleep(SLEEP)