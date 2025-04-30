import math
import random

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
    current = random.choice(list(problem.keys()))  # Nodo inicial aleatorio
    best_solution = current  # Mejor solución encontrada
    
    while temperature > min_temp:
        neighbors = problem.get(current, [])  # Obtener vecinos
        if not neighbors:
            break  # Si no hay vecinos, detenerse
        
        next_node = random.choice(neighbors)  # Seleccionar vecino aleatorio
        delta = heuristic(next_node) - heuristic(current)  # Diferencia de heurística
        
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current = next_node  # Aceptar movimiento
        
        if heuristic(current) > heuristic(best_solution):
            best_solution = current  # Actualizar mejor solución
        
        temperature *= cooling_rate  # Enfriar temperatura
    
    return best_solution

# Definimos el espacio del problema
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Definimos la función heurística
def heuristic(node):
    values = {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 5, 'F': 1, 'G': 6}
    return values.get(node, 0)

# Ejecutar la búsqueda
best_solution = simulated_annealing(graph, heuristic)
print("Mejor solución encontrada por Temple Simulado:", best_solution)
# Output esperado: Mejor solución encontrada por Temple Simulado: G 