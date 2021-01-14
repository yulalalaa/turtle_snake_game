import turtle
import time
import random

delay = 0.3

wn = turtle.Screen ()
wn.title ("Snake Game")
wn.bgcolor ("lightgreen")
wn.setup (width = 600, height = 600)
wn.tracer (0) # turns off screen updates

head = turtle.Turtle () # snake's head
head.speed (0) #animation speed
head.shape ("square")
head.color ("darkgreen")
head.penup () # up - turtle does not draw anything
head.goto (0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle () 
food.speed (0) 
food.shape ("circle")
food.color ("red")
food.penup () 
food.goto (0, 100)

segments = [] 

# functions
def go_up ():
    head.direction = "up"

def go_down ():
    head.direction = "down"

def go_left ():
    head.direction = "left"

def go_right ():
    head.direction = "right"

#keyboard inputs
wn.listen ()
wn.onkeypress (go_up, "w")
wn.onkeypress (go_down, "s")
wn.onkeypress (go_left, "a")
wn.onkeypress (go_right, "d")

def move ():
    if head.direction == "up":
        y = head.ycor ()
        head.sety (y + 20)

    if head.direction == "down":
        y = head.ycor ()
        head.sety (y - 20)

    if head.direction == "left":
        x = head.xcor ()
        head.setx (x - 20)

    if head.direction == "right":
        x = head.xcor ()
        head.setx (x + 20)

# main game loop
while True:
    wn.update ()

    if head.xcor () > 290 or head.xcor () < -290 or head.ycor () > 290 or head.ycor() < - 290: #checks for collision with border
        time.sleep (1)
        head.goto (0, 0)
        head.direction = "stop"

    if head.distance (food) < 20: #checks for collision with food
        x = random.randint (-290, 290)
        y = random.randint (-290., 290)
        food.goto (x, y)

        #add a segment
        new_segment = turtle.Turtle ()
        new_segment.speed (0)
        new_segment.shape ("square") 
        new_segment.color ("green")
        new_segment.penup ()
        segments.append (new_segment)

    # move the end segments first 
    for index in range (len (segments) -1, 0, -1):
        x = segments [index - 1].xcor ()
        y = segments [index - 1].ycor ()
        segments [index].goto (x, y)

    # move segment 0 to the head
    if len (segments) > 0:
        x = head.xcor ()
        y = head.ycor ()
        segments [0].goto (x, y)

    move ()

    time.sleep (delay)


wn.mainloop () # keeps window open 

