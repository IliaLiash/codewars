import numpy as np
def solve_eq(eq):
    b = []
    for element in eq:
        b.append(element.pop())
    A = np.array(eq)
    res = np.linalg.solve(A, b)
    return np.round(res, 0).tolist()