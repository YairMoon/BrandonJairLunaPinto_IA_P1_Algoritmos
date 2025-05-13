# Representamos hechos con certeza asociada (0 a 1)
hechos = {
    "lloverá mañana": 0.8,
    "habrá tráfico": 0.6
}

# Mostramos el grado de certeza
for hecho, certeza in hechos.items():
    print(f"Certeza de que {hecho}: {certeza * 100}%")
