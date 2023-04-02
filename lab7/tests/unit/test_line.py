import math as m


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x: {self.x}, y: {self.y})'


class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def __str__(self):
        return f'Line: [{self.point_a}, {self.point_b}]'

    def get_length(self):
        return m.sqrt((self.point_b.x - self.point_a.x) ** 2 +
                      (self.point_b.y - self.point_a.y) ** 2)

    def get_middle_point(self):
        x = (self.point_a.x + self.point_b.x) / 2
        y = (self.point_a.y + self.point_b.y) / 2

        return Point(x, y)

    def get_length_projection_x(self):
        return abs(self.point_b.x - self.point_a.x)

    def get_length_projection_y(self):
        return abs(self.point_b.y - self.point_a.y)


def test_get_length():
    line = Line(Point(1, 2), Point(4, 6))
    assert line.get_length() == 5.0


def test_get_middle_point():
    line = Line(Point(1, 2), Point(3, 4))
    middle_point = line.get_middle_point()
    assert middle_point.x == 2.0 and middle_point.y == 3.0


def test_get_length_projection_x():
    line = Line(Point(1, 2), Point(5, 2))
    assert line.get_length_projection_x() == 4


def test_get_length_projection_y():
    line = Line(Point(1, 2), Point(1, 5))
    assert line.get_length_projection_y() == 3


def test_str():
    line = Line(Point(132, 212), Point(112, 335))
    assert str(line) == 'Line: [Point(x: 132, y: 212), Point(x: 112, y: 335)]'
