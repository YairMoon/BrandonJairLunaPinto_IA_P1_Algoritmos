from collections import deque

# Búsqueda en Grafos (Graph Search)
def graph_search(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda en Grafos (BFS con nodos visitados).
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    queue = deque([[start]])  # Cola para manejar los caminos a explorar
    visited = set()  # Conjunto de nodos visitados
    
    while queue:
        path = queue.popleft()  # Extraemos el camino más antiguo (FIFO)
        node = path[-1]  # Último nodo del camino actual
        
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if node not in visited:
            visited.add(node)  # Marcamos el nodo como visitado
            for neighbor in graph.get(node, []):  # Exploramos los vecinos
                new_path = list(path)  # Copiamos el camino actual
                new_path.append(neighbor)  # Agregamos el vecino al nuevo camino
                queue.append(new_path)  # Lo añadimos a la cola para exploración
    
    return None  # Si no encontramos el objetivo, retornamos None

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
print("Camino encontrado por Búsqueda en Grafos:", graph_search(graph, start, goal))
