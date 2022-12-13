'''"""
Day 8!




def parse(data: str) -> list[list[int]]:
    """ Parse input """
    trees = []
    data_list = data.splitlines()
    for line in data_list:
        line = [int(x) for x in line]
        trees.append(line)
    return trees


def visible_trees_in_forest(forest):
    """ Return the number of trees in the forest that are visible from outside the forest.
    A tree is visible if all of the other trees between it and an edge of the grid are shorter
    than it. Only consider trees in the same row or column; that is, only look up, down, left,
    or right from any given tree. """

    number_of_rows, number_of_cols = len(forest), len(str(forest[0]))
    visit = set()
    visible_trees: int = 0

    for row_index, row in enumerate(forest):
        for tree_index, tree in enumerate(row):
            if (row_index == 0) or (row_index == (len(forest) - 1)) or (tree_index == 0) or (
                tree_index == (len(row) - 1)):
                visible_trees += 1
            if tree > forest[row_index - 1]:
                visible_trees += 1

    print(visible_trees)

    return visible_trees


if __name__ == "__main__":
    for filepath in sys.argv[1:]:
        print(f"{filepath}:")
        
        forest = parse(puzzle_input)
        solution_part_1 = visible_trees_in_forest(forest)
        print(solution_part_1)
        # Learn for format this better and add Solution for partx: {solution}
        #print('\n'.join(str(solution) for solution in solutions))

"""'''

#DATA HOSTED WITH ♥ BY PASTEBIN.COM - DOWNLOAD RAW - SEE ORIGINAL
from math import prod

DIRECTION_LEFT = (-1, 0)
DIRECTION_RIGHT = (1, 0)
DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)


def measures(forest: list) -> tuple:
    return len(forest[0]), len(forest)


def get_cell(forest: list, x: int, y: int) -> int:
    width, height = measures(forest)

    if x < 0 or y < 0 or x >= width or y >= height:
        return None

    return forest[y][x]


def get_line_of_sight(forest: list, x: int, y: int, direction: tuple) -> tuple:
    # IMPORTANT: this function adds a -1 at the end, representing
    # the outside of the grid so all cell can be treated equally
    # regardless of if they're corners or not

    output = []
    vx, vy = direction
    while True:
        x += vx
        y += vy

        if (current := get_cell(forest, x, y)) is None:
            return tuple(output + [-1])

        output.append(current)


def scenic_value(cell: int, line_of_sight: tuple) -> int:
    for i, tree_height in enumerate(line_of_sight):
        if tree_height >= cell:
            return i + 1

    return len(line_of_sight) - 1


def test(forest: list):
    test_forest = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    assert (value := get_line_of_sight(test_forest, 0, 1, DIRECTION_LEFT)) == (-1,), value
    assert (value := get_line_of_sight(test_forest, 0, 1, DIRECTION_UP)) == (1, -1), value
    assert (value := get_line_of_sight(test_forest, 0, 1, DIRECTION_DOWN)) == (7, -1), value
    assert (value := get_line_of_sight(test_forest, 0, 1, DIRECTION_RIGHT)) == (0, 6, -1), value

    assert (value := scenic_value(1, (1, 2, 3, -1))) == 1, value
    assert (value := scenic_value(2, (1, 2, 3, -1))) == 2, value
    assert (value := scenic_value(3, (1, 2, 3, -1))) == 3, value
    assert (value := scenic_value(4, (1, 2, 3, -1))) == 3, value


def get_forest() -> list:
    forest = []
    for x in open('levels/level8/level8data.txt', 'r').read().strip().split('\n'):
        forest.append([int(y) for y in list(x)])

    return forest


def main2(forest: list) -> int:
    scores = []

    for x, y, cell in iterate_forest(forest):
        points = (
            scenic_value(cell, get_line_of_sight(forest, x, y, DIRECTION_UP)),
            scenic_value(cell, get_line_of_sight(forest, x, y, DIRECTION_DOWN)),
            scenic_value(cell, get_line_of_sight(forest, x, y, DIRECTION_LEFT)),
            scenic_value(cell, get_line_of_sight(forest, x, y, DIRECTION_RIGHT)),
        )

        scores.append(prod(points))

    return max(scores)


def iterate_forest(forest: list):
    width, height = measures(forest)
    for x in range(width):
        for y in range(height):
            yield x, y, get_cell(forest, x, y)


def main1(forest: list) -> int:
    amount_of_trees = 0
    for x, y, cell in iterate_forest(forest):

        conditions = (
            max(get_line_of_sight(forest, x, y, DIRECTION_UP)) < cell,
            max(get_line_of_sight(forest, x, y, DIRECTION_DOWN)) < cell,
            max(get_line_of_sight(forest, x, y, DIRECTION_LEFT)) < cell,
            max(get_line_of_sight(forest, x, y, DIRECTION_RIGHT)) < cell,
        )

        if any(conditions):
            amount_of_trees += 1

    return amount_of_trees


if __name__ == '__main__':
    forest = get_forest()
    test(forest)

    part1 = main1(forest)
    part2 = main2(forest)

    print(part1, part2)
