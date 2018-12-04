from copy import deepcopy

from CSP_sudoku_solver.ac3 import ac3 as inference

flatten_unassigned = lambda l: [item for sublist in l for item in sublist if len(item['domain']) > 1]


def complete_solution(variables: [[dict]]) -> bool:
    for column in variables:
        if any(len(var['domain']) > 1 for var in column):
            return False
    return True

def select_unassigned_value(variables: [[dict]]) -> dict:
    """ Uses MRV (Minimum Remaining Values) heuristic: """
    flat = flatten_unassigned(variables)
    flat.sort(key=lambda x: len(x['domain']))
    return flat[0]

def backtracking_search(original_variables: [[dict]], constraints: [str]) -> [[dict]] or None:
    def backtrack(variables: [[dict]]) -> [[dict]] or None:
        if complete_solution(variables):
            return variables

        var = select_unassigned_value(variables)
        domain = [val for val in var['domain']]
        for domain_value in domain:
            variables[var['y']][var['x']]['domain'] = [domain_value]
            consistant, res_vars = inference(deepcopy(variables), constraints)
            if consistant:
                result = backtrack(res_vars)
                if result:
                    return result
        return None

    return backtrack(deepcopy(original_variables))