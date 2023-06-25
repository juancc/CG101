from google.colab.patches import cv2_imshow
import numpy as np
import cv2 as cv


def draw_triangle(im, triangle, color=(0,255,0)):
    # Normalizar coordenadas homogeneas
    triangle = np.array([ v[:-1]/v[-1] for v in triangle] , np.uint16)
    cv.drawContours(im, [triangle.astype(int)], 0, color, -1)
    for v in triangle:
        cv.circle(im, tuple(v), 2, (255,0,255),-1)

def scale(vertex, sx, sy):
    pass

def rotate(vertex, a):
    pass

def translate(vertex, dx, dy):
    pass

# image size
w = 500
h = 500
im = np.zeros((h,w,3), np.uint8)

# Parametros de las transformaciones
# Traslada a centro y realiza escala y rotacion
angle = 30
s = 3
t = 250
# Sistema coordenado de imagenes
triangle1 = np.array( [[10,10,1], [70,10,1], [40, 60,1]])
triangle2 = translate(rotate( scale(translate(triangle1, -40,-30),s,s) ,angle), t,t)

draw_triangle(im, triangle1)
draw_triangle(im, triangle2, color= (0,100,255))

cv2_imshow(im)
