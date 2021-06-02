from .node2D import Node2D
from .vector2 import Vector2


class Shape2D(Node2D):

    def __init__(self, points=[Vector2(0, 0)], **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def render(self, surface):
        last_point = self.points[0]
        # connect points
        for i in range(len(self.points)):
            Line(
                surface,
                last_point + self.position,
                self.points[i] + self.position
            )
            last_point = self.points[i]
        # connect end to start
        Line(
            surface,
            last_point + self.position,
            self.points[0] + self.position
        )


class Line:
    def __init__(self, surface, start=Vector2(0, 0), end=Vector2(0, 0), color=(0, 0, 0), width=2):
        pygame.draw.line(
            surface,
            color,
            start.to_tuple(),
            end.to_tuple(),
            width
        )
