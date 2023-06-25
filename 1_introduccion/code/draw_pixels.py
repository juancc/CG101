"""
Dibujar pixeles en Google Colab
"""
from google.colab.patches import cv2_imshow
import numpy as np

w = 100
h = 100

im = np.zeros((h,w,3), np.uint8)

i = 50
im[i,i] = [255,255,255]

cv2_imshow(im)
