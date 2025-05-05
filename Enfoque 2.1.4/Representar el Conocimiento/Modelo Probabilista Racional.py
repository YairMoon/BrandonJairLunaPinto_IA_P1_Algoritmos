# Elegimos la acción con mayor utilidad esperada
acciones = {
    "estudiar": 0.9 * 100,  # 90% de sacar 100
    "jugar": 0.4 * 60,      # 40% de pasar
    "dormir": 0.1 * 70      # 10% de pasar
}

# Seleccionamos la mejor acción
mejor_accion = max(acciones, key=acciones.get)
print("La mejor acción es:", mejor_accion)
# La salida mostrará la acción con la mayor utilidad esperada.
# En este caso, "estudiar" tiene la mayor utilidad esperada, por lo que es la mejor opción.