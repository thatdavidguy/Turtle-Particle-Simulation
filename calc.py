import math

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
                move.append([1-distance/d,angle])

    return move

def vector_sum(pairs):
    # Initialize variables for summing components
    sum_x = 0
    sum_y = 0
    
    # Calculate components of each vector and sum them
    for strength, angle_rad in pairs:
        # Convert angle to radians
        
        # Calculate x and y components
        x_component = strength * math.cos(angle_rad)
        y_component = strength * math.sin(angle_rad)
        
        # Add components to the sum
        sum_x += x_component
        sum_y += y_component
    
    # Calculate net strength and angle from components
    net_strength = math.sqrt(sum_x**2 + sum_y**2)
    net_angle = math.degrees(math.atan2(sum_y, sum_x))
    
    return net_strength, net_angle

# Example usage:
coordinates = [[1, 2], [3, 4], [4, 6], [7, 8]]  # Example list of coordinates
index = 1  # Example index
d = 10  # Example distance threshold

# Find the angles from the index coordinates to the coordinates within distance d
move = find_coordinates_within_distance(coordinates, index, d)
for i in move:
    print(i)

net_strength, net_angle = vector_sum(move)
print("Net strength:", net_strength)
print("Net angle:", net_angle)