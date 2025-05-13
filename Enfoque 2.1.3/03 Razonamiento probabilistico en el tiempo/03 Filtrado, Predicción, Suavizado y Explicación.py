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
# Inicialización de los filtros
# -------------------------------

# Estimación inicial de la posición
x_est = 0.0
# Posición estimada inicial.

# Incertidumbre inicial
P = 1.0
# Incertidumbre inicial en la estimación.

# Matriz de transición (A)
A = 1.0
# Relación entre el estado actual y el siguiente.

# Matriz de observación (H)
H = 1.0
# Relación entre el estado y la medición.

# Varianza del ruido de medición (R)
R = var_medicion
# Incertidumbre en las mediciones.

# Varianza del ruido del proceso (Q)
Q = var_proceso
# Incertidumbre en el modelo de movimiento.

# -------------------------------
# Simulación y estimación
# -------------------------------

# Almacenamiento de resultados
pos_real = []       # Posiciones reales del objeto.
mediciones = []     # Mediciones realizadas con ruido.
estimaciones = []   # Estimaciones del filtro de Kalman.
predicciones = []   # Predicciones realizadas por el modelo.
suavizados = []     # Estimaciones suavizadas.

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
    # Predicción de la posición y la incertidumbre
    x_pred = A * x_est
    P_pred = A * P * A + Q
    # Calculamos la posición y la incertidumbre predichas.
    predicciones.append(x_pred)

    # === ACTUALIZACIÓN ===
    # Calcular la ganancia de Kalman
    K = P_pred * H / (H * P_pred * H + R)
    # Calculamos la ganancia de Kalman para ajustar la estimación.

    # Estimación corregida
    x_est = x_pred + K * (z - H * x_pred)
    # Actualizamos la estimación basada en la medición.

    # Actualización de la incertidumbre
    P = (1 - K * H) * P_pred
    # Actualizamos la incertidumbre de la estimación.

    estimaciones.append(x_est)

    # === SUAVIZADO ===
    # Estimación suavizada (considerando las mediciones futuras)
    suavizado = (x_est + x_pred) / 2
    # Calculamos una estimación suavizada combinando la estimación actual y la predicción.
    suavizados.append(suavizado)

# -------------------------------
# Gráfica de resultados
# -------------------------------

plt.plot(pos_real, label='Posición Real')
# Graficamos la posición real del objeto.

plt.plot(mediciones, label='Mediciones (ruido)', linestyle='dotted')
# Graficamos las mediciones realizadas con ruido.

plt.plot(estimaciones, label='Estimación de Kalman', linestyle='--')
# Graficamos las estimaciones realizadas por el filtro de Kalman.

plt.plot(predicciones, label='Predicciones', linestyle='-.')
# Graficamos las predicciones realizadas por el modelo.

plt.plot(suavizados, label='Estimación Suavizada', linestyle=':')
# Graficamos las estimaciones suavizadas.

plt.legend()
plt.title('Filtrado, Predicción, Suavizado y Explicación')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.grid(True)
plt.show()
# Mostramos la gráfica con los resultados.