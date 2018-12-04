from collections import Generator


def new_variables(board: [str]) -> [dict]:
    variables = []
    for y in range(9):
        line_variables = []
        for x in range(9):
            line_variables += [{
                'domain': [board[y][x]] if board[y][x] > 0 else list(range(1, 10)),  # Unary Constraints
                'x': x,
                'y': y,
                'x_offset': int(x / 3) * 3,
                'y_offset': int(y / 3) * 3
            }]
        variables += [line_variables]
    return variables


def get_sudoku_constraits(variables: [dict]) -> list:
    # Creating constraints for making sure the variables on
    # same line have different numbers.
    constraints = []
    diff = "d != dd"

    for i in range(9):
        constraints += [[]]
        for j in range(9):
            constraints[i] += [[]]
            for k in range(9):
                constraints[i][j] += [[]]
                for _ in range(9):
                    constraints[i][j][k] += [None]


    for col in variables:
        for var in col:
            for i in range(9):
                x, y = var['x'], var['y']
                if i != var['x']:
                    xx, yy = i, var['y']
                    constraints[y][x][yy][xx] = diff

                if i != var['y']:
                    xx, yy = var['x'], i
                    constraints[y][x][yy][xx] = diff


    # Creating constraints that check if the variables on
    # the same square is different
    for col in variables:
        for var in col:
            x, y = var['x'], var['y']
            for yy in range(var['y_offset'], var['y_offset'] + 3):
                for xx in range(var['x_offset'], var['x_offset'] + 3):
                    if x != xx or y != yy:
                        constraints[y][x][yy][xx] = diff
    return constraints


def find_neighbours(var: dict, var2:dict, variables: [dict], constraints) -> Generator:
    x, y = var['x'], var['y']
    for i in range(9):
        if i != x and not var2 == variables[y][i]:
            yield (var, variables[y][i], constraints[y][x][y][i])
        if i != y and not var2 == variables[i][x]:
            yield (var, variables[i][x], constraints[y][x][i][x])

    for yy in range(var['y_offset'], var['y_offset'] + 3):
        for xx in range(var['x_offset'], var['x_offset'] + 3):
            if (not (y == yy and var['x_offset'] <= xx < var['x_offset'] + 3)
            and not (x == xx and var['y_offset'] <= yy < var['y_offset'] + 3)
            and not (x == xx and y == yy)
            and not (var2 == variables[yy][xx])):
                yield (var, variables[yy][xx], constraints[y][x][yy][xx])
