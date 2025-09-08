print("=== CSP: Mejor combinación de presupuesto semanal ===")

# Entradas
presupuesto_total = int(input("Ingresa tu presupuesto total para la semana: "))
min_comida = int(input("Gasto mínimo en comida: "))
min_transporte = int(input("Gasto mínimo en transporte: "))
max_ocio = int(input("Gasto máximo en ocio: "))

# Variables y dominios con pasos grandes
variables = ['comida', 'transporte', 'ocio']
dominios = {
    'comida': list(range(min_comida, presupuesto_total + 1, 10)),
    'transporte': list(range(min_transporte, presupuesto_total + 1, 10)),
    'ocio': list(range(0, max_ocio + 1, 5))
}

# Restricciones
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

# Backtracking que guarda solo la mejor solución
mejor_solucion = None
mejor_sobrante = -1  # dinero sobrante máximo

def backtracking_mejor(asignacion={}):
    global mejor_solucion, mejor_sobrante
    if len(asignacion) == len(variables):
        total = sum(asignacion.values())
        sobrante = presupuesto_total - total
        if sobrante > mejor_sobrante:
            mejor_sobrante = sobrante
            mejor_solucion = asignacion.copy()
        return
    var = next(v for v in variables if v not in asignacion)
    for valor in dominios[var]:
        asignacion[var] = valor
        if restricciones(asignacion):
            backtracking_mejor(asignacion)
        asignacion.pop(var)

# Ejecutar búsqueda
backtracking_mejor()

if mejor_solucion:
    total = sum(mejor_solucion.values())
    sobrante = presupuesto_total - total
    print("\nMejor solución encontrada:")
    for cat, gasto in mejor_solucion.items():
        print(f"  {cat.capitalize()}: ${gasto}")
    print(f"  Total gastado: ${total}")
    print(f"  Dinero sobrante: ${sobrante}")
else:
    print("No se encontró ninguna solución válida.")
