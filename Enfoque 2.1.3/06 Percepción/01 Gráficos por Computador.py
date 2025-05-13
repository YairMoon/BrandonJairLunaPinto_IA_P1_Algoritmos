import matplotlib.pyplot as plt  # Importamos Matplotlib para crear gráficos.
import numpy as np  # Importamos NumPy para manejar operaciones matemáticas y matrices.

# Generar una imagen simple con gráficos por computador
def graficos_por_computador():
    # Crear un conjunto de puntos
    x = np.linspace(0, 10, 100)  # Generamos 100 puntos equidistantes entre 0 y 10.
    y = np.sin(x)  # Calculamos el seno de cada punto en `x`.

    # Crear una gráfica
    plt.plot(x, y, label="Seno")  # Graficamos `y` contra `x` y añadimos una etiqueta "Seno".
    plt.title("Gráficos por Computador")  # Título del gráfico.
    plt.xlabel("Eje X")  # Etiqueta para el eje X.
    plt.ylabel("Eje Y")  # Etiqueta para el eje Y.
    plt.legend()  # Mostramos la leyenda para identificar la curva.
    plt.grid(True)  # Añadimos una cuadrícula al gráfico.
    plt.show()  # Mostramos el gráfico en una ventana.

# Ejecutar la función
graficos_por_computador()
# Este código genera una gráfica simple utilizando Matplotlib, mostrando la función seno en el rango de 0 a 10.
# La función `graficos_por_computador` crea un conjunto de puntos y los grafica, mostrando cómo se pueden utilizar gráficos por computador para visualizar datos.