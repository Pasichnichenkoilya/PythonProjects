import math as m
from point import Point


class Line:
    point_a = Point(0, 0)
    point_b = Point(1, 1)

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def __str__(self):
        return f'Line: [{self.point_a}, {self.point_b}]'

    def get_length(self):
        return m.sqrt((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2)

    def get_middle_point(self):
        x = (self.point_a.x + self.point_b.x) / 2
        y = (self.point_a.y + self.point_b.y) / 2

        return Point(x, y)

    def get_length_projection_x(self):
        return abs(self.point_b.x - self.point_a.x)

    def get_length_projection_y(self):
        return abs(self.point_b.y - self.point_a.y)
