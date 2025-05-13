import math  # Importamos la librería math para realizar cálculos matemáticos como la función exponencial.
import random  # Importamos random para manejar la selección aleatoria.

# Búsqueda de Temple Simulado (Simulated Annealing)
def simulated_annealing(problem, heuristic, temperature=100, cooling_rate=0.95, min_temp=1):
    """
    Implementa el algoritmo de búsqueda por temple simulado.
    
    :param problem: Espacio del problema representado como un diccionario {nodo: [vecinos]}
    :param heuristic: Función heurística h(n)
    :param temperature: Temperatura inicial
    :param cooling_rate: Factor de enfriamiento
    :param min_temp: Temperatura mínima para detenerse
    :return: Mejor solución encontrada
    """
    current = random.choice(list(problem.keys()))  # Seleccionamos un nodo inicial aleatorio.
    best_solution = current  # Inicializamos la mejor solución como el nodo inicial.
    
    while temperature > min_temp:  # Mientras la temperatura sea mayor que la mínima.
        neighbors = problem.get(current, [])  # Obtenemos los vecinos del nodo actual.
        if not neighbors:  # Si no hay vecinos, terminamos la búsqueda.
            break
        
        next_node = random.choice(neighbors)  # Seleccionamos un vecino aleatorio.
        delta = heuristic(next_node) - heuristic(current)  # Calculamos la diferencia de heurística entre nodos.

        # Aceptamos el movimiento si mejora la heurística o con cierta probabilidad si no mejora.
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current = next_node  # Actualizamos el nodo actual al vecino seleccionado.

        # Actualizamos la mejor solución si el nodo actual tiene una mejor heurística.
        if heuristic(current) > heuristic(best_solution):
            best_solution = current
        
        temperature *= cooling_rate  # Reducimos la temperatura según el factor de enfriamiento.

    return best_solution  # Retornamos la mejor solución encontrada.

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
best_solution = simulated_annealing(graph, heuristic)  # Ejecutamos el algoritmo de temple simulado.
print("Mejor solución encontrada por Temple Simulado:", best_solution)  # Mostramos la mejor solución encontrada.

# Output esperado: Mejor solución encontrada por Temple Simulado: G
# El resultado puede variar debido a la naturaleza aleatoria del algoritmo.