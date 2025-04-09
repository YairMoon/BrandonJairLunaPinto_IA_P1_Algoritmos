def forward_checking(csp, assignment, domains):
    if len(assignment) == len(csp.variables):
        return assignment

    unassigned = [v for v in csp.variables if v not in assignment]
    var = unassigned[0]

    for value in domains[var]:
        if csp.is_consistent(var, value, assignment):
            local_domains = {v: list(domains[v]) for v in csp.variables}
            assignment[var] = value

            # Eliminamos valores inconsistentes de vecinos
            for neighbor in csp.neighbors[var]:
                if neighbor not in assignment:
                    local_domains[neighbor] = [
                        v for v in local_domains[neighbor]
                        if csp.constraints(var, value, neighbor, v)
                    ]

            result = forward_checking(csp, assignment, local_domains)
            if result:
                return result

            del assignment[var]

    return None
