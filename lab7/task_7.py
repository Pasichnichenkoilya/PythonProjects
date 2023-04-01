from point import Point
from line import Line

line = Line(Point(1, 1), Point(4, 4))

print(line)
print(f'Line length: {round(line.get_length(), 2)}')
print(f'Middle point: {line.get_middle_point()}')
print(f'Projection x: {line.get_length_projection_x()}')
print(f'Projection y: {line.get_length_projection_y()}')
