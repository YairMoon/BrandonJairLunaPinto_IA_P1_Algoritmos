# Ejemplo de Lógica de Orden Superior: funciones como argumentos

# Definimos una propiedad: ser par
def es_par(x):
    return x % 2 == 0

# Función de orden superior que acepta otra función como argumento
def aplicar_predicado(lista, predicado):
    return [x for x in lista if predicado(x)]

# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Aplicamos la lógica: filtrar solo los pares
resultado = aplicar_predicado(numeros, es_par)

print("Números pares:", resultado)
# Salida esperada: Números pares: [2, 4, 6]
# Ejemplo de Lógica de Orden Superior: funciones como valores de retorno