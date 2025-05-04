from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos una red bayesiana
# Estructura: A → B → C, además A → D y C → D

modelo = BayesianNetwork([
    ('A', 'B'),
    ('B', 'C'),
    ('A', 'D'),
    ('C', 'D')
])

# No necesitamos CPDs para analizar el manto de Markov

# Obtenemos el Manto de Markov del nodo 'B'
# Markov Blanket de 'B' = {A (padre), C (hijo), D (padre de hijo C)}
markov_blanket_B = modelo.get_markov_blanket('B')

print(f"Manto de Markov de 'B': {markov_blanket_B}")
print("El manto de Markov de un nodo incluye sus padres, hijos y padres de sus hijos.")
print("Esto significa que el estado de 'B' está completamente determinado por estos nodos.")