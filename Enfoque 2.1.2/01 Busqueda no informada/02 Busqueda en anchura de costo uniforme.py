from queue import PriorityQueue  # Importamos PriorityQueue para manejar la cola de prioridad.

# Búsqueda de Costo Uniforme (Uniform Cost Search - UCS)
def uniform_cost_search(graph, start, goal):
    """
    Implementa el algoritmo de Búsqueda de Costo Uniforme.
    
    :param graph: Diccionario que representa el grafo con costos {nodo: {vecino: costo}}
    :param start: Nodo inicial
    :param goal: Nodo objetivo
    :return: Lista con el camino más barato desde start hasta goal o None si no hay camino
    """
    queue = PriorityQueue()  # Cola de prioridad para manejar caminos y costos.
    queue.put((0, [start]))  # Insertamos el nodo inicial con costo 0.
    visited = set()  # Conjunto de nodos visitados para evitar ciclos.
    
    while not queue.empty():  # Mientras la cola no esté vacía.
        cost, path = queue.get()  # Extraemos el camino de menor costo.
        node = path[-1]  # Último nodo del camino actual.
        
        if node == goal:  # Si encontramos el objetivo.
            return path  # Retornamos el camino encontrado.
        
        if node not in visited:  # Si el nodo no ha sido visitado.
            visited.add(node)  # Marcamos el nodo como visitado.
            for neighbor, weight in graph.get(node, {}).items():  # Exploramos los vecinos del nodo actual.
                new_path = list(path)  # Copiamos el camino actual.
                new_path.append(neighbor)  # Agregamos el vecino al camino.
                queue.put((cost + weight, new_path))  # Lo agregamos a la cola con su costo actualizado.
    
    return None  # Si no encontramos el objetivo, retornamos None.

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},  # Desde 'A', podemos ir a 'B' con costo 1 y a 'C' con costo 4.
    'B': {'D': 2, 'E': 5},  # Desde 'B', podemos ir a 'D' con costo 2 y a 'E' con costo 5.
    'C': {'F': 3},          # Desde 'C', podemos ir a 'F' con costo 3.
    'D': {},                # 'D' no tiene vecinos.
    'E': {'F': 1},          # Desde 'E', podemos ir a 'F' con costo 1.
    'F': {}                 # 'F' es un nodo terminal.
}

start = 'A'  # Nodo inicial.
goal = 'F'  # Nodo objetivo.
print("Camino encontrado por UCS:", uniform_cost_search(graph, start, goal))
# Output esperado: Camino encontrado por UCS: ['A', 'B', 'E', 'F']