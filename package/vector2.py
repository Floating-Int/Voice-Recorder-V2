import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) is type(self):
            return Vector2(self.x + other.x, self.y + other.y)
        raise NotImplementedError

    def __sub__(self, other):
        if type(other) is type(self):
            return Vector2(self.x - other.x, self.y - other.y)
        raise NotImplementedError

    def __mul__(self, other):
        if type(other) is type(self):
            return Vector2(self.x * other.x, self.y * other.y)
        elif type(other) is int or type(other) is float:
            return Vector2(self.x * other, self.y * other)
        raise NotImplementedError

    def __truediv__(self, other):
        return Vector2()

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)

    def to_tuple(self):
        return (self.x, self.y)
