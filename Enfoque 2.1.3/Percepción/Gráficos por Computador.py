import matplotlib.pyplot as plt
import numpy as np

# Generar una imagen simple con gráficos por computador
def graficos_por_computador():
    # Crear un conjunto de puntos
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Crear una gráfica
    plt.plot(x, y, label="Seno")
    plt.title("Gráficos por Computador")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecutar la función
graficos_por_computador()
# Este código genera una gráfica simple utilizando Matplotlib, mostrando la función seno en el rango de 0 a 10.
# La función `graficos_por_computador` crea un conjunto de puntos y los grafica, mostrando cómo se pueden utilizar gráficos por computador para visualizar datos.