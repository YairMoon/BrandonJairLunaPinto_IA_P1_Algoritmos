# Lógica difusa: pertenencia parcial a un conjunto

# Grado de pertenencia a "temperatura alta"
def temperatura_alta(grado):
    if grado <= 20:
        return 0.0
    elif 20 < grado < 30:
        return (grado - 20) / 10
    else:
        return 1.0

temperaturas = [15, 22, 28, 35]

# Evaluamos la pertenencia difusa
for t in temperaturas:
    print(f"Temperatura: {t}°C → Grado de 'alta': {temperatura_alta(t):.2f}")
# La salida mostrará el grado de pertenencia a la categoría "alta" para cada temperatura.
# Esto es útil en sistemas de control difuso, donde se necesita evaluar la pertenencia a múltiples categorías.