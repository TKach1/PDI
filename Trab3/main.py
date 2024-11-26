# este trabalho foi feita com a programação mais PORCA existente, feito em 10 minutos no máximo arredondando

import numpy as np
import cv2

threshold = 0.70
tamanhoBlur = [11, 11]
sigma = 10
borradas = 4

img = cv2.imread("faker.jfif")
img = img.astype (np.float32) / 255

brightPass = img.copy()

for y in range(len(img)):
    for x in range(len(img[0])):
        if img[y][x][0] > threshold and img[y][x][1] > threshold and img[y][x][2] > threshold:
            brightPass[y][x][0] = img[y][x][0]
            brightPass[y][x][1] = img[y][x][1]
            brightPass[y][x][2] = img[y][x][2]
        else:
            brightPass[y][x] = [0, 0, 0]
        
borrarGauss = cv2.GaussianBlur(brightPass, [0,0], sigma)
for i in range(borradas-1):
    borrarGauss += cv2.GaussianBlur(brightPass, [0,0], sigma)

borrar = cv2.blur(brightPass, tamanhoBlur)
for i in range(borradas-1):
    borrar += cv2.blur(borrar, tamanhoBlur)

cv2.imshow("Bright Pass", brightPass)
cv2.imshow("Borrado", borrar)

cv2.imshow("Imagem Original", img)
imgBox = img + borrar
cv2.imshow("Imagem Final (BoxBlur)", imgBox)
imgGauss = img + borrarGauss
cv2.imshow("Imagem Final (GaussianBlur)", imgGauss)

cv2.waitKey(0)