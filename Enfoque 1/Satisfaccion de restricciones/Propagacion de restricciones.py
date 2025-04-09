from collections import deque

def ac3(csp):
    queue = deque((xi, xj) for xi in csp.variables for xj in csp.neighbors[xi])

    while queue:
        (xi, xj) = queue.popleft()
        if revise(csp, xi, xj):
            if not csp.domains[xi]:
                return False
            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(csp, xi, xj):
    revised = False
    for x in csp.domains[xi][:]:
        # Si no hay ningún valor en xj que satisfaga la restricción con x, eliminamos x
        if not any(csp.constraints(xi, x, xj, y) for y in csp.domains[xj]):
            csp.domains[xi].remove(x)
            revised = True
    return revised
