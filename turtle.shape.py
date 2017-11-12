import turtle
turtle.addshape("star.gif")
turtle.shape("star.gif")

turtle.speed(1000000000000000000000000000000000)
turtle.pensize(1)
a = 0

for i in range(360):
	turtle.pendown()
	turtle.right(90)
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(80)
	turtle.right(45)
	turtle.forward(40)
	
	turtle.right(90)
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(80)
	turtle.right(45)
	turtle.forward(40)

	turtle.penup()
	turtle.home()
	a+=7
	turtle.left(a)



turtle.mainloop()

