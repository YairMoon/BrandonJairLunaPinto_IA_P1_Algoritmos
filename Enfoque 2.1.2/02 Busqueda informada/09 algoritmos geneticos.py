import random  # Importamos la librería random para manejar la aleatoriedad.

# Algoritmos Genéticos (Genetic Algorithm)
def genetic_algorithm(population, fitness, mutate, crossover, generations=100):
    """
    Implementa un algoritmo genético básico.
    
    :param population: Lista inicial de soluciones posibles.
    :param fitness: Función de aptitud que evalúa cada solución.
    :param mutate: Función de mutación que modifica una solución.
    :param crossover: Función de cruce entre dos soluciones.
    :param generations: Número de generaciones a iterar.
    :return: Mejor solución encontrada.
    """
    for _ in range(generations):  # Iteramos sobre el número de generaciones.
        # Ordenamos la población por aptitud en orden descendente.
        population = sorted(population, key=fitness, reverse=True)
        new_population = population[:2]  # Conservamos los dos mejores individuos.

        # Generamos nuevos individuos hasta completar la población.
        while len(new_population) < len(population):
            # Seleccionamos dos padres aleatorios de los mejores 5 individuos.
            parent1, parent2 = random.sample(population[:5], 2)
            child = crossover(parent1, parent2)  # Realizamos el cruce genético.
            if random.random() < 0.1:  # Con probabilidad del 10%, aplicamos mutación.
                child = mutate(child)
            new_population.append(child)  # Añadimos el hijo a la nueva población.

        population = new_population  # Actualizamos la población con la nueva generación.

    # Retornamos la mejor solución encontrada según la función de aptitud.
    return max(population, key=fitness)

# Definir funciones auxiliares
def fitness(solution):
    """
    Función de aptitud que evalúa una solución.
    En este caso, la aptitud es la suma de los valores de la solución.
    """
    return sum(solution)

def mutate(solution):
    """
    Función de mutación que modifica un valor aleatorio de la solución.
    """
    index = random.randint(0, len(solution) - 1)  # Seleccionamos un índice aleatorio.
    solution[index] = random.randint(0, 10)  # Cambiamos el valor en ese índice por un número aleatorio.
    return solution

def crossover(parent1, parent2):
    """
    Función de cruce que combina dos soluciones.
    """
    point = random.randint(1, len(parent1) - 1)  # Seleccionamos un punto de cruce aleatorio.
    return parent1[:point] + parent2[point:]  # Combinamos las partes de los padres.

# Crear población inicial
population = [[random.randint(0, 10) for _ in range(5)] for _ in range(10)]  # Generamos 10 soluciones aleatorias.

# Ejecutar el algoritmo genético
best_solution = genetic_algorithm(population, fitness, mutate, crossover)  # Ejecutamos el algoritmo.
print("Mejor solución encontrada por Algoritmos Genéticos:", best_solution)  # Mostramos la mejor solución encontrada.

# Output esperado: Mejor solución encontrada por Algoritmos Genéticos: [x, y, z, ...]
# El resultado puede variar debido a la naturaleza aleatoria de la población inicial y los procesos de cruce y mutación.