def forward_checking(csp, assignment, domains): # Comprobación hacia Adelante (Forward Checking)
    """
    Implementa el algoritmo de Comprobación hacia Adelante (Forward Checking) para resolver un CSP.
    
    :param csp: Objeto CSP que contiene variables, dominios, vecinos y restricciones.
    :param assignment: Diccionario que representa la asignación actual de variables.
    :param domains: Diccionario que representa los dominios actuales de las variables.
    :return: Una asignación completa que satisface las restricciones o None si no hay solución.
    """
    # Si todas las variables están asignadas, retornamos la solución
    if len(assignment) == len(csp.variables):
        return assignment

    # Seleccionamos una variable no asignada
    unassigned = [v for v in csp.variables if v not in assignment]
    var = unassigned[0]  # Seleccionamos la primera variable no asignada

    # Probamos cada valor del dominio de la variable seleccionada
    for value in domains[var]:
        if csp.is_consistent(var, value, assignment):  # Verificamos si la asignación es consistente
            # Creamos una copia local de los dominios para no modificar los originales
            local_domains = {v: list(domains[v]) for v in csp.variables}
            assignment[var] = value  # Asignamos el valor a la variable

            # Eliminamos valores inconsistentes de los dominios de los vecinos
            for neighbor in csp.neighbors[var]:
                if neighbor not in assignment:  # Solo consideramos vecinos no asignados
                    local_domains[neighbor] = [
                        v for v in local_domains[neighbor]
                        if csp.constraints(var, value, neighbor, v)  # Verificamos las restricciones
                    ]

            # Llamada recursiva con la nueva asignación y dominios actualizados
            result = forward_checking(csp, assignment, local_domains)
            if result:
                return result  # Si encontramos una solución, la retornamos

            # Si no encontramos solución, deshacemos la asignación
            del assignment[var]

    return None  # Si no encontramos solución, retornamos None