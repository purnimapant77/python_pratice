import turtle
import random

# Create screen
screen = turtle.Screen()
screen.title("Simple Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()

# Create food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# Movement functions
def move_up():
    snake.setheading(90)
    snake.forward(20)

def move_down():
    snake.setheading(270)
    snake.forward(20)

def move_left():
    snake.setheading(180)
    snake.forward(20)

def move_right():
    snake.setheading(0)
    snake.forward(20)

# Keyboard controls
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Check food collision continuously
def check_food():
    if snake.distance(food) < 20:
        print("Food Eaten!")

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        food.goto(x, y)

    screen.ontimer(check_food, 100)

check_food()

turtle.done()