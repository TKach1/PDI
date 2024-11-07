# este trabalho foi feita com a programação mais PORCA existente, feito em 10 minutos no máximo arredondando

import numpy as np
import cv2

threshold = 0.87
tamanhoBlur = [15, 15]
sigma = 2
borradas = 2

img = cv2.imread("image.jpg")
img = img.astype (np.float32) / 255

brightPass = np.where(img < threshold, 0, img)

borrar = cv2.GaussianBlur(brightPass, tamanhoBlur, 3)
for i in range(borradas):
    borrar += cv2.blur(borrar, tamanhoBlur)

cv2.imshow("Bright Pass", brightPass)
cv2.imshow("Borrado", borrar)

cv2.imshow("Imagem Original", img)
img = img + borrar
cv2.imshow("Imagem Final", img)
cv2.waitKey(0)