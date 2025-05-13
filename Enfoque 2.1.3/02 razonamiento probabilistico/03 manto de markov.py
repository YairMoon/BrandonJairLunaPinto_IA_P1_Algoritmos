from pgmpy.models import BayesianNetwork # Importamos la clase BayesianNetwork de pgmpy.models
from pgmpy.factors.discrete import TabularCPD # Importamos TabularCPD para definir las CPDs (tablas de probabilidad)
from pgmpy.inference import VariableElimination # Importamos VariableElimination para realizar inferencias en la red bayesiana

# Creamos una red bayesiana
# Estructura: A → B → C, además A → D y C → D
modelo = BayesianNetwork([
    ('A', 'B'),
    ('B', 'C'),
    ('A', 'D'),
    ('C', 'D')
])
# Definimos una red bayesiana con cuatro nodos: A, B, C y D.
# Las relaciones son:
# - A afecta a B.
# - B afecta a C.
# - A y C afectan a D.

# No necesitamos CPDs para analizar el manto de Markov

# Obtenemos el Manto de Markov del nodo 'B'
markov_blanket_B = modelo.get_markov_blanket('B')
# El manto de Markov de un nodo incluye:
# - Sus padres (nodos que lo afectan directamente).
# - Sus hijos (nodos que dependen de él).
# - Los padres de sus hijos (nodos que afectan a sus hijos).

print(f"Manto de Markov de 'B': {markov_blanket_B}")
# Mostramos el manto de Markov del nodo 'B'.

print("El manto de Markov de un nodo incluye sus padres, hijos y padres de sus hijos.")
print("Esto significa que el estado de 'B' está completamente determinado por estos nodos.")
# Explicamos el significado del manto de Markov.