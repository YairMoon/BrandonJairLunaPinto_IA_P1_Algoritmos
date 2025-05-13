from queue import LifoQueue  # Importamos LifoQueue para manejar una pila (Last In, First Out).

# Búsqueda en Profundidad (DFS - Depth-First Search)
def dfs(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda en Profundidad.
    
    :param graph: Diccionario que representa el grafo {nodo: [vecinos]}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino desde start hasta goal o None si no hay camino
    """
    stack = LifoQueue()  # Pila para manejar los caminos a explorar.
    stack.put([start])  # Insertamos el nodo inicial como camino inicial.
    visited = set()  # Conjunto para registrar los nodos visitados.
    
    while not stack.empty():  # Mientras haya caminos por explorar.
        path = stack.get()  # Extraemos el camino actual de la pila.
        node = path[-1]  # Último nodo del camino actual.
        
        if node == goal:  # Si encontramos el objetivo.
            return path  # Retornamos el camino encontrado.
        
        if node not in visited:  # Si el nodo no ha sido visitado.
            visited.add(node)  # Marcamos el nodo como visitado.
            for neighbor in graph.get(node, []):  # Exploramos los vecinos del nodo actual.
                new_path = list(path)  # Copiamos el camino actual.
                new_path.append(neighbor)  # Agregamos el vecino al nuevo camino.
                stack.put(new_path)  # Lo añadimos a la pila para exploración.
    
    return None  # Si no encontramos el objetivo, retornamos None.

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],  # Desde 'A', podemos ir a 'B' y 'C'.
    'B': ['D', 'E'],  # Desde 'B', podemos ir a 'D' y 'E'.
    'C': ['F'],       # Desde 'C', podemos ir a 'F'.
    'D': [],          # 'D' es un nodo hoja.
    'E': ['F'],       # Desde 'E', podemos ir a 'F'.
    'F': []           # 'F' es un nodo hoja.
}

start = 'A'  # Nodo inicial.
goal = 'F'  # Nodo objetivo.
print("Camino encontrado por DFS:", dfs(graph, start, goal))
# Output esperado: Camino encontrado por DFS: ['A', 'C', 'F']