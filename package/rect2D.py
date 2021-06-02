from .shape2D import Shape2D, Line
from .vector2 import Vector2


class Rect2D(Shape2D):

    def __init__(self, start=Vector2(0, 0), end=Vector2(0, 0), **kwargs):
        super().__init__(**kwargs)
        self.start = start
        self.end = end

    def render(self, surface):
        # connect start to end with rect shape
        Line(
            surface,
            Vector2(self.start.x, self.start.y) + self.position,
            Vector2(self.end.x, self.start.y) + self.position
        )
        Line(
            surface,
            Vector2(self.end.x, self.start.y) + self.position,
            Vector2(self.end.x, self.end.y) + self.position
        )
        Line(
            surface,
            Vector2(self.end.x, self.end.y) + self.position,
            Vector2(self.start.x, self.end.y) + self.position
        )
        Line(
            surface,
            Vector2(self.start.x, self.end.y) + self.position,
            Vector2(self.start.x, self.start.y) + self.position
        )
