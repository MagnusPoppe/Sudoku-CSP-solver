from CSP_sudoku_solver import setup, printing
from CSP_sudoku_solver.ac3 import ac3
from CSP_sudoku_solver.backtracking_search import backtracking_search


def solve_sudoku(filename) -> [[int]] or None:
    with open(filename, "r") as file:
        board = [[int(x) for x in line.strip("\n").strip("\r")] for line in file.readlines()]

    # CSP Setup:
    all_variables = setup.new_variables(board)
    all_constraints = setup.get_sudoku_constraits(all_variables)

    # Starting CSP algorithm:
    partial_solution, all_variables = ac3(all_variables, all_constraints)
    if partial_solution:
        solution = backtracking_search(all_variables, all_constraints)

        if solution:
            # TESTING RESULTS:
            solution_board = []
            for i, column in enumerate(solution):
                solution_board += [[]]
                for var in column:
                    solution_board[i] += [var['domain'][0]]

            # Checking if all lines on the solution board is consistent with constraints
            for i in range(9):
                x_possible = list(range(1, 10))
                y_possible = list(range(1, 10))
                for j in range(9):
                    x_possible.remove(solution_board[i][j])
                    y_possible.remove(solution_board[j][i])
                assert len(x_possible) == len(y_possible) == 0

            # Testing if solution board maintained the original board rules:
            for y in range(9):
                for x in range(9):
                    if board[y][x] > 0:
                        assert solution_board[y][x] == board[y][x]
            return solution
    else:
        return None

if __name__ == '__main__':
    import time

    for board_name in ['easy', 'medium', 'hard', 'veryhard']:
        setup_start = time.time()
        filename = './sudokus/{}.txt'.format(board_name)
        solution = solve_sudoku(filename)
        print("{} solved in {:.3} sec"
              .format(filename, time.time() - setup_start)
        )

