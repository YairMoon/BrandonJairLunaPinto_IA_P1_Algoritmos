import re
# Importamos la biblioteca `re` para trabajar con expresiones regulares.

# Texto de ejemplo
texto = "Juan trabaja en Google desde 2018 y su email es juan@google.com"
# Definimos un texto de ejemplo que contiene información como nombres, empresas y correos electrónicos.

# Expresión regular para encontrar direcciones de email
emails = re.findall(r'\S+@\S+', texto)
# Utilizamos una expresión regular para buscar direcciones de correo electrónico en el texto.
# `\S+` significa "uno o más caracteres que no son espacios".
# `@` busca el símbolo de arroba.
# `\S+` después del arroba busca el dominio del correo.

print("Emails encontrados:", emails)
# Mostramos las direcciones de correo electrónico encontradas en el texto.