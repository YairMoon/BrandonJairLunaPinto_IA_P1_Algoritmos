import random
# Importamos la biblioteca random para generar valores aleatorios.

# Distribuciones condicionales
P_lluvia = {True: 0.2, False: 0.8}
# Probabilidad marginal de que llueva o no.

P_mojado = {
    True: {True: 0.9, False: 0.1},   # P(mojado | lluvia)
    False: {True: 0.1, False: 0.9}
}
# Probabilidad condicional de que algo esté mojado dado que llueva o no.

# Gibbs Sampling para 2 variables: lluvia y mojado
def gibbs_sampling(evidence_mojado=True, steps=10000):
    """
    Realiza Gibbs Sampling para estimar P(lluvia | mojado=True).
    
    :param evidence_mojado: Evidencia de que algo está mojado (por defecto True).
    :param steps: Número de iteraciones para el muestreo.
    :return: Estimación de P(lluvia | mojado=True).
    """
    # Inicializamos lluvia de forma aleatoria
    lluvia = random.choice([True, False])
    # Elegimos un valor inicial aleatorio para la variable "lluvia".

    lluvia_true_count = 0
    # Contador para las veces que lluvia=True.

    for _ in range(steps):
        # Solo muestreamos la variable oculta: lluvia
        # P(lluvia | mojado) ∝ P(mojado | lluvia) * P(lluvia)
        p_true = P_mojado[True][evidence_mojado] * P_lluvia[True]
        p_false = P_mojado[False][evidence_mojado] * P_lluvia[False]
        # Calculamos las probabilidades no normalizadas para lluvia=True y lluvia=False.

        total = p_true + p_false
        prob_lluvia = p_true / total
        # Normalizamos las probabilidades para obtener P(lluvia | mojado).

        lluvia = random.random() < prob_lluvia
        # Actualizamos el valor de "lluvia" basado en la probabilidad calculada.

        if lluvia:
            lluvia_true_count += 1
        # Incrementamos el contador si lluvia=True.

    return lluvia_true_count / steps
    # Retornamos la estimación de P(lluvia | mojado=True) como la proporción de veces que lluvia=True.

# Ejecutamos
estimacion = gibbs_sampling()
print(f"Gibbs Sampling: P(lluvia | mojado=True) ≈ {estimacion:.4f}")
# Ejecutamos el muestreo de Gibbs y mostramos la estimación de P(lluvia | mojado=True).