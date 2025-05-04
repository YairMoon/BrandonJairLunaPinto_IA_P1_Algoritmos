import re

# Texto de ejemplo
texto = "Juan trabaja en Google desde 2018 y su email es juan@google.com"

# Expresión regular para encontrar direcciones de email
emails = re.findall(r'\S+@\S+', texto)

print("Emails encontrados:", emails)
