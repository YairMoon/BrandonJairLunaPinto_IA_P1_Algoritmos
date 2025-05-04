import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Parámetros del sistema
# -------------------------------

# Número de pasos de tiempo
n = 50

# Número de estados posibles
n_estados = 2

# Probabilidades de transición entre estados
transiciones = np.array([[0.7, 0.3],
                         [0.4, 0.6]])

# Probabilidades de observación
observaciones = np.array([[0.9, 0.1],
                          [0.2, 0.8]])

# Probabilidades iniciales
inicio = np.array([0.5, 0.5])

# -------------------------------
# Datos de observación (secuencia de observaciones)
# -------------------------------

# Simulación de una secuencia de observaciones
sec_observaciones = np.random.choice([0, 1], size=n, p=[0.5, 0.5])

# -------------------------------
# Algoritmo hacia adelante
# -------------------------------

# Inicialización de las probabilidades hacia adelante
alpha = np.zeros((n, n_estados))

# Paso inicial
alpha[0] = inicio * observaciones[:, sec_observaciones[0]]

# Paso hacia adelante
for t in range(1, n):
    for j in range(n_estados):
        alpha[t, j] = np.sum(alpha[t-1] * transiciones[:, j]) * observaciones[j, sec_observaciones[t]]

# -------------------------------
# Algoritmo hacia atrás
# -------------------------------

# Inicialización de las probabilidades hacia atrás
beta = np.zeros((n, n_estados))

# Paso inicial (beta en el último tiempo)
beta[-1] = 1

# Paso hacia atrás
for t in range(n-2, -1, -1):
    for i in range(n_estados):
        beta[t, i] = np.sum(transiciones[i, :] * observaciones[:, sec_observaciones[t+1]] * beta[t+1])

# -------------------------------
# Cálculo de las probabilidades posteriores
# -------------------------------

# Probabilidades posteriores = alpha * beta
posteriores = alpha * beta

# Normalizar las probabilidades
posteriores /= np.sum(posteriores, axis=1, keepdims=True)

# -------------------------------
# Resultados
# -------------------------------

# Mostrar las probabilidades posteriores de cada estado a lo largo del tiempo
plt.plot(posteriores[:, 0], label="Estado 0", linestyle='--')
plt.plot(posteriores[:, 1], label="Estado 1", linestyle=':')
plt.title('Algoritmo Hacia Adelante-Atrás')
plt.xlabel('Tiempo')
plt.ylabel('Probabilidad Posterior')
plt.legend()
plt.grid(True)
plt.show()
