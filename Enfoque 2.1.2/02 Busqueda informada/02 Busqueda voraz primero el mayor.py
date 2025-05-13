import heapq  # Importamos heapq para manejar la cola de prioridad.

# Búsqueda Voraz Primero el Mejor (Greedy Best-First Search)
def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Implementa la búsqueda voraz primero el mejor.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :param heuristic: Función heurística h(n)
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    frontier = []  # Cola de prioridad para la frontera
    # Insertamos el nodo inicial en la frontera con su valor heurístico.
    heapq.heappush(frontier, (heuristic(start, goal), [start]))  # (heurística, camino)
    visited = set()  # Conjunto para registrar los nodos visitados.
    
    while frontier:  # Mientras haya nodos en la frontera.
        _, path = heapq.heappop(frontier)  # Extraemos el nodo con menor valor heurístico.
        node = path[-1]  # Obtenemos el nodo actual (último en el camino).
        
        if node == goal:  # Si llegamos al nodo objetivo.
            return path  # Retornamos el camino encontrado.
        
        if node not in visited:  # Si el nodo no ha sido visitado.
            visited.add(node)  # Marcamos el nodo como visitado.
            for neighbor in graph.get(node, []):  # Iteramos sobre los vecinos del nodo actual.
                if neighbor not in visited:  # Si el vecino no ha sido visitado.
                    new_path = path + [neighbor]  # Generamos un nuevo camino extendido.
                    # Añadimos el vecino a la frontera con su valor heurístico.
                    heapq.heappush(frontier, (heuristic(neighbor, goal), new_path))
    
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
    (0, 0): [(1, 0), (0, 1)],  # Desde (0, 0), podemos ir a (1, 0) y (0, 1).
    (1, 0): [(2, 0)],          # Desde (1, 0), podemos ir a (2, 0).
    (0, 1): [(1, 1)],          # Desde (0, 1), podemos ir a (1, 1).
    (1, 1): [(2, 1)],          # Desde (1, 1), podemos ir a (2, 1).
    (2, 0): [(2, 1), (3, 0)],  # Desde (2, 0), podemos ir a (2, 1) y (3, 0).
    (2, 1): [(3, 1)],          # Desde (2, 1), podemos ir a (3, 1).
    (3, 0): [(3, 1)],          # Desde (3, 0), podemos ir a (3, 1).
    (3, 1): []                 # (3, 1) es un nodo terminal.
}

start = (0, 0)  # Nodo inicial.
goal = (3, 1)   # Nodo objetivo.

# Ejecutamos la búsqueda voraz primero el mejor y mostramos el camino encontrado.
print("Camino encontrado por Búsqueda Voraz Primero el Mejor:", greedy_best_first_search(graph, start, goal, heuristic))
# Output esperado: Camino encontrado por Búsqueda Voraz Primero el Mejor: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]