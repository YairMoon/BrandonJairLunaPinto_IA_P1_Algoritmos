# Definimos un espacio de estados con diferentes condiciones y acciones
estados = ["inicio", "en_ruta", "en_destino"]
acciones = {
    "inicio": ["moverse", "esperar"],
    "en_ruta": ["detenerse", "continuar"],
    "en_destino": ["terminar"]
}

# Función que muestra el siguiente estado dado el estado actual
def siguiente_estado(estado_actual, accion):
    if accion in acciones[estado_actual]:
        if accion == "moverse" and estado_actual == "inicio":
            return "en_ruta"
        elif accion == "continuar" and estado_actual == "en_ruta":
            return "en_destino"
        else:
            return estado_actual
    return estado_actual

# Ejemplo de transición en el espacio de estados
estado_actual = "inicio"
estado_actual = siguiente_estado(estado_actual, "moverse")
estado_actual = siguiente_estado(estado_actual, "continuar")
print("Estado final:", estado_actual)
# El estado final debe ser "en_destino" después de realizar las acciones definidas.
# La salida mostrará el estado final después de aplicar las acciones en el espacio de estados.