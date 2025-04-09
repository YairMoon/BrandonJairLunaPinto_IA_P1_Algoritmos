def condition_domains(csp):
    for var in csp.variables:
        allowed_values = []
        for value in csp.domains[var]:
            # Chequeamos si hay al menos un valor válido en cada vecino
            if all(
                any(csp.constraints(var, value, neighbor, v)
                    for v in csp.domains[neighbor])
                for neighbor in csp.neighbors[var]
            ):
                allowed_values.append(value)
        csp.domains[var] = allowed_values
    return csp