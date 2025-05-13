import random  # Importamos la librería random para manejar la selección aleatoria.

# Búsqueda de Haz Local (Local Beam Search)
def local_beam_search(problem, heuristic, k=2, max_iterations=100):
    """
    Implementa el algoritmo de búsqueda de haz local.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :param k: Número de estados a mantener en cada iteración
    :param max_iterations: Número máximo de iteraciones
    :return: Mejor solución encontrada
    """
    # Selección aleatoria de k nodos iniciales.
    current_states = random.sample(list(problem.keys()), k)
    
    for _ in range(max_iterations):  # Iteramos hasta el número máximo de iteraciones.
        all_neighbors = []  # Lista para recolectar todos los vecinos de los estados actuales.
        for state in current_states:
            neighbors = problem.get(state, [])  # Obtenemos los vecinos del estado actual.
            all_neighbors.extend(neighbors)  # Agregamos los vecinos a la lista de todos los vecinos.
        
        if not all_neighbors:  # Si no hay vecinos, terminamos la búsqueda.
            break
        
        # Seleccionamos los k mejores vecinos según la función heurística.
        current_states = sorted(all_neighbors, key=heuristic, reverse=True)[:k]
    
    # Retornamos el mejor estado encontrado según la heurística.
    return max(current_states, key=heuristic)

# Definimos el espacio del problema
graph = {
    'A': ['B', 'C'],  # Desde 'A', podemos ir a 'B' y 'C'.
    'B': ['D', 'E'],  # Desde 'B', podemos ir a 'D' y 'E'.
    'C': ['F'],       # Desde 'C', podemos ir a 'F'.
    'D': [],          # 'D' es un nodo hoja.
    'E': ['G'],       # Desde 'E', podemos ir a 'G'.
    'F': [],          # 'F' es un nodo hoja.
    'G': []           # 'G' es un nodo hoja.
}

# Definimos la función heurística
def heuristic(node):
    """
    Función heurística que asigna un valor a cada nodo.
    """
    values = {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 5, 'F': 1, 'G': 6}  # Valores heurísticos de los nodos.
    return values.get(node, 0)  # Retornamos el valor heurístico del nodo.

# Ejecutar la búsqueda
best_solution = local_beam_search(graph, heuristic)  # Ejecutamos la búsqueda de haz local.
print("Mejor solución encontrada por Búsqueda de Haz Local:", best_solution)  # Mostramos la mejor solución encontrada.

# Output esperado: Mejor solución encontrada por Búsqueda de Haz Local: G
# El resultado puede variar debido a la naturaleza aleatoria de la selección de nodos iniciales.