import cv2  # Importamos OpenCV para procesamiento de imágenes.
import numpy as np  # Importamos NumPy para operaciones con matrices.

# Cargar la imagen
img = cv2.imread("ruta_a_imagen.jpg", cv2.IMREAD_GRAYSCALE) # Leemos la imagen en escala de grises.
# Leemos la imagen desde la ruta especificada y la convertimos a escala de grises.

# Aplicar el operador de Canny para detectar bordes
edges = cv2.Canny(img, 50, 150, apertureSize=3) # Aplicamos el detector de bordes de Canny con umbrales de 50 y 150, y un tamaño de apertura de 3.
# Aplicamos el detector de bordes de Canny con umbrales de 50 y 150, y un tamaño de apertura de 3.

# Detectar líneas usando la transformada de Hough
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10) 
# Usamos la transformada de Hough probabilística para detectar líneas en la imagen.
# Parámetros:
# - 1: Resolución en píxeles del acumulador.
# - np.pi / 180: Resolución angular en radianes.
# - threshold=100: Número mínimo de intersecciones en el acumulador para considerar una línea.
# - minLineLength=50: Longitud mínima de una línea para ser detectada.
# - maxLineGap=10: Máxima separación entre segmentos de línea para unirlos.

# Dibujar las líneas detectadas
for line in lines:
    x1, y1, x2, y2 = line[0]  # Extraemos las coordenadas de cada línea detectada.
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Dibujamos cada línea sobre la imagen original en color verde (0, 255, 0) con un grosor de 2 píxeles.

# Mostrar la imagen con las líneas etiquetadas
cv2.imshow("Imagen con Líneas Etiquetadas", img)  # Mostramos la imagen con las líneas detectadas.
cv2.waitKey(0)  # Esperamos a que se presione una tecla para cerrar las ventanas.
cv2.destroyAllWindows()  # Cerramos todas las ventanas abiertas por OpenCV.

# Este código carga una imagen en escala de grises, aplica el operador de Canny para detectar bordes
# y luego utiliza la transformada de Hough para detectar líneas. Finalmente, dibuja las líneas detectadas
# sobre la imagen original y muestra el resultado.