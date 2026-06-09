import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# Score
score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)

# Snake body segments
segments = []

# Direction functions
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

# Keyboard controls
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Update score
def update_score():
    score_display.clear()
    score_display.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 16, "normal")
    )

update_score()

# Move snake
def move():

    # Move body from back to front
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # First segment follows head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move head
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    elif head.direction == "down":
        head.sety(head.ycor() - 20)

    elif head.direction == "left":
        head.setx(head.xcor() - 20)

    elif head.direction == "right":
        head.setx(head.xcor() + 20)

    # Food collision
    global score

    if head.distance(food) < 20:

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        food.goto(x, y)

        # Add new body part
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("lightgreen")
        segment.penup()

        segments.append(segment)

        score += 1
        update_score()

    screen.update()
    screen.ontimer(move, 100)

# Start game loop
move()

turtle.done()