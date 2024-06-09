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

        start_x = random.uniform(-screen_width / 2, screen_width / 2)
        start_y = random.uniform(-screen_height / 2, screen_height / 2)
        new_turtle.penup()  # Lift the pen to prevent drawing lines
        new_turtle.goto(start_x, start_y)
        new_turtle.pendown()

        #new_turtle.speed("fastest")
        new_turtle.speed(int(10/n))
        # Set a random shape and color for the turtle
        shape = "turtle" #random.choice(["turtle", "arrow", "circle", "square"])
        hue = random.uniform(0, 1)
        r, g, b = colorsys.hls_to_rgb(hue, 0.5, 1)  # Using lightness value of 0.5
        color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
        new_turtle.shape(shape)
        new_turtle.color(color)

        turtle_list.append(new_turtle)

    return turtle_list

def calculate_angle_from_index(index_x, index_y, x, y):
    # Calculate differences in x and y coordinates
    dx = x - index_x
    dy = y - index_y
    
    # Calculate the angle using arctangent
    angle_rad = math.atan2(dy, dx)
    
    # Convert angle from radians to degrees
    #angle_deg = math.degrees(angle_rad)
    
    return angle_rad

def find_coordinates_within_distance(coordinates, index, d):
    # Extract the index coordinates
    index_x, index_y = coordinates[index]

    # Initialize a list to store the angles within distance d
    move = []

    # Iterate over each coordinate pair
    for i, (x, y) in enumerate(coordinates):
        if i != index:  # Skip comparing with the index itself
            distance = math.sqrt((x - index_x)**2 + (y - index_y)**2)
            if distance <= d:
                angle = calculate_angle_from_index(index_x, index_y, x, y)
                angle_deg = math.degrees(angle)
                #print("dis",distance/d)
                move.append([1-(distance/d),angle_deg])

    return move

def vector_sum(pairs):
    if len(pairs)>0:
        # Initialize variables for summing components
        sum_x = 0
        sum_y = 0
        
        # Calculate components of each vector and sum them
        for strength, angle in pairs:
            # Convert angle to radians
            angle_rad = math.radians(angle)
            # Calculate x and y components
            x_component = strength * math.cos(angle_rad)
            y_component = strength * math.sin(angle_rad)
            
            # Add components to the sum
            sum_x += x_component
            sum_y += y_component
        
        # Calculate net strength and angle from components
        net_strength = math.sqrt(sum_x**2 + sum_y**2)
        net_angle = math.degrees(math.atan2(sum_y, sum_x))
    else:
        net_strength=0
        net_angle =0
    return net_strength, net_angle

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

circle_turtle = turtle.Turtle()
def circles(coords,radius):
    for cord in coords:
        x = cord[0]
        y = cord[1]
        circle_turtle.penup()
        circle_turtle.goto(x, y - radius)  # Move to the starting point at the bottom of the circle
        circle_turtle.pendown()
        circle_turtle.circle(radius)
# Example usage:
n = 20 # Number of turtles to create
steps = 1000000
turtle_list = create_turtles(n)
radius = 75
coords = []
for i in range(len(turtle_list)):
    coords.append([])
for i in range(len(turtle_list)):
    coords[i] = [turtle_list[i].xcor(),turtle_list[i].ycor()]
for step in range(steps):
    move_forward = []
    move_angle = []
    for i in range(len(turtle_list)):
        move_list = find_coordinates_within_distance(coords, i,radius)
        #print(move_list,"\n")
        net_strength, net_angle = vector_sum(move_list)
        #print(net_strength,net_angle)
        #print("="*50)
        forward = net_strength*radius
        move_forward.append(forward)
        move_angle.append(net_angle)
        #move(turtle_list[i] ,-net_angle,forward)
        #print(net_angle,forward)
        #print()
        #print("="*50)

    turtle.delay(0)
    circle_turtle.clear()
    circles(coords,radius)
    turtle.delay(10)
    for i in range(len(turtle_list)):
        move(turtle_list[i] ,-move_angle[i],move_forward[i])
        coords[i] =[turtle_list[i].xcor(),turtle_list[i].ycor()]

    

    
    

    

