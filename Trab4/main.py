import numpy as np
import cv2

imgs = ['60.bmp', '82.bmp', '114.bmp', '150.bmp' ,'205.bmp'] 

for img in imgs:
    imgName = img
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype (np.float32) / 255

    borrada = cv2.blur(img, [51, 51]) # o tamanho deste blur foi selecionado de forma que a imagem tenha + que 25 pixels
    img = img - borrada               # (supondo que se tirar uma foto de 1 ou vários arrozes com menos de 26 pixels não faria sentido)

    img = cv2.normalize(img, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8U)
    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8) # kernel size mínimo para retirar pixeis unitários de ruído

    thresh = cv2.erode(thresh, kernel)
    thresh = cv2.dilate(thresh, kernel)

    cv2.imshow(imgName + '- binarizada', thresh)

    totalRicePixels = 0

    for x in range(len(thresh)):
        for y in range(len(thresh[0])):
            if thresh[x][y] == 255:
                totalRicePixels += 1
    
    n_objects = 0
    mask = thresh.copy()
    mask = mask.astype (np.float32) / 255
    label = 0.1
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if mask[i, j] == 1:
                n_objects += 1
                cv2.floodFill(mask, None, (j, i), newVal=label)
                label += 0.1
    
    pixel_counts, pixel_counts = np.unique(mask, return_counts=True)
    
    blob = pixel_counts[1 : len(pixel_counts)]

    #----- aplicando remoção de outliers

    media = np.mean(blob)
    desvio_padrao = np.std(blob)

    limite_inferior = media - 1 * desvio_padrao
    limite_superior = media + 1 * desvio_padrao

    valores_filtrados = blob[(blob >= limite_inferior) & (blob <= limite_superior)]
    soma_filtrados = np.sum(valores_filtrados)

    mediaDePixelsPorBlob = soma_filtrados // len(valores_filtrados)

    riceTotal = 0
    for i in range(len(blob)): 
        riceTotal += round(blob[i] / mediaDePixelsPorBlob)

    print(riceTotal)

    cv2.waitKey(0)

cv2.waitKey(0)  