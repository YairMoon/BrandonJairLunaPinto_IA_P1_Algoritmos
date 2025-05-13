import random
# Importamos la biblioteca random para generar valores aleatorios.

# Distribuciones
P_lluvia = {True: 0.2, False: 0.8}
# Probabilidad marginal de que llueva o no.

P_mojado = {
    True: {True: 0.9, False: 0.1},   # P(mojado | lluvia)
    False: {True: 0.1, False: 0.9}
}
# Probabilidad condicional de que algo esté mojado dado que llueva o no.

# Muestreo directo: genera muestras sin evidencia
def muestreo_directo(n=1000):
    """
    Realiza muestreo directo para estimar P(lluvia).
    
    :param n: Número de muestras a generar.
    :return: Estimación de P(lluvia).
    """
    lluvia_true = 0
    for _ in range(n):
        lluvia = random.random() < P_lluvia[True]
        # Generamos una muestra para "lluvia" basada en su probabilidad marginal.

        mojado = random.random() < P_mojado[lluvia][True]
        # Generamos una muestra para "mojado" basada en la probabilidad condicional P(mojado | lluvia).

        if lluvia:
            lluvia_true += 1
        # Contamos las veces que lluvia=True.

    return lluvia_true / n
    # Retornamos la proporción de veces que lluvia=True.

# Muestreo por rechazo: solo cuenta muestras donde mojado = True
def muestreo_rechazo(n=10000):
    """
    Realiza muestreo por rechazo para estimar P(lluvia | mojado=True).
    
    :param n: Número de muestras a generar.
    :return: Estimación de P(lluvia | mojado=True).
    """
    lluvia_true = 0
    muestras_validas = 0
    # Inicializamos contadores para lluvia=True y muestras válidas.

    for _ in range(n):
        lluvia = random.random() < P_lluvia[True]
        # Generamos una muestra para "lluvia".

        mojado = random.random() < P_mojado[lluvia][True]
        # Generamos una muestra para "mojado" basada en P(mojado | lluvia).

        # Rechazamos si mojado != True
        if mojado:
            muestras_validas += 1
            # Contamos la muestra como válida si mojado=True.

            if lluvia:
                lluvia_true += 1
            # Contamos las veces que lluvia=True en las muestras válidas.

    if muestras_validas == 0:
        return None
    # Si no hay muestras válidas, retornamos None para evitar división por cero.

    return lluvia_true / muestras_validas
    # Retornamos la proporción de veces que lluvia=True en las muestras válidas.

# Ejecutamos ambos métodos
print(f"Muestreo directo (estimación de P(lluvia)): {muestreo_directo():.4f}")
# Estimamos P(lluvia) usando muestreo directo.

print(f"Muestreo por rechazo (estimación de P(lluvia | mojado=True)): {muestreo_rechazo():.4f}")
# Estimamos P(lluvia | mojado=True) usando muestreo por rechazo.