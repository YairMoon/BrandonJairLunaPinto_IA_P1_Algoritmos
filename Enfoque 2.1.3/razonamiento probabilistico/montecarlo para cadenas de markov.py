import random

# Distribuciones condicionales
P_lluvia = {True: 0.2, False: 0.8}
P_mojado = {
    True: {True: 0.9, False: 0.1},   # P(mojado | lluvia)
    False: {True: 0.1, False: 0.9}
}

# Gibbs Sampling para 2 variables: lluvia y mojado
def gibbs_sampling(evidence_mojado=True, steps=10000):
    # Inicializamos lluvia de forma aleatoria
    lluvia = random.choice([True, False])

    lluvia_true_count = 0

    for _ in range(steps):
        # Solo muestreamos la variable oculta: lluvia
        # P(lluvia | mojado) ∝ P(mojado | lluvia) * P(lluvia)
        p_true = P_mojado[True][evidence_mojado] * P_lluvia[True]
        p_false = P_mojado[False][evidence_mojado] * P_lluvia[False]

        total = p_true + p_false
        prob_lluvia = p_true / total

        lluvia = random.random() < prob_lluvia

        if lluvia:
            lluvia_true_count += 1

    return lluvia_true_count / steps

# Ejecutamos
estimacion = gibbs_sampling()
print(f"Gibbs Sampling: P(lluvia | mojado=True) ≈ {estimacion:.4f}")
 