import random

# Distribuciones
P_lluvia = {True: 0.2, False: 0.8}
P_mojado = {
    True: {True: 0.9, False: 0.1},   # P(mojado | lluvia)
    False: {True: 0.1, False: 0.9}
}

# Muestreo directo: genera muestras sin evidencia
def muestreo_directo(n=1000):
    lluvia_true = 0
    for _ in range(n):
        lluvia = random.random() < P_lluvia[True]
        mojado = random.random() < P_mojado[lluvia][True]
        if lluvia:
            lluvia_true += 1
    return lluvia_true / n

# Muestreo por rechazo: solo cuenta muestras donde mojado = True
def muestreo_rechazo(n=10000):
    lluvia_true = 0
    muestras_validas = 0

    for _ in range(n):
        lluvia = random.random() < P_lluvia[True]
        mojado = random.random() < P_mojado[lluvia][True]

        # Rechazamos si mojado != True
        if mojado:
            muestras_validas += 1
            if lluvia:
                lluvia_true += 1

    if muestras_validas == 0:
        return None
    return lluvia_true / muestras_validas

# Ejecutamos ambos métodos
print(f"Muestreo directo (estimación de P(lluvia)): {muestreo_directo():.4f}")
print(f"Muestreo por rechazo (estimación de P(lluvia | mojado=True)): {muestreo_rechazo():.4f}")
# Resultado esperado: P(lluvia | mojado=True) ≈ 0.2