from pgmpy.models import BayesianNetwork # Importamos la clase BayesianNetwork de pgmpy.models
from pgmpy.factors.discrete import TabularCPD # Importamos TabularCPD para definir las CPDs (tablas de probabilidad)
from pgmpy.inference import VariableElimination # Importamos VariableElimination para realizar inferencias en la red bayesiana
# Definimos una red bayesiana: lluvia → mojado
modelo = BayesianNetwork([ 
    ('lluvia', 'mojado')
])
# Creamos una red bayesiana simple con dos nodos: "lluvia" y "mojado".
# La relación es que "lluvia" afecta si algo está "mojado".

# Definimos las CPDs (tablas de probabilidad)
cpd_lluvia = TabularCPD(variable='lluvia', variable_card=2, values=[[0.2], [0.8]]) 
# Definimos la probabilidad marginal de "lluvia":
# P(lluvia=True) = 0.2, P(lluvia=False) = 0.8.

cpd_mojado = TabularCPD(
    variable='mojado', variable_card=2,
    values=[
        [0.9, 0.1],  # P(mojado=True | lluvia)
        [0.1, 0.9]   # P(mojado=False | lluvia)
    ],
    evidence=['lluvia'],
    evidence_card=[2]
)
# Definimos la probabilidad condicional de "mojado" dado "lluvia":
# Si llueve: P(mojado=True) = 0.9, P(mojado=False) = 0.1.
# Si no llueve: P(mojado=True) = 0.1, P(mojado=False) = 0.9.

# Añadimos las CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_mojado)

# Verificamos que el modelo sea válido
assert modelo.check_model()
# Validamos que las CPDs sean consistentes con la estructura de la red.

# Usamos inferencia por eliminación de variables
inferencia = VariableElimination(modelo)
# Creamos un objeto de inferencia utilizando el método de eliminación de variables.

# Consultamos P(lluvia | mojado=True)
resultado = inferencia.query(variables=['lluvia'], evidence={'mojado': 0})
# Realizamos una consulta para calcular la probabilidad de "lluvia" dado que "mojado=True".

print("P(lluvia | mojado=True):")
print(resultado)
# Mostramos el resultado de la consulta.