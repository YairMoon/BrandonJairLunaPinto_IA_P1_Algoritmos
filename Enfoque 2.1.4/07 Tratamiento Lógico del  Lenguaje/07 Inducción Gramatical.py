# La inducción gramatical se refiere a aprender una gramática a partir de ejemplos.
# Simularemos un proceso de inducción a partir de ejemplos de oraciones simples.

def induccion_gramatical(oraciones):
    # Definir reglas simples de gramática
    reglas = []
    for oracion in oraciones:
        if len(oracion) == 3:  # Sujeto + Verbo + Objeto
            reglas.append("Sujeto + Verbo + Objeto")
    return reglas

# Ejemplo de uso
oraciones = [["Juan", "come", "manzana"], ["Ana", "corre", "camino"]]
resultado = induccion_gramatical(oraciones)
print("Reglas aprendidas:", resultado)  # ['Sujeto + Verbo + Objeto', 'Sujeto + Verbo + Objeto']
# Output:
# Reglas aprendidas: ['Sujeto + Verbo + Objeto', 'Sujeto + Verbo + Objeto']
# La inducción gramatical es un proceso complejo y este es un ejemplo simplificado.
# En la práctica, se utilizan algoritmos más avanzados y conjuntos de datos más grandes para aprender gramáticas complejas.