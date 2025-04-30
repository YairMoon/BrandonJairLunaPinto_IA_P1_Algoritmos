# Distribución de Probabilidad
# Representa todas las probabilidades de los valores posibles de una variable aleatoria

# Ejemplo: distribución de probabilidad de un dado justo
from collections import Counter

# Distribución teórica (todos los valores son equiprobables)
dado_justo = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

# Función para validar si es una distribución válida
def es_distribucion_valida(distribucion):
    return abs(sum(distribucion.values()) - 1.0) < 1e-6

print("Distribución teórica del dado justo:")
for cara, prob in dado_justo.items():
    print(f"  Cara {cara}: {prob:.2f}")

print("\n¿Es una distribución válida?", es_distribucion_valida(dado_justo))

# Simulamos lanzamientos para obtener una distribución empírica
import random
lanzamientos = [random.randint(1, 6) for _ in range(1000)]
conteo = Counter(lanzamientos)

distribucion_empirica = {cara: conteo[cara]/1000 for cara in range(1, 7)}

print("\nDistribución empírica tras 1000 lanzamientos:")
for cara, prob in distribucion_empirica.items():
    print(f"  Cara {cara}: {prob:.2f}")
