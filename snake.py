import turtle
import random #we'll need this later in the lab.

turtle.bgcolor("red")
turtle.tracer(1,0) #this helps the turtle move more smoothlty.

SCORE=0

size_x=800
size_y=500

turtle.setup(850,550) #curious? it,s the turtle window. size.

border = turtle.clone()

border.pensize(12)
border.pencolor("white")

border.penup()
border.goto(-400,-250)
border.pendown()
border.goto(400,-250)
border.goto(400,250)
border.goto(-400,250)
border.goto(-400,-250)

turtle.penup()
turtle.goto(0,0)
turtle.hideturtle()

square_size=20
start_length=5


#intialize lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
color_snake_list=["blue","green","black","yellow","brown","pink","lightblue","purple","gray","orange"]

#set up positions (x,y) of boxes that make up the snake.
snake=turtle.clone()
snake.shape("square")

#hide thee turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#draw a snake at the start of the game with a for loop.
#for loop should use range() and count up to the number of pieces.
#in the snake (i.e. start_length).
for snake_draw in range(start_length):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    #add square_size to x_pos. where does x_pos point  to now?
    #you're right
    x_pos+=square_size

    my_pos=(x_pos,y_pos) #store position variables in a tuple
    snake.goto(x_pos,y_pos) #move snake to new (x,y)

    #append the new position tuple to pos_list
    pos_list.append(my_pos)
    #save the stamp id! you'll need to erase it later. than append it to stamp_list.
    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)

#make sure you pay attention to upper and lower case.
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100 #update snake position after this many milliseconds

SPACEBAR="space" #careful,it's not supposed to be capitalized

UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP

TOP_EDGE=250
BOTTOM_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def up():
    global direction
    direction= UP
    print("you pressed the up key!")

def left():
    global direction
    direction= LEFT
    print("you pressed the left key!")

def down():
    global direction
    direction= DOWN
    print("you pressed the down key!")

def right():
    global direction
    direction= RIGHT
    print("you pressed the right key!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos=snake.pos()        
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + square_size, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - square_size, y_pos)
        print("you moved left")
    elif direction==UP:
        snake.goto(x_pos, y_pos+square_size)
        print("you moved up")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-square_size)

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    global food_stamps,food_pos,SCORE
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind]) #remove eaten food        
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!!!!!")
        make_food()

        SCORE+=1

        randomColor = random.choice(color_snake_list)
        snake.color(randomColor)

    else:
        
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
#grab position of snake
    new_pos=snake.pos()

    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! game over!!!!!:(")
        quit()
    
    elif new_x_pos<=LEFT_EDGE:
        print("you hit the left edge! game over!!!!!:(")
        quit()

    elif new_y_pos>=TOP_EDGE:
        print("you hit the top edge! game over!!!!!:(")
        quit()

    elif new_y_pos<=BOTTOM_EDGE:
        print("you hit the bottom edge! gmae over!!!!!:(")
        quit()
    if pos_list[-1] in pos_list[:-1]:
        print("you ate yourself!!!!!!!!!!!!")
        quit()
    
    turtle.ontimer(move_snake,TIME_STEP)

def printScore():
    turtle.goto(320,250)
    turtle.clear()
    turtle.write("Score: " + str(SCORE), False, "left", ("Arial", 16, "normal"))
    turtle.ontimer(printScore,1000)
    
printScore()
move_snake()

turtle.register_shape("star.gif")
#add trash picture
#make sure you have downloaded this shape
#from the google drive folder and saved it
#in the same folder as this python script
food=turtle.clone()
food.shape("star.gif")

#locations of food
food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
food_stamps=[]
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food2 = food.stamp()
    food_stamps.append(food2)

def make_food():
#the screen positions go from - size/2+size/2 but we need to make food pieces only appear on game squares so we cut up the game board into multiples of 
#square_size
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    min_y=-int(size_y/2/square_size)+1
    max_y=int(size_y/2/square_size)-1

#pick a position that is random multiple of square_size
    food_x=random.randint(min_x,max_x)*square_size
    food_y=random.randint(min_y,max_y)*square_size
    food.goto(food_x,food_y)
    random_food= (food_x,food_y)
    random_food_stamp=food.stamp()
    food_stamps.append(random_food_stamp)
    food_pos.append(random_food)
    


