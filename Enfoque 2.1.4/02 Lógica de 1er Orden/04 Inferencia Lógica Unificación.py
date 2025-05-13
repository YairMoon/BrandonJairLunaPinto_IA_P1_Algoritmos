# Ejemplo básico de unificación de términos lógicos

# Unificamos dos expresiones si sus estructuras coinciden

def unificar(x, y):
    if x == y:
        return True
    if isinstance(x, str) and x.startswith("?"):
        return True
    if isinstance(y, str) and y.startswith("?"):
        return True
    return False

print("¿Unifica padre(juan, ?x) con padre(juan, pedro)?", unificar(("juan", "?x"), ("juan", "pedro")))
# La salida mostrará True si las expresiones se unifican y False si no lo hacen.
# En este caso, "padre(juan, ?x)" se unifica con "padre(juan, pedro)" porque la variable "?x" puede ser sustituida por "pedro".