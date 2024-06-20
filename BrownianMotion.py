import turtle
import random
import colorsys
import math

# Set screen dimensions
screen_width = turtle.window_width()
screen_height = turtle.window_height()

def create_turtles(n):
    turtle_list = []
    screen_width = turtle.window_width()
    screen_height = turtle.window_height()

    for _ in range(n):
        new_turtle = turtle.Turtle()
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.goto(-300, 300)
        new_turtle.pendown()
        # Set a random shape and color for the turtle
        shape = "turtle" #random.choice(["turtle", "arrow", "circle", "square"])
        hue = random.uniform(0, 1)
        r, g, b = colorsys.hls_to_rgb(hue, 0.5, 1)  # Using lightness value of 0.5
        color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
        new_turtle.shape(shape)
        new_turtle.color(color)

        turtle_list.append(new_turtle)

    return turtle_list



def move(turtl, angle, forward_distance):
    
    x = turtl.xcor()
    y = turtl.ycor()

    # Simulate the turtle's movement
    turtl.setheading(0)

    if angle <= 180:
        turtl.left(angle)
    else:
        turtl.right(360 - angle)
    turtl.forward(forward_distance)

    # Get the resulting position
    x = turtl.xcor()
    y = turtl.ycor()

    # Check if the resulting position is above the screen
    turtl.penup()
    if y > screen_height / 2:
        diff = y - (screen_height / 2)
        turtl.goto(x, -screen_height / 2)
        turtl.pendown()
        turtl.forward(diff)
        #turtl.goto(x, -(screen_height / 2) + diff)  # Teleport to bottom of the screen
    # Check if the resulting position is below the screen
    elif y < -screen_height / 2:
        diff = abs(y) - (screen_height / 2)
        turtl.goto(x, screen_height / 2)
        turtl.pendown()
        turtl.forward(diff)
        #turtl.goto(x, (screen_height / 2) - diff)  # Teleport to top of the screen
    turtl.penup()
    # Check if the resulting position is off-screen to the left
    if x < -screen_width / 2:
        diff = abs(x) - (screen_width / 2)
        turtl.goto(screen_width / 2, y)
        turtl.pendown()
        turtl.forward(diff)
        #turtl.goto((screen_width / 2) - diff, y)  # Teleport to right side of the screen
    # Check if the resulting position is off-screen to the right
    elif x > screen_width / 2:
        diff = x - (screen_width / 2)
        turtl.goto(-screen_width / 2, y)
        turtl.pendown()
        turtl.forward(diff)
        #turtl.goto(-(screen_width / 2) + diff, y) 
    turtl.pendown()

# Example usage:
n = 200 # Number of turtles to create
steps = 1000000
turtle_list = create_turtles(n)
coords = []
for i in range(len(turtle_list)):
    coords.append([])
for i in range(len(turtle_list)):
    coords[i] = [turtle_list[i].xcor(),turtle_list[i].ycor()]
for step in range(steps):
    move_forward = []
    move_angle = []
    for i in range(len(turtle_list)):
        net_strength = random.randint(0, 20)
        net_angle = step#random.randint(0, 180)
        forward = net_strength#step#net_strength
        move_forward.append(forward)
        move_angle.append(net_angle)

    turtle.delay(0)
    for i in range(len(turtle_list)):
        move(turtle_list[i] ,-move_angle[i],move_forward[i])
        coords[i] =[turtle_list[i].xcor(),turtle_list[i].ycor()]

    

    
    

    

