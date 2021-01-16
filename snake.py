import turtle
import time
import random

delay = 0.3

score = 0
high_score = 0

wn = turtle.Screen ()
wn.title ("Snake Game")
wn.bgcolor ("lightgreen")
wn.setup (width = 600, height = 600)
wn.tracer (0) # turns off screen updates

head = turtle.Turtle () # snake's head
head.speed (0) #animation speed
head.shape ("square")
head.color ("darkgreen")
head.penup ()
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

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))

# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard inputs
wn.listen ()
wn.onkeypress (go_up, "w")
wn.onkeypress (go_down, "s")
wn.onkeypress (go_left, "a")
wn.onkeypress (go_right, "d")

# main game loop
while True:
    wn.update ()

    if head.xcor () > 290 or head.xcor () < -290 or head.ycor () > 290 or head.ycor() < - 290: #checks for collision with border
        time.sleep (1)
        head.goto (0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0 # resets the score

        delay = 0.3 

        pen.clear()
        pen.write ("Score: {}  High Score: {}".format (score, high_score), align="center", font=("Arial", 24, "normal")) 


    if head.distance (food) < 20: #checks for collision with food
        # moves food to random spot
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

        score += 10 

        if score > high_score:
            high_score = score

        pen.clear ()
        pen.write ("Score: {}  High Score: {}".format (score, high_score), align="center", font=("Arial", 24, "normal"))

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

    for segment in segments: # checks for head collision with body
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

            score = 0 # reset the score

            delay = 0.1  # reset the delay
        
            # update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep (delay)

wn.mainloop () # keeps window open 

