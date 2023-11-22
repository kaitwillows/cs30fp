# from re import X
# idk why ^that line is there i legit did not type that

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinates(new_x, new_y)

    def as_tuple(self):
        return self.x, self.y