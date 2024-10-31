import numpy as np
import cv2

INPUT_IMAGE = 'image.jpg'
BOX_HEIGHT = 7
BOX_WIDTH = 7

def ingenuous(img, h, w):
    for y in range(int(h/2), len(img)-int(h/2)):
        for x in range(int(h/2), len(img[0])-int(h/2)):
            soma = 0
            for dy in range(y-int(h/2), y+int(h/2)):
                for dx in range(x-int(w/2), x+int(w/2)):
                    soma += img[dy][dx]
            img[y][x] = soma / (h*w)

def main ():

    img = cv2.imread (INPUT_IMAGE)
    img = img.astype (np.float32) / 255
    img = np.tile(img, (3,3,1))

    upCut = int(len(img)/3 - BOX_HEIGHT)
    downCut = int(len(img) - len(img)/3 + BOX_HEIGHT)
    leftCut = int(len(img[0])/3 - BOX_WIDTH)
    rightCut = int(len(img[0]) - len(img[0])/3 + BOX_WIDTH)
    img = img[upCut:downCut, leftCut:rightCut]

    ingenuous(img, BOX_HEIGHT, BOX_WIDTH)

    img = img[BOX_HEIGHT:len(img) - BOX_HEIGHT, BOX_WIDTH:len(img[0]) - BOX_WIDTH]

    cv2.imshow('blur', img)

    cv2.waitKey ()
    cv2.destroyAllWindows ()


if __name__ == '__main__':
    main ()