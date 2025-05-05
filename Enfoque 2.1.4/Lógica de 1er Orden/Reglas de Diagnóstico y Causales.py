# Simulación de reglas de diagnóstico y causales en un sistema médico

# Síntomas del paciente
sintomas = {"fiebre", "tos", "dolor de cabeza"}

# Base de reglas: si tiene ciertos síntomas, puede ser una enfermedad
def diagnosticar(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible gripe"
    elif "dolor de cabeza" in sintomas:
        return "Posible migraña"
    else:
        return "Desconocido"

print("Diagnóstico:", diagnosticar(sintomas))
# La salida mostrará el diagnóstico basado en los síntomas proporcionados.
# En este caso, si el paciente tiene fiebre y tos, se diagnostica como posible gripe.