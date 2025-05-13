# Probabilidad a Priori
# La probabilidad a priori es el conocimiento inicial sobre un evento antes de considerar nueva evidencia

# Ejemplo: un dado cargado (no justo)
# La probabilidad a priori para cada cara es desigual y refleja nuestro conocimiento inicial
probabilidades_priori = {
    1: 0.05,  # Cara 1 tiene una probabilidad del 5%.
    2: 0.10,  # Cara 2 tiene una probabilidad del 10%.
    3: 0.15,  # Cara 3 tiene una probabilidad del 15%.
    4: 0.20,  # Cara 4 tiene una probabilidad del 20%.
    5: 0.25,  # Cara 5 tiene una probabilidad del 25%.
    6: 0.25   # Cara 6 tiene una probabilidad del 25%.
}

# Función para verificar validez de la distribución
def es_distribucion_valida(distribucion): # Verifica si la suma de las probabilidades es 1.
    # Comprobamos si la suma de las probabilidades es 1 (con tolerancia a errores de redondeo).
    return abs(sum(distribucion.values()) - 1.0) < 1e-6 
# Verificamos que la suma de las probabilidades sea igual a 1 (o muy cercana por redondeo).

# Mostrar probabilidades a priori
print("Probabilidad a Priori para cada cara del dado cargado:") # Mostramos la probabilidad a priori para cada cara del dado cargado.
for cara, prob in probabilidades_priori.items(): # Iteramos sobre cada cara del dado y su probabilidad asociada.
    print(f"  Cara {cara}: {prob:.2f}") # Mostramos la probabilidad de cada cara del dado cargado con 2 decimales.
# Mostramos las probabilidades a priori para cada cara del dado cargado.

# Validar la distribución
print("\n¿Es una distribución válida?", es_distribucion_valida(probabilidades_priori)) ## Verificamos si la distribución de probabilidad a priori es válida.
# La suma de las probabilidades debe ser 1 (o muy cercana por redondeo).