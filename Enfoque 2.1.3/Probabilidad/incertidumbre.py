# Incertidumbre en probabilidad
# Representamos la incertidumbre mediante una distribución de probabilidad sobre posibles estados

# Supongamos un sensor de clima que puede fallar. El clima real puede ser 'Soleado', 'Lluvioso', o 'Nublado'
# La incertidumbre se representa con probabilidades asignadas a cada estado

# Creamos una distribución de probabilidad
probabilidad_clima = {
    'Soleado': 0.6,   # 60% de probabilidad de estar soleado
    'Lluvioso': 0.3,  # 30% de probabilidad de lluvia
    'Nublado': 0.1    # 10% de probabilidad de nublado
}

# Función para verificar si la distribución es válida
# (la suma debe ser igual a 1, o muy cercana por redondeo)
def es_distribucion_valida(distribucion):
    return abs(sum(distribucion.values()) - 1.0) < 1e-6

# Imprimir los valores y verificar validez
print("Distribución de probabilidad del clima:")
for estado, prob in probabilidad_clima.items():
    print(f"  {estado}: {prob}")

print("\n¿Es una distribución válida?", es_distribucion_valida(probabilidad_clima))
