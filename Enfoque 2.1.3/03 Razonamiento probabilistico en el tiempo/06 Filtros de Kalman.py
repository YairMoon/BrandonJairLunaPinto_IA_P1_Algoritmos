import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# -------------------------------
# Parámetros del sistema
# -------------------------------

# Número de pasos de tiempo
n = 50
# Definimos el número de pasos de tiempo para la simulación.

# Posición real inicial
x_real = 0.0
# Posición inicial del objeto.

# Velocidad constante del objeto
v_real = 1.0
# Velocidad constante del objeto.

# Varianza del ruido del proceso (movimiento)
var_proceso = 1e-5
# Define la incertidumbre en el modelo de movimiento.

# Varianza del ruido de la medición (sensores)
var_medicion = 0.1**2
# Define la incertidumbre en las mediciones realizadas por los sensores.

# -------------------------------
# Inicialización del filtro de Kalman
# -------------------------------

# Estimación inicial de la posición
x_est = 0.0
# Posición estimada inicial.

# Incertidumbre inicial
P = 1.0
# Incertidumbre inicial en la estimación.

# Ganancia del filtro de Kalman (se actualizará)
K = 0.0
# Inicializamos la ganancia de Kalman.

# Matriz de covarianza del proceso (Q)
Q = var_proceso
# Incertidumbre en el modelo de movimiento.

# Varianza del ruido de medición (R)
R = var_medicion
# Incertidumbre en las mediciones.

# Matriz de observación (H)
H = 1.0
# Relación entre el estado y la medición.

# Matriz de transición (A)
A = 1.0
# Relación entre el estado actual y el siguiente.

# -------------------------------
# Simulación y estimación
# -------------------------------

# Almacenamiento de resultados para graficar
pos_real = []       # Posiciones reales del objeto.
mediciones = []     # Mediciones realizadas con ruido.
estimaciones = []   # Estimaciones realizadas por el filtro de Kalman.

for t in range(n):
    # Movimiento real del objeto
    x_real += v_real + np.random.normal(0, np.sqrt(Q))
    # Actualizamos la posición real con ruido del proceso.
    pos_real.append(x_real)

    # Medición con ruido
    z = x_real + np.random.normal(0, np.sqrt(R))
    # Generamos una medición ruidosa basada en la posición real.
    mediciones.append(z)

    # === PREDICCIÓN ===
    x_pred = A * x_est
    P_pred = A * P * A + Q
    # Calculamos la posición y la incertidumbre predichas.

    # === ACTUALIZACIÓN ===
    K = P_pred * H / (H * P_pred * H + R)
    # Calculamos la ganancia de Kalman para ajustar la estimación.

    x_est = x_pred + K * (z - H * x_pred)
    # Actualizamos la estimación basada en la medición.

    P = (1 - K * H) * P_pred
    # Actualizamos la incertidumbre de la estimación.

    estimaciones.append(x_est)
    # Guardamos la estimación actual.

# -------------------------------
# Gráfica de resultados
# -------------------------------

plt.plot(pos_real, label='Posición Real')
# Graficamos la posición real del objeto.

plt.plot(mediciones, label='Mediciones (ruido)', linestyle='dotted')
# Graficamos las mediciones realizadas con ruido.

plt.plot(estimaciones, label='Estimación Kalman', linestyle='--')
# Graficamos las estimaciones realizadas por el filtro de Kalman.

plt.legend()
plt.title('Filtro de Kalman 1D - Seguimiento de posición')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.grid(True)
plt.show()
# Mostramos la gráfica con los resultados.