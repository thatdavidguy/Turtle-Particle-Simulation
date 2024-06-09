import turtle
import random
import colorsys


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

        # Set a random shape and color for the turtle
        shape = "turtle" #random.choice(["turtle", "arrow", "circle", "square"])
        hue = random.uniform(0, 1)
        r, g, b = colorsys.hls_to_rgb(hue, 0.5, 1)  # Using lightness value of 0.5
        color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
        new_turtle.shape(shape)
        new_turtle.color(color)

        turtle_list.append(new_turtle)

    return turtle_list

# Example usage:
n = 10 # Number of turtles to create
turtle_list = create_turtles(n)

def random_move():
    forward = random.randint(0, 50)
    angle = random.randint(0, 360)
    return(forward,angle)

def move(turtl, angle, forward_distance):
    
    x = turtl.xcor()
    y = turtl.ycor()

    # Simulate the turtle's movement
    #turtl.setheading(90)

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


while True:
    for i in turtle_list:
        forward,angle = random_move()
        move(i,angle,forward)
        

    

