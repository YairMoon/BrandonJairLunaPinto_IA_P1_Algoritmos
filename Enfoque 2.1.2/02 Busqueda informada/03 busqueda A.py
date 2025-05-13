import heapq  # Importamos heapq para manejar la cola de prioridad.

# Búsqueda A* (A Star Search)
def a_star_search(graph, start, goal, heuristic): 
    """
    Implementa la búsqueda A*.
    
    :param graph: Diccionario que representa el grafo {nodo: [(vecino, costo)]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :param heuristic: Función heurística h(n)
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    frontier = []  # Cola de prioridad para la frontera.
    # Insertamos el nodo inicial en la frontera con su costo f = g + h.
    heapq.heappush(frontier, (0 + heuristic(start, goal), 0, [start]))  # (f, g, camino)
    visited = {}  # Diccionario para registrar los costos mínimos de los nodos visitados.

    while frontier:  # Mientras haya nodos en la frontera.
        # Extraemos el nodo con el menor costo f de la frontera.
        _, cost, path = heapq.heappop(frontier)
        node = path[-1]  # Obtenemos el nodo actual (último en el camino).

        if node == goal:  # Si llegamos al nodo objetivo.
            return path  # Retornamos el camino encontrado.

        # Si el nodo no ha sido visitado o encontramos un costo menor.
        if node not in visited or cost < visited[node]:
            visited[node] = cost  # Registramos el menor costo para este nodo.
            # Iteramos sobre los vecinos del nodo actual.
            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost + edge_cost  # Calculamos el costo g(n) del vecino.
                new_path = path + [neighbor]  # Extendemos el camino actual.
                # Insertamos el vecino en la frontera con su costo f = g + h.
                heapq.heappush(frontier, (new_cost + heuristic(neighbor, goal), new_cost, new_path))

    return None  # Si no encontramos un camino, retornamos None.

# Función heurística de ejemplo (distancia de Manhattan)
def heuristic(node, goal):
    """
    Calcula la distancia de Manhattan entre el nodo actual y el objetivo.
    :param node: Nodo actual (x1, y1)
    :param goal: Nodo objetivo (x2, y2)
    :return: Distancia de Manhattan
    """
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)  # Distancia Manhattan: |x1 - x2| + |y1 - y2|

# Ejemplo de uso
graph = {
    (0, 0): [((1, 0), 1), ((0, 1), 1)],  # Desde (0, 0), podemos ir a (1, 0) y (0, 1) con costo 1.
    (1, 0): [((2, 0), 1)],               # Desde (1, 0), podemos ir a (2, 0) con costo 1.
    (0, 1): [((1, 1), 1)],               # Desde (0, 1), podemos ir a (1, 1) con costo 1.
    (1, 1): [((2, 1), 1)],               # Desde (1, 1), podemos ir a (2, 1) con costo 1.
    (2, 0): [((2, 1), 1), ((3, 0), 1)],  # Desde (2, 0), podemos ir a (2, 1) y (3, 0) con costo 1.
    (2, 1): [((3, 1), 1)],               # Desde (2, 1), podemos ir a (3, 1) con costo 1.
    (3, 0): [((3, 1), 1)],               # Desde (3, 0), podemos ir a (3, 1) con costo 1.
    (3, 1): []                           # (3, 1) es un nodo terminal.
}

start = (0, 0)  # Nodo inicial.
goal = (3, 1)   # Nodo objetivo.

# Ejecutamos la búsqueda A* y mostramos el camino encontrado.
print("Camino encontrado por Búsqueda A*:", a_star_search(graph, start, goal, heuristic))
# Output esperado: Camino encontrado por Búsqueda A*: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]