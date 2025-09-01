print("=== CSP optimizado: Presupuesto semanal ===")

# Pedir presupuesto total y límites
presupuesto_total = int(input("Ingresa tu presupuesto total para la semana: "))
min_comida = int(input("Gasto mínimo en comida: "))
min_transporte = int(input("Gasto mínimo en transporte: "))
max_ocio = int(input("Gasto máximo en ocio: "))

# Variables y dominios con pasos mayores para reducir combinaciones
variables = ['comida', 'transporte', 'ocio']
dominios = {
    'comida': list(range(min_comida, presupuesto_total + 1, 10)),       # paso 10
    'transporte': list(range(min_transporte, presupuesto_total + 1, 10)),# paso 10
    'ocio': list(range(0, max_ocio + 1, 5))                               # paso 5
}

# Función de restricciones
def restricciones(asignacion):
    if 'comida' in asignacion and asignacion['comida'] < min_comida:
        return False
    if 'transporte' in asignacion and asignacion['transporte'] < min_transporte:
        return False
    if 'ocio' in asignacion and asignacion['ocio'] > max_ocio:
        return False
    if sum(asignacion.values()) > presupuesto_total:
        return False
    return True

# Backtracking rápido: busca todas las soluciones
def backtracking_todas(asignacion={}, soluciones=[]):
    if len(asignacion) == len(variables):
        soluciones.append(asignacion.copy())
        return
    var = next(v for v in variables if v not in asignacion)
    for valor in dominios[var]:
        asignacion[var] = valor
        if restricciones(asignacion):
            backtracking_todas(asignacion, soluciones)
        asignacion.pop(var)
    return soluciones

# Ejecutar búsqueda
soluciones = backtracking_todas()
if soluciones:
    print(f"\nSe encontraron {len(soluciones)} soluciones posibles:")
    for i, sol in enumerate(soluciones, 1):
        total = sum(sol.values())
        print(f"Solución {i}: Comida: ${sol['comida']}, Transporte: ${sol['transporte']}, Ocio: ${sol['ocio']} | Total: ${total}")
else:
    print("\nNo se encontró ninguna solución que cumpla las restricciones.")
# CSP optimizado: Presupuesto semanal con búsqueda de todas las soluciones