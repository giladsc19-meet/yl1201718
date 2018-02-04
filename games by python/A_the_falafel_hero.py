import turtle
import time

turtle.setup(700,700)


from turtle import *
screen = Screen()
turtle.penup()

screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

def mainMenu():
    screen.bgcolor("black")
    goto(0, screenMaxY - 200)
    color('grey')
    write("The Pita Hero!!", align="center", font=("Arial",50))
    goto(0, screenMaxY - 215)
    write("CoOl GaMe WiTh CoOl FeAtUrEs...YoU hAvE tO pLaY iT!", align="center")
    turtle.showturtle()
    goto(0,screenMaxY- 350)
    write("Play game",align="center",font=("Ariel",20))
    goto(0,screenMaxY-400)
    write("Score table",align="center",font=("Ariel",20))
    goto(0,screenMaxY-450)
    write("How to play", align="center",font=("Ariel",20))
    turtle.register_shape("phlaphel2.gif")
    turtle.shape("phlaphel2.gif")
    turtle.goto(-200, -200)
    turtle.stamp()
    turtle.register_shape("pitaBread2.gif")
    turtle.shape("pitaBread2.gif")
    turtle.goto(200,-200)
    turtle.stamp()
xclick=0
yclick = 0

mainMenu()
    
##############################

turtle.tracer(1, 0)
mouth=turtle.clone()
turtle.hideturtle()
turtle.setup(700,700)
turtle.penup()
mouth.penup()
mouth.hideturtle()

clones_list=[]
clones_pos_list=[]
shot_pos=[]

TIME_STEP = 500

turtle.register_shape("mouth.gif")
mouth.shape("mouth.gif")
turtle.bgcolor("black")

x_pos = -280
y_pos = -130

#Edges and Borders:

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

SCORE = 0

edgy_turtle=turtle.clone()
edgy_turtle.speed(0)
edgy_turtle.hideturtle()
edgy_turtle.color("red")
edgy_turtle.penup()

##############################################################################

def create_border():
    edgy_turtle.pensize(6)

    edgy_turtle.goto(UP_EDGE, RIGHT_EDGE)

    edgy_turtle.pendown()
    
    edgy_turtle.right(90)
    for i in range (3):
        edgy_turtle.forward(600)
        edgy_turtle.right(90)
        
create_border()

#This is the starving kid:
def starving_kid():
    turtle.register_shape("kid.gif")
    starving_kid1=turtle.clone()
    starving_kid1.shape("kid.gif")
    starving_kid1.pu()
    starving_kid1.showturtle()
    starving_kid1.goto(30, 310)
starving_kid()
#score:

score_turtle=turtle.clone()
score_turtle.hideturtle
score_turtle.pu()
score_turtle.color("white")
score_turtle.goto(-295, 305)

def score():
    score_turtle.clear()
    score_turtle.write("Score: " + str(SCORE), font=("Arial", 16, "normal"))

##def accessories():
##    acc = turtle.clone()
##    acc.showturtle()
##    acc.color("white")
##    acc.hideturtle()
##    acc.pu()
##    acc.goto(-350, -300)
##    acc.pd()
##    acc.pensize(10)
##    acc.goto(-300, -300)
##    acc.goto(-300, -350)
##    acc.pu()
##    acc.goto(350, -300)
##    acc.pd()
##    acc.goto(300, -300)
##    acc.goto(300, -350)
##    acc.pu()
##    acc.goto(-350, 300)
##    acc.pd()
##    acc.goto(-300, 300)
##    acc.goto(-300, 350)
##    acc.pu()
##    acc.goto(350, 300)
##    acc.pd()
##    acc.goto(300, 300)
##    acc.goto(300, 350)
##accessories()

h=0
def highscore():
    high=turtle.clone()
    high.color("white")
    high.hideturtle()
    high.pu()
    high.goto(-290, -340)
    high.write("Highscore: " + str(h), font=("Aerial", 16, "normal"))

highscore()

clock_clone = turtle.clone()
clock_clone.goto(RIGHT_EDGE - 50, UP_EDGE - 20)
clock = 0

def timer():
    global clock
    clock += 1

    clock_clone.clear()
    clock_clone.write("0:" + str(clock), font=("Aerial", 16, "normal"))
    
    if clock == 2:
##        gameOver()
        print("Game Over")
        
    turtle.ontimer(timer, 1000)
    
def draw_enemy():
    global x_pos, y_pos

    mouth.showturtle()
    
    for row in range(0,4):
        x_pos = -280
        y_pos += 60
        mouth.setposition(x_pos,y_pos)
        for column in range (0,13):
            if column != 0:
                x_pos += 40
                mouth.goto(x_pos, y_pos)
                
            mouth_clone = mouth.clone()
            clones_list.append(mouth_clone)
            clones_pos_list.append(mouth_clone.pos())
            
    mouth.hideturtle()
    print(clones_pos_list)
    
##draw_enemy()
count = 0
def move_enemy_right():
    global count
    for clone in clones_list:
        (x_pos,y_pos) = clone.pos()
        d = clones_pos_list.index(clone.pos())
        clone.goto(x_pos+10,y_pos)
        clones_pos_list[d] = clone.pos()
        
    count += 1
    if count % 5 == 0:
        move_enemy_left()
    else:
        turtle.ontimer(move_enemy_right, TIME_STEP)

def move_enemy_left():
    global count
    for clone in clones_list:
        (x_pos,y_pos) = clone.pos()
        d = clones_pos_list.index(clone.pos())
        clone.goto(x_pos-10,y_pos)
        clones_pos_list[d] = clone.pos()
        
    count+=1
    if count % 5 == 0:
        move_enemy_right()
    else:
        turtle.ontimer(move_enemy_left, TIME_STEP)
        
        
#####################################################33


##    #_______________musa start_____________________________
##    if my_pos[0] > -300 and my_pos[0] < 300:
##     #___________________musa end_____________________________
##        if direction==RIGHT:
##            player.goto(x_pos +SQUARE_SIZE, y_pos)
##            print ("You moved right!")
##        elif direction==LEFT:
##            player.goto(x_pos - SQUARE_SIZE, y_pos)
##            print("You moved left!")
##
## #_________________________musa start____________________________           
##    elif my_pos[0] <= -300 or my_pos[0] >= 300:
##        player.goto(x_pos, y_pos)
##        if direction == RIGHT:
##            player.goto(x_pos-25, y_pos)
##        
##        elif direction == LEFT:
## if x_pos + SQUARE_SIZE < 300 and x_pos - SQUARE_SIZE > -300:
##            player.goto(x_pos+25, y_pos)
###__________________________musa end_________________________________



pos_list = []
stamp_list = []

SQUARE_SIZE = 10


player = turtle.clone()
turtle.register_shape("pitaBread2.gif")
player.shape("pitaBread2.gif")
player.penup()
player.goto(0, DOWN_EDGE + 20)
player.showturtle()

LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right"
LEFT = 2
RIGHT = 3
IDLE = 0

direction = LEFT

## Dan comment: Make direction that's an idle state - don't move at all

def left ():
    global direction
    if player.pos()[0] > -280:   
        direction=LEFT
    else:
        direction = IDLE
    move()
def right ():
    global direction
    if player.pos()[0] < 280:  
        direction=RIGHT
    else:
        direction = IDLE
    move()

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


def move():
    global direction
    my_pos = player.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT:
        player.goto(x_pos + SQUARE_SIZE, y_pos)
        print ("You moved right!")
    elif direction==LEFT:
        player.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction == IDLE:
        pass

FALAFEL_SPEED = 30

phlaphel = turtle.clone()
turtle.register_shape("phlaphel2.gif")
turtle.register_shape("ketchup.gif")
phlaphel.shape('phlaphel2.gif')
phlaphel.penup()

ball_shot = False
IS_KETCHUP = False
def falafel_shot():
    global ball_shot, IS_KETCHUP

    """
    If ball_shot is False,
    it shoots a piece of falafel
    and sets ball_shot to True
    """
    
    if ball_shot == False:
        phlaphel.st()
        shot = player.pos()
        x_pos = shot[0]
        y_pos = shot[1]
        #phlaphel.goto(shot)
        phlaphel.goto(x_pos, y_pos)
        phlaphel.showturtle()
        phlaphel.shape("phlaphel2.gif")
        ball_shot = True
        IS_KETCHUP = False

def ketchup_shot():
    global ball_shot, IS_KETCHUP

    """
    If ball_shot is False,
    it shoots a piece of ketchup
    and sets ball_shot to True
    """
    
    if ball_shot == False:
        phlaphel.st()
        shot = player.pos()
        x_pos = shot[0]
        y_pos = shot[1]
        #phlaphel.goto(shot)
        phlaphel.goto(x_pos, y_pos)
        phlaphel.showturtle()
        phlaphel.shape("ketchup.gif")
        ball_shot = True
        IS_KETCHUP = True

def kill_enemies():
    global clones_list, clones_pos_list
    
    for i in range(len(clones_pos_list) - 1):
        if (phlaphel.pos() == clones_pos_list[i]) == True:
            clones_list[i].ht()
            clones_list.pop(i)
            clones_pos_list.pop(i)
            print("asfasf")
            break
            
def shotBullet():
    global ball_shot, SCORE

    if ball_shot == True:
        phlaphel.goto(phlaphel.pos()[0], phlaphel.pos()[1] + FALAFEL_SPEED)

    if phlaphel.pos()[1] >= UP_EDGE:
        phlaphel.ht()
        phlaphel.goto(0, -1000)

        if IS_KETCHUP == True:
            SCORE -= 1
        else:
            SCORE += 1
            
        ball_shot = False
        score()

    if (phlaphel.pos() in clones_pos_list) == True:
        phlaphel.ht()
        
        if IS_KETCHUP:
            kill_enemies()
        else:
            SCORE -= 1

        phlaphel.goto(0, -10000)
        score()
        ball_shot = False
        print("hit enemy")
    
    turtle.ontimer(shotBullet, 5)

def controlBullet():
    """
    If ball_shot is True, moves the
    phlaphel up by 30
    If the phlaphel's y is bigger than
    
    or equal to 300, ball_shot becomes False
    Every 10 milliseconds, run shotBullet()
    """
    global ball_shot
    
    if ball_shot == True:
        # move up by 30
        phlaphel.goto(phlaphel.pos()[0], phlaphel.pos()[1] + 30)

    # if the phlaphel goes above the border
    if phlaphel.pos()[1] >= 300:
        ball_shot = False
    
    turtle.ontimer(controlBullet, 10)

shotBullet()

turtle.onkeypress(falafel_shot, 'z')
turtle.onkeypress(ketchup_shot, 'x')

def play():
    draw_enemy()
    move_enemy_right()
    timer()

def variables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)

turtle.onscreenclick(variables)


def gameOver():
    edgy_turtle.clear()
    screenMinX = -screen.window_width()/2
    screenMinY = -screen.window_height()/2
    screenMaxX = screen.window_width()/2
    screenMaxY = screen.window_height()/2
    screen.bgcolor("black")
    goto(0, screenMaxY - 350)
    color('grey')
    write("GAME OVER!!", align="center", font=("Arial",50))

    color('black')
    
    turtle.stamp()
    turtle.register_shape("ppp.gif")
    turtle.shape("ppp.gif")
    turtle.goto(200,-200)
    turtle.stamp()

def check_click():
    IS_NOT_MENU = False
    if xclick >= -75 and xclick <= 75 and yclick > 0 and yclick <= 35:
        turtle.clear()
        play()
        IS_NOT_MENU = True
    elif xclick>= -75 and xclick<= 75 and yclick>-46 and yclick<= -22:
        turtle.clear()
        print("score is on")
        IS_NOT_MENU = True
    elif xclick>=-75  and xclick<=75  and yclick> -92 and yclick <= -73:
        turtle.clear()
        print("how to play is on")
        IS_NOT_MENU = True
        
    if IS_NOT_MENU == False:
        turtle.ontimer(check_click, 100)
        
check_click()

##       ADD ENEMY SHOT - N
##       MOVING KIDS - N / 2
##       FIX BUGS - N / 2
##       KILL ENEMY - Y / 2
##       GAME OVER - Y
##       BUG - Run the game while in main menu because hit the bullet in the kids