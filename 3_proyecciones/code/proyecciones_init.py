import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow

# Funciones
def draw(vertices, edges, im):
    """Dibuja objeto definido por vertices y bordes"""
    # Normalizar coordenadas homogeneas
    v_h = np.array([ v[:-2]/v[-1] for v in vertices])
    for e in edges:
        cv.line(im, tuple(v_h[e[0]].astype(int)), tuple(v_h[e[1]].astype(int)), (255,0,15), 2)
    for v in v_h:
        cv.circle(im, tuple(v.astype(int)), 3, (255,0,255),-1)

### ---------- DEFINIR FUNCIONES ---------- ###
def translate3d(vertex, dx, dy, dz):
    """Operación de traslación 3d"""

def project2D(vertex, f=35, w=100, h=100):
    """Aplica una transformacion de proyeccion pinhole"""


### ---------- DEFINIT GEOMETRIA  ---------- ###    
# Cubo definido en su sistema coordenado
# Lista de vertices [[x, y, z,1], ...
v = None
# List de bordes que relacionan los indices de los vertices
# [(0,1), (1,2), ....
edges = None


### ---------- TRASLADAR CUBO A POSICION INDICADA ---------- ###



# Parametros camara
f = 200 # Distancia focal
# Tamano imagen
w = 500
h = 500

### ---------- PROYECTAR VERTICES ---------- ###
# Proyectar 3D -> 2D



###----------  TRASLADAR PROYECCION A CENTRO DE IMAGEN ---------- ###


# Dibujar y mostrar
im = np.zeros((h,w,3), np.uint8)
draw(vp, edges, im)
cv2_imshow(im)
