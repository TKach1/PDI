import numpy as np
import cv2

imgs = ['60.bmp', '82.bmp', '114.bmp', '150.bmp' ,'205.bmp'] 

for img in imgs:
    imgName = img
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype (np.float32) / 255

    borrada = cv2.blur(img, [51, 51])
    img = img - borrada

    img = cv2.normalize(img, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8U)
    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow(imgName, thresh)

cv2.waitKey(0)  