class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x: {self.x}, y: {self.y})'


def test_str():
    point = Point(123, 321)
    assert str(point) == 'Point(x: 123, y: 321)'
