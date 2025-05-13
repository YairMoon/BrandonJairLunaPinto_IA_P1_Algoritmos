import cv2  # Importamos OpenCV para procesamiento de imágenes.
import numpy as np  # Importamos NumPy para operaciones con matrices.

# Cargar la imagen
img = cv2.imread("C:\Users\Jair\Desktop\BrandonJairLunaPinto_IA_P1_Algoritmos\carro.jpeg", cv2.IMREAD_GRAYSCALE) # Leemos la imagen en escala de grises.
# Leemos la imagen desde la ruta especificada y la convertimos a escala de grises.

# Aplicar un filtro Canny para detección de aristas
aristas = cv2.Canny(img, 100, 200) # Aplicamos el detector de bordes de Canny con umbrales de 100 y 200.
# Aplicamos el detector de bordes de Canny con umbrales de 100 y 200.

# Mostrar la imagen original y la imagen con aristas
cv2.imshow("Imagen Original", img)  # Mostramos la imagen original.
cv2.imshow("Aristas Detectadas", aristas)  # Mostramos la imagen con las aristas detectadas.
cv2.waitKey(0)  # Esperamos a que se presione una tecla para cerrar las ventanas.
cv2.destroyAllWindows()  # Cerramos todas las ventanas abiertas por OpenCV.

# Este código carga una imagen en escala de grises y aplica un filtro Canny para detectar aristas.
# Luego, muestra la imagen original y la imagen con las aristas detectadas.
# Asegúrate de reemplazar "ruta_a_imagen.jpg" con la ruta real de tu imagen.