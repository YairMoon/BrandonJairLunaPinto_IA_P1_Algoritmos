# Distribución de Probabilidad
# Representa todas las probabilidades de los valores posibles de una variable aleatoria

# Ejemplo: distribución de probabilidad de un dado justo
from collections import Counter  # Importamos Counter para contar frecuencias en simulaciones.

# Distribución teórica (todos los valores son equiprobables)
dado_justo = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}
# Representamos un dado justo donde cada cara tiene la misma probabilidad de 1/6.

# Función para validar si es una distribución válida
def es_distribucion_valida(distribucion): # Verifica si la suma de las probabilidades es 1.
    return abs(sum(distribucion.values()) - 1.0) < 1e-6 # Comprobamos si la suma de las probabilidades es 1 (con tolerancia a errores de redondeo).
# Verificamos que la suma de las probabilidades sea igual a 1 (o muy cercana por redondeo).

print("Distribución teórica del dado justo:") # Mostramos la distribución teórica del dado justo.
for cara, prob in dado_justo.items(): # Iteramos sobre cada cara del dado y su probabilidad.
    print(f"  Cara {cara}: {prob:.2f}") # Mostramos la probabilidad de cada cara del dado justo con 2 decimales.
# Mostramos la distribución teórica del dado justo.

print("\n¿Es una distribución válida?", es_distribucion_valida(dado_justo)) # Verificamos si la distribución teórica es válida.
# Validamos si la distribución teórica es válida.

# Simulamos lanzamientos para obtener una distribución empírica
import random  # Importamos random para generar números aleatorios.
lanzamientos = [random.randint(1, 6) for _ in range(1000)] # Generamos 1000 lanzamientos aleatorios de un dado justo (números entre 1 y 6).
# Simulamos 1000 lanzamientos de un dado justo.

conteo = Counter(lanzamientos) #
# Contamos la frecuencia de cada cara en los lanzamientos.

distribucion_empirica = {cara: conteo[cara]/1000 for cara in range(1, 7)} # Creamos un diccionario con la distribución empírica, dividiendo la frecuencia de cada cara por el total de lanzamientos (1000).
# Calculamos la distribución empírica dividiendo las frecuencias por el número total de lanzamientos.

print("\nDistribución empírica tras 1000 lanzamientos:") # Mostramos la distribución empírica obtenida tras los lanzamientos.
for cara, prob in distribucion_empirica.items(): # Iteramos sobre cada cara del dado y su probabilidad empírica.
    print(f"  Cara {cara}: {prob:.2f}") #
# Mostramos la distribución empírica obtenida tras los lanzamientos.