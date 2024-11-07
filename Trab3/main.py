# este trabalho foi feita com a programação mais PORCA existente, feito em 10 minutos no máximo arredondando

import numpy as np
import cv2

threshold = 0.87
tamanhoBlur = [15, 15]
sigma = 10
borradas = 3

img = cv2.imread("image.jpg")
img = img.astype (np.float32) / 255

brightPass = np.where(img < threshold, 0, img)

borrarGauss = cv2.GaussianBlur(brightPass, [0,0], sigma)

borrar = cv2.blur(brightPass, tamanhoBlur)
for i in range(borradas-1):
    borrar += cv2.blur(borrar, tamanhoBlur)

cv2.imshow("Bright Pass", brightPass)
cv2.imshow("Borrado", borrar)

cv2.imshow("Imagem Original", img)
imgBox = img + borrar
cv2.imshow("Imagem Final (BoxBlur)", imgBox)
imgGauss = img + borrarGauss
cv2.imshow("Imagem Final (GaussianBlur)", imgBox)

cv2.waitKey(0)