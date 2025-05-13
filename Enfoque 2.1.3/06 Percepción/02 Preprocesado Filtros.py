import cv2  # Importamos OpenCV para procesamiento de imágenes.
import numpy as np  # Importamos NumPy para operaciones con matrices.

# Cargar una imagen
img = cv2.imread("C:\Users\Jair\Desktop\BrandonJairLunaPinto_IA_P1_Algoritmos\carro.jpeg", cv2.IMREAD_GRAYSCALE)
# Leemos la imagen desde la ruta especificada y la convertimos a escala de grises.

# Verificar si la imagen se cargó correctamente
if img is None:
    print("Error al cargar la imagen. Verifica la ruta.")  # Mensaje de error si no se encuentra la imagen.
else:
    print("Imagen cargada correctamente.")  # Mensaje de confirmación si la imagen se cargó.

# Aplicar un filtro de suavizado (Gaussian blur)
filtro_suavizado = cv2.GaussianBlur(img, (5, 5), 0)
# Aplicamos un filtro de suavizado Gaussiano con un kernel de 5x5 y desviación estándar 0.

# Mostrar la imagen original y la filtrada
cv2.imshow("Original", img)  # Mostramos la imagen original.
cv2.imshow("Imagen Filtrada", filtro_suavizado)  # Mostramos la imagen suavizada.
cv2.waitKey(0)  # Esperamos a que se presione una tecla para cerrar las ventanas.
cv2.destroyAllWindows()  # Cerramos todas las ventanas abiertas por OpenCV.

# Este código carga una imagen en escala de grises y aplica un filtro de suavizado utilizando Gaussian Blur.
# Luego, muestra la imagen original y la imagen filtrada.
# Asegúrate de reemplazar "C:\Users\Jair\Desktop\BrandonJairLunaPinto_IA_P1_Algoritmos\carro.jpeg" con la ruta real de tu imagen.