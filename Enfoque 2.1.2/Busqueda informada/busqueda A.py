import heapq

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
    frontier = []  # Cola de prioridad para la frontera
    heapq.heappush(frontier, (0 + heuristic(start, goal), 0, [start]))  # (f, g, camino)
    visited = {}
    
    while frontier:
        _, cost, path = heapq.heappop(frontier)  # Extraemos el nodo con menor costo f
        node = path[-1]
        
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if node not in visited or cost < visited[node]:
            visited[node] = cost  # Registramos el menor costo
            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost + heuristic(neighbor, goal), new_cost, new_path))
    
    return None  # Si no encontramos un camino, retornamos None

# Función heurística de ejemplo (distancia de Manhattan)
def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Ejemplo de uso
graph = {
    (0, 0): [((1, 0), 1), ((0, 1), 1)],
    (1, 0): [((2, 0), 1)],
    (0, 1): [((1, 1), 1)],
    (1, 1): [((2, 1), 1)],
    (2, 0): [((2, 1), 1), ((3, 0), 1)],
    (2, 1): [((3, 1), 1)],
    (3, 0): [((3, 1), 1)],
    (3, 1): []
}

start = (0, 0)
goal = (3, 1)
print("Camino encontrado por Búsqueda A*:", a_star_search(graph, start, goal, heuristic))
# Output esperado: Camino encontrado por Búsqueda A*: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]