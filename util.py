# from re import X
# idk why ^that line is there i legit did not type that

# class Coordinates:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Coordinates(new_x, new_y)

#     def as_tuple(self):
#         return self.x, self.y


def add_coordinates(coord1: tuple[float, float], coord2: tuple[float, float]) -> tuple[float, float]:
    x1, y1 = coord1
    x2, y2 = coord2
    new_x = x1 + x2
    new_y = y1 + y2
    return new_x, new_y



def collision():
    pass