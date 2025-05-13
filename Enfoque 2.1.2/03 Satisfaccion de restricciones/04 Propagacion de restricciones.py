from collections import deque  # Importamos deque para manejar una cola de arcos de manera eficiente.

def ac3(csp):
    """
    Implementa el algoritmo AC-3 (Arc Consistency 3) para la propagación de restricciones en un CSP.
    
    :param csp: Objeto CSP que contiene variables, dominios, vecinos y restricciones.
    :return: True si el CSP es consistente, False si algún dominio queda vacío.
    """
    # Inicializamos la cola con todos los arcos (xi, xj) del CSP
    queue = deque((xi, xj) for xi in csp.variables for xj in csp.neighbors[xi])

    while queue:  # Mientras haya arcos en la cola
        (xi, xj) = queue.popleft()  # Extraemos un arco (xi, xj) de la cola
        if revise(csp, xi, xj):  # Revisamos si el dominio de xi necesita ser reducido
            if not csp.domains[xi]:  # Si el dominio de xi queda vacío, el CSP no es consistente
                return False
            # Si el dominio de xi cambió, añadimos los arcos relacionados con xi a la cola
            for xk in csp.neighbors[xi]:
                if xk != xj:  # Evitamos volver a añadir el arco (xi, xj)
                    queue.append((xk, xi))
    return True  # Si procesamos todos los arcos sin problemas, el CSP es consistente

def revise(csp, xi, xj):
    """
    Revisa el arco (xi, xj) y elimina valores inconsistentes del dominio de xi.
    
    :param csp: Objeto CSP.
    :param xi: Variable origen del arco.
    :param xj: Variable destino del arco.
    :return: True si el dominio de xi fue modificado, False en caso contrario.
    """
    revised = False
    for x in csp.domains[xi][:]:  # Iteramos sobre una copia del dominio de xi
        # Si no hay ningún valor en xj que satisfaga la restricción con x, eliminamos x
        if not any(csp.constraints(xi, x, xj, y) for y in csp.domains[xj]):
            csp.domains[xi].remove(x)  # Eliminamos el valor inconsistente
            revised = True  # Indicamos que el dominio de xi fue modificado
    return revised  # Retornamos si hubo cambios en el dominio de xi