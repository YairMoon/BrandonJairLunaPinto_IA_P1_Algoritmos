# Base de conocimiento con lógica no monotónica

# Hechos iniciales
hechos = {"ave": True}

# Regla: si es un ave, entonces vuela (por defecto)
def puede_volar(hechos):
    if hechos.get("ave") and not hechos.get("no_vuela"):
        return True
    return False

print("¿Puede volar?", puede_volar(hechos))

# Añadimos un nuevo hecho que invalida el anterior
hechos["no_vuela"] = True

print("¿Puede volar después del nuevo hecho?", puede_volar(hechos))
# La salida mostrará que inicialmente puede volar, pero después de añadir el hecho "no_vuela", ya no puede volar.
# En este ejemplo, la lógica no monotónica permite que el sistema cambie su conclusión inicial (que puede volar) al recibir nueva información (que no vuela).