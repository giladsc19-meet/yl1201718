import turtle

turtle.begin_fill()
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.end_fill()

turtle.mainloop()