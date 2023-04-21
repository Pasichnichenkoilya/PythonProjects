from utils import get_number


def get_figure_name(sides: int) -> str:
    figures = {3: 'triangle', 4: 'quadrilateral', 5: 'pentagon', 6: 'hexagon'}
    return figures[sides] if sides in figures else None


if __name__ == '__main__':
    sides_count = 0
    while sides_count < 3 or sides_count > 6:
        sides_count = get_number('Enter sides count (from 3 to 6): ', int)

    print(get_figure_name(sides_count))
