class CSP: # Definimos la clase CSP (Problema de Satisfacción de Restricciones).
    def __init__(self, variables, domains, neighbors, constraints):# Inicializador de la clase CSP
        """
        Inicializa un problema de satisfacción de restricciones (CSP).
        
        :param variables: Lista de variables (por ejemplo, regiones de un mapa).
        :param domains: Diccionario que asigna a cada variable una lista de valores posibles.
        :param neighbors: Diccionario que asigna a cada variable una lista de variables vecinas.
        :param constraints: Función que verifica si una asignación cumple las restricciones.
        """
        # Lista de variables (por ejemplo, regiones del mapa)
        self.variables = variables

        # Diccionario de dominios: variable -> lista de valores posibles
        self.domains = domains

        # Diccionario de vecinos: variable -> lista de variables vecinas
        self.neighbors = neighbors

        # Función de restricciones que toma (A, a, B, b) y devuelve True si es válido
        self.constraints = constraints

    def is_consistent(self, var, value, assignment):
        """
        Verifica si asignar 'value' a 'var' no viola restricciones con los vecinos ya asignados.
        
        :param var: Variable a asignar.
        :param value: Valor a asignar a la variable.
        :param assignment: Diccionario con las asignaciones actuales.
        :return: True si la asignación es consistente, False en caso contrario.
        """
        for neighbor in self.neighbors[var]:  # Iteramos sobre los vecinos de la variable.
            if neighbor in assignment:  # Si el vecino ya está asignado.
                # Verificamos si la restricción entre 'var' y el vecino se cumple.
                if not self.constraints(var, value, neighbor, assignment[neighbor]):
                    return False  # Si no se cumple, la asignación no es consistente.
        return True  # Si todas las restricciones se cumplen, la asignación es consistente.