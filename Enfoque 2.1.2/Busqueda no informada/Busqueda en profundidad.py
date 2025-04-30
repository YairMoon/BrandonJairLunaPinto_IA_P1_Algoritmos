from queue import LifoQueue

# Búsqueda en Profundidad (DFS - Depth-First Search)
def dfs(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda en Profundidad.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    stack = LifoQueue()  # Pila para manejar los caminos a explorar
    stack.put([start])  # Insertamos el nodo inicial como camino inicial
    visited = set()  # Conjunto para registrar los nodos visitados
    
    while not stack.empty(): # Mientras haya caminos por explorar
        path = stack.get()  # Extraemos el camino actual de la pila
        node = path[-1]  # Último nodo del camino actual
        
        if node == goal:
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if node not in visited:
            visited.add(node)  # Marcamos el nodo como visitado
            for neighbor in graph.get(node, []):  # Exploramos los vecinos
                new_path = list(path)  # Copiamos el camino actual
                new_path.append(neighbor)  # Agregamos el vecino al nuevo camino
                stack.put(new_path)  # Lo añadimos a la pila para exploración
    
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
print("Camino encontrado por DFS:", dfs(graph, start, goal))
