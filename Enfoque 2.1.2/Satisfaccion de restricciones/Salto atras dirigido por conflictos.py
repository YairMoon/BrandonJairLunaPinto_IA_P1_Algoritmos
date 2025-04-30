def backjumping_search(csp, assignment={}, level=0, conflict={}):
    if len(assignment) == len(csp.variables):
        return assignment

    var = [v for v in csp.variables if v not in assignment][0]

    for value in csp.domains[var]:
        if csp.is_consistent(var, value, assignment):
            assignment[var] = value
            result = backjumping_search(csp, assignment, level+1, conflict)
            if result:
                return result
            del assignment[var]
        else:
            # Guardamos conflicto para salto
            for neighbor in csp.neighbors[var]:
                if neighbor in assignment:
                    conflict[var] = conflict.get(var, set()) | {neighbor}

    if var in conflict:
        # Saltamos al nivel más alto con conflicto
        return None  # Se puede personalizar con lógica de salto

    return None
