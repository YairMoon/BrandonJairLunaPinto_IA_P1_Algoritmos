# Una red jerárquica de tareas representa las dependencias entre ellas
# Definimos un ejemplo de red jerárquica de tareas en un diccionario

tareas = {
    "Proyecto": ["Investigación", "Desarrollo", "Pruebas"],
    "Investigación": ["Búsqueda de información", "Análisis de datos"],
    "Desarrollo": ["Codificación", "Documentación"],
    "Pruebas": ["Pruebas unitarias", "Pruebas de integración"]
}

# Función que muestra la jerarquía de tareas
def mostrar_tareas(tareas, tarea):
    print(f"Tarea principal: {tarea}")
    for sub_tarea in tareas.get(tarea, []):
        mostrar_tareas(tareas, sub_tarea)

mostrar_tareas(tareas, "Proyecto")
# La salida mostrará la jerarquía de tareas, comenzando desde la tarea principal "Proyecto" y descendiendo a través de las sub-tareas.
# Esto es útil para visualizar la estructura de un proyecto y las tareas que deben completarse en cada etapa.