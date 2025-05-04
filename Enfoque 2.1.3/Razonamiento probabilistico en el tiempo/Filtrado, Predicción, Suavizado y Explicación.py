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
# Inicialización de los filtros
# -------------------------------

# Estimación inicial de la posición
x_est = 0.0

# Incertidumbre inicial
P = 1.0

# Matriz de transición (A)
A = 1.0

# Matriz de observación (H)
H = 1.0

# Varianza del ruido de medición (R)
R = var_medicion

# Varianza del ruido del proceso (Q)
Q = var_proceso

# -------------------------------
# Simulación y estimación
# -------------------------------

# Almacenamiento de resultados
pos_real = []
mediciones = []
estimaciones = []
predicciones = []
suavizados = []

for t in range(n):
    # Movimiento real del objeto
    x_real += v_real + np.random.normal(0, np.sqrt(Q))
    pos_real.append(x_real)

    # Medición con ruido
    z = x_real + np.random.normal(0, np.sqrt(R))
    mediciones.append(z)

    # === PREDICCIÓN ===
    # Predicción de la posición y la incertidumbre
    x_pred = A * x_est
    P_pred = A * P * A + Q
    predicciones.append(x_pred)

    # === ACTUALIZACIÓN ===
    # Calcular la ganancia de Kalman
    K = P_pred * H / (H * P_pred * H + R)
    # Estimación corregida
    x_est = x_pred + K * (z - H * x_pred)
    # Actualización de la incertidumbre
    P = (1 - K * H) * P_pred

    estimaciones.append(x_est)

    # === SUAVIZADO ===
    # Estimación suavizada (considerando las mediciones futuras)
    suavizado = (x_est + x_pred) / 2
    suavizados.append(suavizado)

# -------------------------------
# Gráfica de resultados
# -------------------------------

plt.plot(pos_real, label='Posición Real')
plt.plot(mediciones, label='Mediciones (ruido)', linestyle='dotted')
plt.plot(estimaciones, label='Estimación de Kalman', linestyle='--')
plt.plot(predicciones, label='Predicciones', linestyle='-.')
plt.plot(suavizados, label='Estimación Suavizada', linestyle=':')
plt.legend()
plt.title('Filtrado, Predicción, Suavizado y Explicación')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.grid(True)
plt.show()
