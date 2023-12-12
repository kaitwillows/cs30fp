import math

def convert_to_unit_circle(x, y):
    # Calculate the magnitude (distance from origin) of the point
    magnitude = math.sqrt(x**2 + y**2)
    
    # Calculate the coordinates on the unit circle
    if magnitude != 0:
        unit_x = x / magnitude
        unit_y = y / magnitude
    else:
        unit_x, unit_y = 0, 0
    
    return unit_x, unit_y

# Example coordinates
x, y = 0, 10

unit_x, unit_y = convert_to_unit_circle(x, y)
print(f"The original point ({x}, {y}) is roughly ({unit_x:.3f}, {unit_y:.3f}) on the unit circle.")
