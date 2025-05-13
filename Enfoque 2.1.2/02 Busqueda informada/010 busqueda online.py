import random  # Importamos la librería random para manejar la selección aleatoria.

# Búsqueda Online (Online Search)
def online_search(problem, heuristic, start):
    """
    Implementa el algoritmo de búsqueda online.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :param start: Nodo inicial
    :return: Mejor solución encontrada
    """
    current = start  # Nodo inicial
    visited = set()  # Conjunto de nodos visitados
    
    while True:
        visited.add(current)  # Marcar nodo como visitado
        neighbors = [n for n in problem.get(current, []) if n not in visited]  # Filtrar vecinos no visitados
        
        if not neighbors:  # Si no hay vecinos sin visitar.
            return current  # Retornamos el nodo actual como solución.
        
        current = min(neighbors, key=heuristic)  # Elegir el vecino con menor heurística.

# Definir espacio del problema
graph = {
    'A': ['B', 'C'],  # Desde 'A', podemos ir a 'B' y 'C'.
    'B': ['D', 'E'],  # Desde 'B', podemos ir a 'D' y 'E'.
    'C': ['F'],       # Desde 'C', podemos ir a 'F'.
    'D': [],          # 'D' es un nodo hoja.
    'E': ['G'],       # Desde 'E', podemos ir a 'G'.
    'F': [],          # 'F' es un nodo hoja.
    'G': []           # 'G' es un nodo hoja.
}

# Definir función heurística
def heuristic(node):
    """
    Función heurística que asigna un valor a cada nodo.
    """
    values = {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 5, 'F': 1, 'G': 6}  # Valores heurísticos de los nodos.
    return values.get(node, 0)  # Retornamos el valor heurístico del nodo.

# Ejecutar la búsqueda
start_node = 'A'  # Nodo inicial.
best_solution = online_search(graph, heuristic, start_node)  # Ejecutamos la búsqueda online.
print("Mejor solución encontrada por Búsqueda Online:", best_solution)  # Mostramos la mejor solución encontrada.

# Output esperado: Mejor solución encontrada por Búsqueda Online: G
# El resultado puede variar dependiendo de la estructura del grafo y la heurística.