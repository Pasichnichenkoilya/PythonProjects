from lab7.point import Point
from lab7.line import Line


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
