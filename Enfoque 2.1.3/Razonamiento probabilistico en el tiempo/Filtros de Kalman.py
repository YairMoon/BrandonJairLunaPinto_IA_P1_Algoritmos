import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Parámetros del sistema
# -------------------------------

# Número de pasos de tiempo
n = 50

# Posición real inicial
x_real = 0.0

# Velocidad constante del objeto
v_real = 1.0

# Varianza del ruido del proceso (movimiento)
var_proceso = 1e-5

# Varianza del ruido de la medición (sensores)
var_medicion = 0.1**2

# -------------------------------
# Inicialización del filtro de Kalman
# -------------------------------

# Estimación inicial de la posición
x_est = 0.0

# Incertidumbre inicial
P = 1.0

# Ganancia del filtro de Kalman (se actualizará)
K = 0.0

# Matriz de covarianza del proceso (Q)
Q = var_proceso

# Varianza del ruido de medición (R)
R = var_medicion

# Matriz de observación (H)
H = 1.0

# Matriz de transición (A)
A = 1.0

# -------------------------------
# Simulación y estimación
# -------------------------------

# Almacenamiento de resultados para graficar
pos_real = []
mediciones = []
estimaciones = []

for t in range(n):
    # Movimiento real del objeto
    x_real += v_real + np.random.normal(0, np.sqrt(Q))
    pos_real.append(x_real)

    # Medición con ruido
    z = x_real + np.random.normal(0, np.sqrt(R))
    mediciones.append(z)

    # === PREDICCIÓN ===
    x_pred = A * x_est
    P_pred = A * P * A + Q

    # === ACTUALIZACIÓN ===
    K = P_pred * H / (H * P_pred * H + R)       # Ganancia de Kalman
    x_est = x_pred + K * (z - H * x_pred)       # Corrección con la medición
    P = (1 - K * H) * P_pred                    # Nueva incertidumbre

    estimaciones.append(x_est)

# -------------------------------
# Gráfica de resultados
# -------------------------------

plt.plot(pos_real, label='Posición Real')
plt.plot(mediciones, label='Mediciones (ruido)', linestyle='dotted')
plt.plot(estimaciones, label='Estimación Kalman', linestyle='--')
plt.legend()
plt.title('Filtro de Kalman 1D - Seguimiento de posición')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.grid(True)
plt.show()
