from utils import get_number

figures = {3: 'triangle', 4: 'quadrilateral', 5: 'pentagon', 6: 'hexagon'}
sides_count = 0

while sides_count not in figures:
    sides_count = get_number('Enter sides count (from 3 to 6): ', int)

print(figures[sides_count])
