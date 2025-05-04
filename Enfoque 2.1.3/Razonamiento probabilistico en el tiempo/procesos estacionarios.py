import numpy as np
import matplotlib.pyplot as plt

# Generamos un proceso estacionario gaussiano
def proceso_estacionario_gaussiano(n=1000, media=0, varianza=1):
    return np.random.normal(media, np.sqrt(varianza), n)

# Graficamos
datos = proceso_estacionario_gaussiano()
plt.plot(datos)
plt.title("Proceso Estacionario Gaussiano")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()
