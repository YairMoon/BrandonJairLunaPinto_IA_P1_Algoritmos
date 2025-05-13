import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# -------------------------------
# Parámetros del sistema
# -------------------------------

# Número de partículas
N = 1000
# Definimos el número de partículas que representan posibles estados del sistema.

# Número de pasos de tiempo
T = 50
# Definimos el número de pasos de tiempo para la simulación.

# Posición real inicial
x_real = 0.0
# Posición inicial del objeto.

# Velocidad constante real
v_real = 1.0
# Velocidad constante del objeto.

# Ruido en el proceso (desviación estándar)
sigma_proceso = 1.0
# Define la incertidumbre en el modelo de movimiento.

# Ruido en la medición (desviación estándar)
sigma_medicion = 2.0
# Define la incertidumbre en las mediciones realizadas por los sensores.

# -------------------------------
# Inicialización de partículas
# -------------------------------

# Cada partícula representa una posible posición del objeto
particulas = np.random.normal(0.0, 5.0, N)
# Inicializamos las partículas con valores aleatorios alrededor de 0 con una desviación estándar de 5.

# Pesos iniciales (uniformes)
pesos = np.ones(N) / N
# Inicializamos los pesos de las partículas de manera uniforme.

# -------------------------------
# Simulación y estimación
# -------------------------------

# Almacenar resultados
pos_real = []       # Posiciones reales del objeto.
mediciones = []     # Mediciones realizadas con ruido.
estimaciones = []   # Estimaciones realizadas por el filtro de partículas.

for t in range(T):
    # Movimiento real con ruido
    x_real += v_real + np.random.normal(0, sigma_proceso)
    # Actualizamos la posición real con ruido del proceso.
    pos_real.append(x_real)

    # Medición con ruido
    z = x_real + np.random.normal(0, sigma_medicion)
    # Generamos una medición ruidosa basada en la posición real.
    mediciones.append(z)

    # === PREDICCIÓN ===
    particulas += np.random.normal(v_real, sigma_proceso, N)
    # Actualizamos las partículas añadiendo ruido del proceso.

    # === ACTUALIZACIÓN (ponderar partículas según la observación) ===
    distancias = z - particulas
    # Calculamos las distancias entre las partículas y la medición.

    pesos = (1.0 / (np.sqrt(2 * np.pi) * sigma_medicion)) * \
        np.exp(-0.5 * (distancias / sigma_medicion)**2)
    # Calculamos los pesos de las partículas basados en la probabilidad gaussiana.

    # Normalizar los pesos
    pesos += 1e-300  # evitar división por cero
    pesos /= np.sum(pesos)
    # Normalizamos los pesos para que sumen 1.

    # === RESAMPLEO (remuestreo de partículas según sus pesos) ===
    indices = np.random.choice(N, size=N, replace=True, p=pesos)
    # Seleccionamos partículas basándonos en sus pesos.

    particulas = particulas[indices]
    # Actualizamos las partículas con las seleccionadas.

    pesos = np.ones(N) / N
    # Reiniciamos los pesos de las partículas de manera uniforme.

    # Estimación del estado: promedio ponderado de las partículas
    x_est = np.mean(particulas)
    # Calculamos la estimación como el promedio de las partículas.

    estimaciones.append(x_est)
    # Guardamos la estimación actual.

# -------------------------------
# Gráfica de resultados
# -------------------------------

plt.plot(pos_real, label='Posición Real')
# Graficamos la posición real del objeto.

plt.plot(mediciones, label='Mediciones (ruido)', linestyle='dotted')
# Graficamos las mediciones realizadas con ruido.

plt.plot(estimaciones, label='Estimación por Partículas', linestyle='--')
# Graficamos las estimaciones realizadas por el filtro de partículas.

plt.legend()
plt.title('Filtrado de Partículas - Estimación de estado')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.grid(True)
plt.show()
# Mostramos la gráfica con los resultados.