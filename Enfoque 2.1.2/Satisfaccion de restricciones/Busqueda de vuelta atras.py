def backtracking_search(csp, assignment={}):
    # Si ya se asignaron todas las variables, retorna la solución
    if len(assignment) == len(csp.variables):
        return assignment

    # Elegimos la siguiente variable no asignada
    unassigned = [v for v in csp.variables if v not in assignment]
    var = unassigned[0]

    # Probamos cada valor del dominio
    for value in csp.domains[var]:
        if csp.is_consistent(var, value, assignment):
            # Si es consistente, asignamos y continuamos recursivamente
            assignment[var] = value
            result = backtracking_search(csp, assignment)
            if result:
                return result
            # Si no resultó, deshacemos (backtrack)
            del assignment[var]

    return None  # Si no hay solución
