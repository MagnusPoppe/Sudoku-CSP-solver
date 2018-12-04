def print_constraints_board_style(x, y, constraints):
    for yy in range(9):
        for xx in range(9):
            if x == xx and y == yy:
                print("X", end=" ")
            else:
                print("#" if constraints[y][x][yy][xx] else ".", end=" ")
        print()


def print_variables_board_style(variables):
    for column in variables:
        for var in column:
            if len(var['domain']) == 1:
                print(var['domain'][0], end="  ")
            elif len(var['domain']) > 1:
                print(".", end="  ")
            elif len(var['domain']) == 0:
                print("#", end="  ")
        print()


def print_remaining_variables_board_style(variables):
    for column in variables:
        for var in column:
            print(len(var['domain']), end="  ")
        print()