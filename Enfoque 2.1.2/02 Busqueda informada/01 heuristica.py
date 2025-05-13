# Heurísticas en Búsqueda Informada

def heuristic_example(node, goal):
    """
    Función heurística de ejemplo que mide la distancia en un grafo.
    
    :param node: Nodo actual
    :param goal: Nodo objetivo
    :return: Valor heurístico estimado (en este caso, distancia Manhattan)
    """
    x1, y1 = node  # Coordenadas del nodo actual
    x2, y2 = goal  # Coordenadas del nodo objetivo
    return abs(x1 - x2) + abs(y1 - y2)  # Distancia Manhattan como heurística

# Ejemplo de uso
goal = (5, 5)  # Nodo objetivo definido con coordenadas (5, 5)
nodes = [(2, 3), (4, 1), (3, 3), (5, 2)]  # Lista de nodos con coordenadas

# Iteramos sobre los nodos y calculamos la heurística para cada uno
for node in nodes:
    print(f"Heurística para {node} -> {heuristic_example(node, goal)}")
    # Mostramos el valor heurístico calculado para cada nodo