import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# Generamos un proceso estacionario gaussiano
def proceso_estacionario_gaussiano(n=1000, media=0, varianza=1):
    """
    Genera un proceso estacionario gaussiano.

    :param n: Número de muestras a generar.
    :param media: Media del proceso.
    :param varianza: Varianza del proceso.
    :return: Un arreglo de valores generados.
    """
    return np.random.normal(media, np.sqrt(varianza), n)
    # Generamos valores aleatorios siguiendo una distribución normal con la media y varianza dadas.

# Graficamos
datos = proceso_estacionario_gaussiano()
# Generamos un conjunto de datos del proceso estacionario gaussiano con los valores por defecto.

plt.plot(datos)
# Graficamos los datos generados.

plt.title("Proceso Estacionario Gaussiano")
# Añadimos un título a la gráfica.

plt.xlabel("Tiempo")
# Etiquetamos el eje X como "Tiempo".

plt.ylabel("Valor")
# Etiquetamos el eje Y como "Valor".

plt.grid(True)
# Añadimos una cuadrícula para facilitar la visualización.

plt.show()
# Mostramos la gráfica.