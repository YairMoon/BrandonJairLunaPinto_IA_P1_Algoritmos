print("\n=== Sistema de decisiones de estudio ===")
# Estado actual ingresado por usuario
tengo_tarea = input("¿Tienes tarea? (si/no): ").lower() == 'si'
hay_internet = input("¿Hay internet? (si/no): ").lower() == 'si'

# Sistema de reglas para decidir qué hacer
if tengo_tarea and hay_internet:
    accion = "Estudio en línea"
elif tengo_tarea and not hay_internet:
    accion = "Estudio en físico"
elif not tengo_tarea:
    accion = "Descanso"

# Mostrar resultado
print(f"\nSituación -> Tarea: {tengo_tarea}, Internet: {hay_internet}")
print(f"Acción recomendada: {accion}")
# Ejemplo de uso:
# ¿Tienes tarea? (si/no): si
# ¿Hay internet? (si/no): no
# Output:
# Situación -> Tarea: True, Internet: False
# Acción recomendada: Estudio en físico
# --- IGNORE ---
