import math as m
from point import Point


class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self._point_a = point_a
        self._point_b = point_b

    def __str__(self):
        return f'Line: [{self._point_a}, {self._point_b}]'

    def get_length(self):
        return m.sqrt((self._point_b.x - self._point_a.x) ** 2 +
                      (self._point_b.y - self._point_a.y) ** 2)

    def get_middle_point(self):
        x = (self._point_a.x + self._point_b.x) / 2
        y = (self._point_a.y + self._point_b.y) / 2

        return Point(x, y)

    def get_length_projection_x(self):
        return abs(self._point_b.x - self._point_a.x)

    def get_length_projection_y(self):
        return abs(self._point_b.y - self._point_a.y)
