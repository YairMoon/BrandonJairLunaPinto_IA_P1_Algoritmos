from queue import Queue

# Búsqueda en Anchura (BFS - Breadth-First Search)
def bfs(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda en Anchura.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    queue = Queue()  # Cola para manejar los caminos a explorar
    queue.put([start])  # Agregamos el nodo inicial como camino inicial
    visited = set()  # Conjunto para registrar los nodos visitados
    
    while not queue.empty(): ## Mientras haya caminos por explorar
        path = queue.get()  # Extraemos el camino actual de la cola
        node = path[-1]  # Último nodo del camino actual
        
        if node == goal: ## Si el nodo actual es el objetivo, retornamos el camino
            return path  # Si encontramos el objetivo, retornamos el camino
        
        if node not in visited: # Si el nodo no ha sido visitado
            visited.add(node)  # Marcamos el nodo como visitado
            for neighbor in graph.get(node, []):  # Exploramos los vecinos
                new_path = list(path)  # Copiamos el camino actual
                new_path.append(neighbor)  # Agregamos el vecino al nuevo camino
                queue.put(new_path)  # Lo añadimos a la cola para exploración
    
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
print("Camino encontrado por BFS:", bfs(graph, start, goal))
