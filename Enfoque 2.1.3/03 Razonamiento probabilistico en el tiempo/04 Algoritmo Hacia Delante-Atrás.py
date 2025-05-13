import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# -------------------------------
# Parámetros del sistema
# -------------------------------

# Número de pasos de tiempo
n = 50
# Definimos el número de pasos de tiempo para la simulación.

# Número de estados posibles
n_estados = 2
# Definimos el número de estados posibles en el sistema.

# Probabilidades de transición entre estados
transiciones = np.array([[0.7, 0.3],
                         [0.4, 0.6]])
# Matriz de transición que define las probabilidades de pasar de un estado a otro.

# Probabilidades de observación
observaciones = np.array([[0.9, 0.1],
                          [0.2, 0.8]])
# Matriz de observación que define las probabilidades de observar ciertos valores en cada estado.

# Probabilidades iniciales
inicio = np.array([0.5, 0.5])
# Probabilidades iniciales de estar en cada estado.

# -------------------------------
# Datos de observación (secuencia de observaciones)
# -------------------------------

# Simulación de una secuencia de observaciones
sec_observaciones = np.random.choice([0, 1], size=n, p=[0.5, 0.5])
# Generamos una secuencia aleatoria de observaciones con probabilidades iguales para 0 y 1.

# -------------------------------
# Algoritmo hacia adelante
# -------------------------------

# Inicialización de las probabilidades hacia adelante
alpha = np.zeros((n, n_estados))
# Creamos una matriz para almacenar las probabilidades hacia adelante.

# Paso inicial
alpha[0] = inicio * observaciones[:, sec_observaciones[0]]
# Calculamos las probabilidades iniciales multiplicando las probabilidades iniciales por las probabilidades de observación.

# Paso hacia adelante
for t in range(1, n):
    for j in range(n_estados):
        alpha[t, j] = np.sum(alpha[t-1] * transiciones[:, j]) * observaciones[j, sec_observaciones[t]]
# Iteramos sobre el tiempo y los estados para calcular las probabilidades hacia adelante.

# -------------------------------
# Algoritmo hacia atrás
# -------------------------------

# Inicialización de las probabilidades hacia atrás
beta = np.zeros((n, n_estados))
# Creamos una matriz para almacenar las probabilidades hacia atrás.

# Paso inicial (beta en el último tiempo)
beta[-1] = 1
# Inicializamos las probabilidades hacia atrás en 1 para el último paso de tiempo.

# Paso hacia atrás
for t in range(n-2, -1, -1):
    for i in range(n_estados):
        beta[t, i] = np.sum(transiciones[i, :] * observaciones[:, sec_observaciones[t+1]] * beta[t+1])
# Iteramos hacia atrás en el tiempo para calcular las probabilidades hacia atrás.

# -------------------------------
# Cálculo de las probabilidades posteriores
# -------------------------------

# Probabilidades posteriores = alpha * beta
posteriores = alpha * beta
# Calculamos las probabilidades posteriores multiplicando las probabilidades hacia adelante y hacia atrás.

# Normalizar las probabilidades
posteriores /= np.sum(posteriores, axis=1, keepdims=True)
# Normalizamos las probabilidades para que sumen 1 en cada paso de tiempo.

# -------------------------------
# Resultados
# -------------------------------

# Mostrar las probabilidades posteriores de cada estado a lo largo del tiempo
plt.plot(posteriores[:, 0], label="Estado 0", linestyle='--') 
plt.plot(posteriores[:, 1], label="Estado 1", linestyle=':') 
# Graficamos las probabilidades posteriores para cada estado.

plt.title('Algoritmo Hacia Adelante-Atrás')
plt.xlabel('Tiempo')
plt.ylabel('Probabilidad Posterior')
plt.legend()
plt.grid(True)
plt.show()
# Mostramos la gráfica de las probabilidades posteriores a lo largo del tiempo.