"""
Dibujar curvas Bezier 
Partiendo de unos puntos de control 
Crear una curva cubica con la interpolacion
de polinomios de Berstein

Script para ser ejecutado en Google Colab

JCA
"""

import numpy as np
from google.colab.patches import cv2_imshow
import cv2 as cv

def draw_points (im, points, color = (0,255,0)):
    pass

def bezier(im, points, color=(255,0,0)):
    pass


w = 500
h = 500
im = np.zeros((w,h,3), np.uint8)
control_points= np.array([[30, 300],[80,100],[250,250],[350, 120]])
bezier(im, control_points)
draw_points(im, control_points)
cv2_imshow(im)
