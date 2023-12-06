import math

# Function to normalize coordinates
def normalize_coordinates(coords):
    normalized_coords = []
    for x, y in coords:
        # Calculate the magnitude of the vector
        magnitude = math.sqrt(x**2 + y**2)
        
        # Normalize coordinates to lie on the unit circle
        normalized_x = x / magnitude
        normalized_y = y / magnitude
        
        # Preserve the ratio between x and y
        ratio = y / x if x != 0 else 1  # Avoid division by zero
        
        # Adjust normalized coordinates to maintain the ratio
        adjusted_y = math.sqrt(1 - normalized_x**2)
        adjusted_x = adjusted_y * math.copysign(1, x) * abs(ratio) if x != 0 else 0
        
        normalized_coords.append((adjusted_x, adjusted_y))
    
    return normalized_coords

# Example coordinates
coordinates = [(3, 4), (-2, 5), (1, -1), (-3, -4)]

# Normalize coordinates
normalized_coordinates = normalize_coordinates(coordinates)
print("Original Coordinates:", coordinates)
print("Normalized Coordinates:", normalized_coordinates)
