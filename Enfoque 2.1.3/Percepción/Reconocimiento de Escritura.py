import pytesseract
from PIL import Image

# Cargar una imagen que contenga texto escrito
img = Image.open("ruta_a_imagen.jpg")

# Usar Tesseract para hacer OCR y extraer texto
texto = pytesseract.image_to_string(img)

# Mostrar el texto extraído
print("Texto extraído:", texto)
# Este código utiliza la biblioteca pytesseract para realizar el reconocimiento óptico de caracteres (OCR) en una imagen. Carga una imagen que contiene texto escrito y utiliza Tesseract para extraer el texto. Finalmente, imprime el texto extraído en la consola.
# Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.