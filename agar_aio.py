from turtle import *
import turtle
import random
import math

#borders
turtle.setup(5000,5000)

border = turtle.clone()

border.pensize(12)
border.pencolor("red")
border.speed(10000)

border.penup()
border.goto(-600,-350)
border.pendown()
border.goto(600,-350)
border.goto(600,350)
border.goto(-600,350)
border.goto(-600,-350)
border.hideturtle()


class Players(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
P1 = Players(0.9,"red",1)
P2 = Players(0.9,"orange",1)

P1.penup()
P2.penup()
P1.goto(110,0)
P2.goto(-110,0)

def check_collision(ball1, ball2):
	if (P1.shapesize()[0])*10+(P2.shapesize()[0])*10>=math.sqrt(math.pow((P1.xcor()-P2.xcor()),2)+math.pow((P1.ycor()-P2.ycor()),2)):
		print("collision")
		P1.color("black")
		P2.color("gray")
	else:
		print("no collision")
check_collision(P1,P2)

mainloop()