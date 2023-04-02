from utils import get_number

figures = ['triangle', 'quadrilateral', 'pentagon', 'hexagon']
sides_count = 0

while sides_count < 3 or sides_count > 6:
    sides_count = get_number('Enter sides count (from 3 to 6): ', int)

print(figures[sides_count - 3])
