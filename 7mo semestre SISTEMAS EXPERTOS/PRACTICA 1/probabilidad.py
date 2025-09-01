print("\n=== Probabilidad de lluvia ===")
# Ingresar datos históricos
dias_lluvia = int(input("Número de días lluviosos: "))
dias_total = int(input("Número total de días: "))

# Calcular probabilidad
prob_lluvia = dias_lluvia / dias_total

print(f"Probabilidad de lluvia hoy: {prob_lluvia*100:.2f}%")

# Decisión según probabilidad
if prob_lluvia > 0.3:
    print("Acción recomendada: Llevar paraguas")
else:
    print("Acción recomendada: No llevar paraguas")
# Ejemplo de uso:
# Número de días lluviosos: 45
# Número total de días: 150
# Output:
# Probabilidad de lluvia hoy: 30.00%
# Acción recomendada: No llevar paraguas