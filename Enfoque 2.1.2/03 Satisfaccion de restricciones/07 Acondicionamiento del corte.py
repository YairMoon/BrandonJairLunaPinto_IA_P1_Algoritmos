def condition_domains(csp): # Acondicionamiento del dominio para un CSP
    """
    Realiza el acondicionamiento del dominio para un CSP (Problema de Satisfacción de Restricciones).
    Elimina valores de los dominios que no tienen soporte en los vecinos.

    :param csp: Objeto CSP que contiene variables, dominios, vecinos y restricciones.
    :return: CSP con dominios acondicionados.
    """
    for var in csp.variables:  # Iteramos sobre cada variable del CSP.
        allowed_values = []  # Lista para almacenar los valores permitidos.
        for value in csp.domains[var]:  # Iteramos sobre los valores del dominio de la variable.
            # Verificamos si el valor tiene soporte en todos los vecinos.
            if all(
                any(csp.constraints(var, value, neighbor, v)  # Existe un valor en el vecino que satisface la restricción.
                    for v in csp.domains[neighbor])
                for neighbor in csp.neighbors[var]  # Iteramos sobre los vecinos de la variable.
            ):
                allowed_values.append(value)  # Si el valor es válido, lo añadimos a la lista.
        csp.domains[var] = allowed_values  # Actualizamos el dominio de la variable con los valores permitidos.
    return csp  # Retornamos el CSP con dominios acondicionados.