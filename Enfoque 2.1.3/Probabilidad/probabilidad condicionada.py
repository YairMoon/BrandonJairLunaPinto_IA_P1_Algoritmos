# Probabilidad Condicionada y Normalización
# P(A|B) = P(A ∩ B) / P(B)

# Supongamos:
# A = "Tiene fiebre"
# B = "Está enfermo"
# Sabemos que:
# P(A ∩ B) = 0.12 (la persona tiene fiebre y está enferma)
# P(B) = 0.2 (probabilidad de estar enfermo)

# Calculamos P(A|B):
P_A_interseccion_B = 0.12
P_B = 0.2

# Verificamos que P(B) no sea 0 para evitar división por cero
if P_B != 0:
    P_A_dado_B = P_A_interseccion_B / P_B
else:
    P_A_dado_B = None

# Imprimimos el resultado
print("Tener fiebre | Estar enfermo:", P_A_dado_B)

# Normalización: cuando se tienen probabilidades no normalizadas y se quieren ajustar
# Supongamos probabilidades no normalizadas de un sensor
valores_no_normalizados = {
    'Correcto': 0.4,
    'Incorrecto': 0.1
}

# Normalizamos dividiendo por la suma total
suma = sum(valores_no_normalizados.values())
valores_normalizados = {k: v / suma for k, v in valores_no_normalizados.items()}

print("\nValores normalizados:")
for estado, prob in valores_normalizados.items():
    print(f"  {estado}: {prob:.2f}")
