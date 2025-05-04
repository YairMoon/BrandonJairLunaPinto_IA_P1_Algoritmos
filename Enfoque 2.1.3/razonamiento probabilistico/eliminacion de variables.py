from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos una red bayesiana: lluvia → mojado
modelo = BayesianNetwork([
    ('lluvia', 'mojado')
])

# Definimos las CPDs (tablas de probabilidad)
cpd_lluvia = TabularCPD(variable='lluvia', variable_card=2, values=[[0.2], [0.8]])

cpd_mojado = TabularCPD(
    variable='mojado', variable_card=2,
    values=[
        [0.9, 0.1],  # P(mojado=True | lluvia)
        [0.1, 0.9]   # P(mojado=False | lluvia)
    ],
    evidence=['lluvia'],
    evidence_card=[2]
)

# Añadimos las CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_mojado)

# Verificamos que el modelo sea válido
assert modelo.check_model()

# Usamos inferencia por eliminación de variables
inferencia = VariableElimination(modelo)

# Consultamos P(lluvia | mojado=True)
resultado = inferencia.query(variables=['lluvia'], evidence={'mojado': 0})

print("P(lluvia | mojado=True):")
print(resultado)
