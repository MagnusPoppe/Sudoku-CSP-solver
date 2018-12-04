from collections import Generator

from CSP_sudoku_solver import setup

def revise(var_1: dict, var_2: dict, constraint: str) -> bool:
    revised = False
    cleaning = []

    def satisfies_constraint(d) -> Generator:
        """ Returns true if any of the values in domain of var_2
            allows value d of domain in var_1 to be satisfied
        """
        for dd in var_2['domain']:
            yield eval(constraint)

    for d in var_1['domain']:
        if not any(satisfies_constraint(d)):
            cleaning += [d]
            revised = True

    for d in cleaning:
        var_1['domain'].remove(d)

    return revised


def ac3(variables: [dict], constraints: [str]) -> (bool, [dict]):
    queue = []
    for column in variables:
        for var in column:
            queue += setup.find_neighbours(var, None, variables, constraints)

    while queue:
        var_1, var_2, constraint = queue.pop(0)
        if revise(var_1, var_2, constraint):
            if len(var_1['domain']) == 0:
                return False, variables
            queue += setup.find_neighbours(var_1, var_2, variables, constraints)
    return True, variables