import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Parámetros del sistema
# -------------------------------

# Número de partículas
N = 1000

# Número de pasos de tiempo
T = 50

# Posición real inicial
x_real = 0.0

# Velocidad constante real
v_real = 1.0

# Ruido en el proceso (desviación estándar)
sigma_proceso = 1.0

# Ruido en la medición (desviación estándar)
sigma_medicion = 2.0

# -------------------------------
# Inicialización de partículas
# -------------------------------

# Cada partícula representa una posible posición del objeto
particulas = np.random.normal(0.0, 5.0, N)

# Pesos iniciales (uniformes)
pesos = np.ones(N) / N

# -------------------------------
# Simulación y estimación
# -------------------------------

# Almacenar resultados
pos_real = []
mediciones = []
estimaciones = []

for t in range(T):
    # Movimiento real con ruido
    x_real += v_real + np.random.normal(0, sigma_proceso)
    pos_real.append(x_real)

    # Medición con ruido
    z = x_real + np.random.normal(0, sigma_medicion)
    mediciones.append(z)

    # === PREDICCIÓN ===
    particulas += np.random.normal(v_real, sigma_proceso, N)

    # === ACTUALIZACIÓN (ponderar partículas según la observación) ===
    distancias = z - particulas
    pesos = (1.0 / (np.sqrt(2 * np.pi) * sigma_medicion)) * \
        np.exp(-0.5 * (distancias / sigma_medicion)**2)

    # Normalizar los pesos
    pesos += 1e-300  # evitar división por cero
    pesos /= np.sum(pesos)

    # === RESAMPLEO (remuestreo de partículas según sus pesos) ===
    indices = np.random.choice(N, size=N, replace=True, p=pesos)
    particulas = particulas[indices]
    pesos = np.ones(N) / N

    # Estimación del estado: promedio ponderado de las partículas
    x_est = np.mean(particulas)
    estimaciones.append(x_est)

# -------------------------------
# Gráfica de resultados
# -------------------------------

plt.plot(pos_real, label='Posición Real')
plt.plot(mediciones, label='Mediciones (ruido)', linestyle='dotted')
plt.plot(estimaciones, label='Estimación por Partículas', linestyle='--')
plt.legend()
plt.title('Filtrado de Partículas - Estimación de estado')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.grid(True)
plt.show()
# Este código simula un filtro de partículas para estimar la posición de un objeto en movimiento
# con ruido en el proceso y en la medición. Se inicializan partículas aleatorias y se actualizan