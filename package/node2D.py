from .node import Node
from .vector2 import Vector2


class Node2D(Node):

    def __init__(self, position=Vector2(0, 0), scale=Vector2(1, 1), **kwargs):
        super().__init__(**kwargs)
        self.position = position
        self.scale = scale

    def move(self, amount=Vector2(0, 0)):
        self.position += amount
