import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed
t.speed(0)

# Set the turtle shape
t.shape("turtle")

# Set the turtle pen size
t.pensize(20)

# Set the initial position of the turtle
x = 0
y = 0
t.penup()
t.goto(x, y)
t.pendown()

# Define the number of steps for the random walk
num_steps = 100

# Perform the random walk
for _ in range(num_steps):
    # Generate a random angle (0, 90, 180, or 270 degrees)
    angle = random.choice([0, 90, 180, 270])

    # Set the distance to 100 pixels
    distance = 40

    # Generate random RGB values for the turtle color
    red = random.random()
    green = random.random()
    blue = random.random()

    # Set the turtle color
    t.color(red, green, blue)

    # Move the turtle forward by the fixed distance
    t.forward(distance)

    # Rotate the turtle by the random angle
    t.right(angle)

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()
