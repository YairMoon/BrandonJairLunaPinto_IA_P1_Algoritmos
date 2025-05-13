import pytesseract  # Importamos pytesseract para realizar OCR (Reconocimiento Óptico de Caracteres).
from PIL import Image  # Importamos PIL para manejar imágenes.

# Cargar una imagen que contenga texto escrito
img = Image.open("ruta_a_imagen.jpg")
# Abrimos la imagen desde la ruta especificada. Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.

# Usar Tesseract para hacer OCR y extraer texto
texto = pytesseract.image_to_string(img)
# Utilizamos pytesseract para procesar la imagen y extraer el texto contenido en ella.

# Mostrar el texto extraído
print("Texto extraído:", texto)
# Imprimimos el texto extraído en la consola.

# Este código utiliza la biblioteca pytesseract para realizar el reconocimiento óptico de caracteres (OCR) en una imagen.
# Carga una imagen que contiene texto escrito y utiliza Tesseract para extraer el texto.
# Finalmente, imprime el texto extraído en la consola.