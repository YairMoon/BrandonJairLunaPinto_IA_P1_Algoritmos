import random

# Algoritmos Genéticos (Genetic Algorithm)
def genetic_algorithm(population, fitness, mutate, crossover, generations=100):
    """
    Implementa un algoritmo genético básico.
    
    :param population: Lista inicial de soluciones posibles
    :param fitness: Función de aptitud que evalúa cada solución
    :param mutate: Función de mutación
    :param crossover: Función de cruce entre soluciones
    :param generations: Número de generaciones a iterar
    :return: Mejor solución encontrada
    """
    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)  # Ordenar por aptitud
        new_population = population[:2]  # Mantener los mejores individuos
        
        while len(new_population) < len(population):
            parent1, parent2 = random.sample(population[:5], 2)  # Selección de padres
            child = crossover(parent1, parent2)  # Cruce genético
            if random.random() < 0.1:  # Probabilidad de mutación
                child = mutate(child)
            new_population.append(child)
        
        population = new_population  # Actualizar la población
    
    return max(population, key=fitness)  # Retornar la mejor solución

# Definir funciones auxiliares
def fitness(solution):
    return sum(solution)  # Ejemplo: Evaluamos la aptitud sumando los valores

def mutate(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.randint(0, 10)  # Mutamos cambiando un valor aleatorio
    return solution

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)  # Punto de cruce
    return parent1[:point] + parent2[point:]

# Crear población inicial
population = [[random.randint(0, 10) for _ in range(5)] for _ in range(10)]

# Ejecutar el algoritmo genético
best_solution = genetic_algorithm(population, fitness, mutate, crossover)
print("Mejor solución encontrada por Algoritmos Genéticos:", best_solution)
# Output esperado: Mejor solución encontrada por Algoritmos Genéticos: [x, y, z, ...]
# El resultado puede variar debido a la naturaleza aleatoria de la población inicial y los procesos de cruce y mutación