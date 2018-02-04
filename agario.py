from turtle import *
import turtle
from ball import Ball
from ball import Food
import time
import random
import math 
###import from other files

tracer(0)
hideturtle()
colormode(255)
###smoothering,hide,all colors

bgcolor("maroon")
setup(1280,720)
SCREEN_WIDTH = int(getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(getcanvas().winfo_height()/2)
###board sizes

color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
MY_BALL = Ball(0,0,0,0,30,color)
###MY_BALL charactristic

m = clone()
m.hideturtle()
m.color("white")
m.pu()
###clones that makes the menu

SCORE = 0
SCORE2 = 0
RUNNING = False
SLEEP = 0.0077
NUMBER_OF_BALLS = 6
FOOD_AMOUNT = 25
MAXIMUM_MY_BALL_RADIUS = 150 
MINIMUM_BALL_RADIUS = 0.75*MY_BALL.radius
MAXIMUM_BALL_RADIUS = 1.50*MY_BALL.radius
MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1
###global veriables

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
	radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
	ball = Ball(xpos,ypos,dx,dy,radius,color)
	BALLS.append(ball)
###chossing random charactaristics for all the enemy balls

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
###using the function that i imported from Ball class (move())

def collide(ball1,ball2):
	if (ball1.shapesize()[0])*10+(ball2.shapesize()[0])*10>=math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)):
		return(True)
	else:
		return(False)
###check if there a collision between two balls

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
				radius = random.randint((int)(MINIMUM_BALL_RADIUS),(int)(MAXIMUM_BALL_RADIUS))
				color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
###using the collide function fo check if there is a collision between two balls and random new charactaristic

				if ra>rb:
					ball_b.goto(xpos,ypos) 
					ball_b.dx = dx
					ball_b.dy = dy
					ball_b.radius = radius
					ball_b.shapesize(radius/10)
					ball_b.color = color
					ball_a.radius += ball_b.radius/10
					ball_a.shapesize(ball_a.radius/10)
				
				if ra<rb:
					ball_a.goto(xpos,ypos)
					ball_a.dx =dx
					ball_a.dy = dy
					ball_a.radius = radius
					ball_a.shapesize(radius/10)
					ball_a.color = color
					ball_b.radius += ball_a.radius/10
					ball_b.shapesize(ball_b.radius/10)
###put new charactaristics for the smaller ball in the collision

def check_myball_collision():
	for b in BALLS:
		a = collide(MY_BALL , b)
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
			radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
			color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
###using the collide function fo check if there is a collision between two balls and random new charactaristics

			if rmy>ri:
				b.goto(xpos,ypos)
				if MAXIMUM_MY_BALL_RADIUS > MY_BALL.radius:
					MY_BALL.radius += b.radius/10
					MY_BALL.shapesize(MY_BALL.radius/10)
					b.dx = dx
					b.dy = dy
					b.radius = radius
					b.color = color
					b.shapesize(b.radius/10)
					
					Score()
				else:
					goto(0,0)
					write("-YOU WON!-",align = "center" , font = ("lklug",50,"italic","underline","bold"))
					time.sleep(4)
					return False
			if rmy<ri:
				goto(0,0)
				write("-YOU LOST!-",align = "center" , font = ("lklug",50,"italic","underline","bold"))
				time.sleep(4)
				return False
	return True
### if i won print, if i ate grow, if i failed

def movearound(event):  
	MY_BALL.xpos = event.x - SCREEN_WIDTH
	MY_BALL.ypos = SCREEN_HEIGHT - event.y
	MY_BALL.goto(MY_BALL.xpos,MY_BALL.ypos)
###event corresponds to the mouse moving on the screen

FOOD = []
for i in range(FOOD_AMOUNT):
	xpos = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	ypos = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
	food = Food(xpos,ypos,color)
	FOOD.append(food)
###creating the first foods

def myball_collision_food():
	for f in FOOD:
		a = collide(MY_BALL,f)
		if a==True:
			xpos = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			ypos = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
			f.goto(xpos,ypos)
			f.color = color
			MY_BALL.radius += 1
			MY_BALL.shapesize(MY_BALL.radius/10)
			FScore()
###checking my collision with food

def FScore():
	pu()
	goto(-SCREEN_WIDTH+30,SCREEN_HEIGHT-70)
	clear()
	global SCORE2
	SCORE2 += 1
	write("Eaten Food: "+str(SCORE2) , font = ("Aerial" , 30 , "bold"))
###responsibole for changing the score every time i eat food

def Score():
	pu()
	goto(-SCREEN_WIDTH+30,SCREEN_HEIGHT-70)
	clear()
	global SCORE
	SCORE += 1
	write("Eaten Balls: "+str(SCORE) , font = ("Aerial" , 30 , "bold"))
###responsibole for changing the score every time i eat
def RUN():
	global RUNNING,SCREEN_HEIGHT,SCREEN_WIDTH
	m.clear()
	RUNNING = True
	while RUNNING==True:
		if SCREEN_WIDTH != int(getcanvas().winfo_width()/2) or SCREEN_HEIGHT != int(getcanvas().winfo_height()/2):
			SCREEN_WIDTH = int(getcanvas().winfo_width()/2)
			SCREEN_HEIGHT = int(getcanvas().winfo_height()/2)
		getcanvas().bind("<Motion>", movearound)
		move_all_balls()
		check_all_balls_collision()
		RUNNING = check_myball_collision()
		MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		myball_collision_food()
		update()
		time.sleep(SLEEP)

def RULES():
	m.clear()
	m.color("white")
	m.pu()
	m.goto(0,150)
	m.write("RULES!",align="center",font=("lklug",50,"italic","underline"))
	m.goto(-550,30)
	time.sleep(0.5)
	m.write("-you need to eat the smallest balls, what will make you bigger",align="left",font=("lklug",20,"italic"))
	m.goto(-550,-30)
	time.sleep(0.5)
	m.write("-you need to escape the bigger balls, so you won't lose the game",align="left",font=("lklug",20,"italic"))
	m.goto(-550,-90)
	time.sleep(0.5)
	m.write("-you can choose the mode you want to play in in the setting and changing the game",align="left",font=("lklug",20,"italic"))
	m.goto(-550,-150)
	time.sleep(0.5)
	m.write("-in each mode you win differently (according to the food amount or the balls you ate or your score",align="left",font=("lklug",20,"italic"))
	m.goto(-SCREEN_WIDTH+30,-SCREEN_HEIGHT+30)
	m.write("back (1)",align="left",font=("lklug",18,"italic"))
	turtle.onkeypress(menu,"1")
	turtle.listen()

def menu():
	m.clear()
	m.goto(0,150)
	m.write("AGARIO!",align="center",font=("lklug",50,"italic","underline"))
	m.goto(-160,30)
	time.sleep(0.5)
	m.write("*Play (1)",align="left",font=("lklug",30,"italic"))
	m.goto(-160,-30)
	time.sleep(0.5)
	m.write("*Rules (2)",align="left",font=("lklug",30,"italic"))
	m.goto(-160,-90)
	time.sleep(0.5)
	m.write("*Credits (3)",align="left",font=("lklug",30,"italic"))
	m.goto(-160,-150)
	time.sleep(0.5)
	m.write("*Quit (4)",align="left",font=("lklug",30,"italic"))
	turtle.onkeypress(RUN,"1")
	turtle.listen()
	turtle.onkeypress(RULES,"2")
	turtle.listen()
	#onkeypress(,'3')
	#onkeypress(,'4')
menu()

#######todo list!#######
# make the score better
# collision food with balls
# make the balls change their collor and size after they are eaten by others
# do what glober did with the screen colors
# make the menu work + adding rules credits and quit and play again options
# adding settings: remove food, add more players... 
# make new modes for the game (on time, on score, till you dead...)
# thinking about new features

#######error list!#######
# dead enemies should change the color
mainloop()