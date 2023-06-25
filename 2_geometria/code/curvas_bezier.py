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
    for p in points:
        cv.circle(im, tuple(p), 2, color,-1)

def bezier(im, points, color=(255,0,0)):
    for i in range(0, 1000):
        t = i/1000
        a = 1-t
        p_c = (points[0] * np.power(a,3)) + (points[1] * 3*t* np.power(a,2)) + (points[2] * 3* np.power(t,2)*a) + ( points[3]* np.power(t,3))
        im[int(p_c[1]), int(p_c[0])] = color

w = 500
h = 500
im = np.zeros((w,h,3), np.uint8)
control_points= np.array([[30, 300],[80,100],[250,250],[350, 120]])
bezier(im, control_points)
draw_points(im, control_points)
cv2_imshow(im)
