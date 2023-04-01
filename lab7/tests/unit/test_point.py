from lab7.point import Point


def test_str():
    point = Point(123, 321)
    assert str(point) == 'Point(x: 123, y: 321)'
